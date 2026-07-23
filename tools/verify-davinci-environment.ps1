[CmdletBinding()]
param(
    [switch]$AllowMissingResolve
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$python312 = 'C:\Users\SE\AppData\Local\Programs\Python\Python312\python.exe'
$managedRoot = 'C:\Users\SE\AppData\Local\davinci-resolve-mcp'
$managedPython = Join-Path $managedRoot 'venv\Scripts\python.exe'
$coreServer = Join-Path $managedRoot 'src\server.py'
$advancedRoot = 'C:\Users\SE\AppData\Local\davinci-resolve-mcp-advanced'
$advancedPackage = Join-Path $advancedRoot 'node_modules\davinci-resolve-mcp'
$advancedServer = Join-Path $advancedPackage 'bin\davinci-resolve-advanced-mcp.mjs'
$resolveExe = 'C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe'
$resolveApi = 'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting'
$resolveLib = 'C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll'
$results = [System.Collections.Generic.List[object]]::new()

function Add-Result {
    param(
        [string]$Check,
        [bool]$Passed,
        [bool]$Required,
        [string]$Evidence
    )

    $status = if ($Passed) { 'PASS' } elseif ($Required) { 'FAIL' } else { 'SKIP' }
    $script:results.Add([pscustomobject]@{
        Check = $Check
        Status = $status
        Evidence = $Evidence
    })
}

Add-Result 'runtime:python-3.12' (Test-Path -LiteralPath $python312) $true $python312
Add-Result 'mcp:core-server-files' ((Test-Path -LiteralPath $managedPython) -and (Test-Path -LiteralPath $coreServer)) $true $managedRoot
Add-Result 'mcp:advanced-server-files' (Test-Path -LiteralPath $advancedServer) $true $advancedServer

$advancedVersion = $null
$advancedPackageJson = Join-Path $advancedPackage 'package.json'
if (Test-Path -LiteralPath $advancedPackageJson) {
    $advancedVersion = (Get-Content -LiteralPath $advancedPackageJson -Raw | ConvertFrom-Json).version
}
Add-Result 'mcp:advanced-version' ($advancedVersion -eq '2.63.0') $true "installed=$advancedVersion; expected=2.63.0"

$mcpPath = Join-Path $repoRoot '.mcp.json'
$claudeNames = @()
if (Test-Path -LiteralPath $mcpPath) {
    $mcpConfig = Get-Content -LiteralPath $mcpPath -Raw | ConvertFrom-Json
    $claudeNames = @($mcpConfig.mcpServers.PSObject.Properties.Name)
}
Add-Result 'claude:core-registered' ($claudeNames -contains 'davinci-resolve') $true $mcpPath
Add-Result 'claude:advanced-registered' ($claudeNames -contains 'davinci-resolve-advanced') $true $mcpPath

$codexList = (& codex mcp list 2>&1 | Out-String)
Add-Result 'codex:core-registered' ($codexList -match '(?m)^davinci-resolve\s') $true 'codex mcp list'
Add-Result 'codex:advanced-registered' ($codexList -match '(?m)^davinci-resolve-advanced\s') $true 'codex mcp list'

$probeScript = @'
import asyncio
import json
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

CORE_PYTHON = r"C:\Users\SE\AppData\Local\davinci-resolve-mcp\venv\Scripts\python.exe"
CORE_SERVER = r"C:\Users\SE\AppData\Local\davinci-resolve-mcp\src\server.py"
ADVANCED_SERVER = r"C:\Users\SE\AppData\Local\davinci-resolve-mcp-advanced\node_modules\davinci-resolve-mcp\bin\davinci-resolve-advanced-mcp.mjs"


async def list_tools(command, args, extra_env):
    env = os.environ.copy()
    env.update(extra_env)
    params = StdioServerParameters(command=command, args=args, env=env)
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()
            return [tool.name for tool in result.tools]


async def main():
    output = {"core": [], "advanced": [], "errors": []}
    try:
        output["core"] = await list_tools(
            CORE_PYTHON,
            [CORE_SERVER],
            {
                "RESOLVE_SCRIPT_API": r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting",
                "RESOLVE_SCRIPT_LIB": r"C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll",
                "PYTHONPATH": r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules",
                "PYTHONHOME": r"C:\Users\SE\AppData\Local\Programs\Python\Python312",
            },
        )
    except BaseException as exc:
        output["errors"].append(f"core: {exc!r}")

    try:
        output["advanced"] = await list_tools(
            "node",
            [ADVANCED_SERVER],
            {
                "AAF_PROBE_PYTHON": CORE_PYTHON,
            },
        )
    except BaseException as exc:
        output["errors"].append(f"advanced: {exc!r}")

    print(json.dumps(output, separators=(",", ":")))


asyncio.run(main())
'@

$previousErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
$probeOutput = $probeScript | & $managedPython - 2>&1
$probeExit = $LASTEXITCODE
$ErrorActionPreference = $previousErrorActionPreference
$probeJsonLine = @($probeOutput | Where-Object { $_ -match '^\{.*\}$' } | Select-Object -Last 1)
$probe = $null
if ($probeJsonLine) {
    try {
        $probe = $probeJsonLine | ConvertFrom-Json
    } catch {}
}

$coreCount = if ($probe) { @($probe.core).Count } else { 0 }
$advancedCount = if ($probe) { @($probe.advanced).Count } else { 0 }
$probeErrors = if ($probe) { @($probe.errors) -join '; ' } else { ($probeOutput | Out-String).Trim() }
Add-Result 'smoke:core-tool-discovery' (($probeExit -eq 0) -and ($coreCount -ge 34)) $true "tools=$coreCount; errors=$probeErrors"
Add-Result 'smoke:advanced-tool-discovery' (($probeExit -eq 0) -and ($advancedCount -ge 18)) $true "tools=$advancedCount; errors=$probeErrors"

$resolveRequired = -not $AllowMissingResolve
Add-Result 'resolve:application-installed' (Test-Path -LiteralPath $resolveExe) $resolveRequired $resolveExe
Add-Result 'resolve:scripting-api-installed' (Test-Path -LiteralPath $resolveApi) $resolveRequired $resolveApi
Add-Result 'resolve:scripting-library-installed' (Test-Path -LiteralPath $resolveLib) $false $resolveLib

$results | Format-Table -AutoSize -Wrap
$failed = @($results | Where-Object { $_.Status -eq 'FAIL' })
if ($failed.Count -gt 0) {
    Write-Error "$($failed.Count) required DaVinci environment check(s) failed."
    exit 1
}

Write-Output "DaVinci MCP checks passed. Resolve checks may be SKIP only when -AllowMissingResolve was supplied."
