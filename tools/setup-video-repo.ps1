<#
.SYNOPSIS
  Check, and optionally repair, this machine so it can produce the repository films.

.DESCRIPTION
  Read-only by default. It reports one row for each requirement, then prints the actions that
  only a human can do. Use -Install to run the safe automated installs.

  This script never prints a credential value. It never runs a login. It never spends money.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1
  powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1 -Install
  powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1 -Json
#>
[CmdletBinding()]
param(
    [switch]$Install,
    [switch]$Json
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$results = [System.Collections.Generic.List[object]]::new()
$humanActions = [System.Collections.Generic.List[string]]::new()

function Add-Row {
    param(
        [string]$Area,
        [string]$Check,
        [string]$Status,
        [string]$Evidence,
        [string]$Fix = ''
    )
    $script:results.Add([pscustomobject]@{
        Area     = $Area
        Check    = $Check
        Status   = $Status
        Evidence = $Evidence
        Fix      = $Fix
    })
}

function Add-Human {
    param([string]$Action)
    if (-not $script:humanActions.Contains($Action)) { $script:humanActions.Add($Action) }
}

function Test-Binary {
    param(
        [string]$Name,
        [string[]]$VersionArgs = @('--version'),
        [string]$Fix,
        [switch]$Optional
    )
    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $command) {
        $status = 'FAIL'
        if ($Optional) { $status = 'WARN' }
        Add-Row 'tool' $Name $status 'not found' $Fix
        return $false
    }
    $version = ''
    try {
        $version = (& $Name @VersionArgs 2>&1 | Select-Object -First 1 | Out-String).Trim()
    } catch {
        $version = $command.Source
    }
    Add-Row 'tool' $Name 'PASS' $version ''
    return $true
}

Write-Output "Repository: $repoRoot"
if ($Install) { Write-Output 'Mode: check and install' } else { Write-Output 'Mode: check only' }
Write-Output ''

# ---------------------------------------------------------------- 1. Host binaries
Test-Binary -Name 'git'     -Fix 'Install Git for Windows from https://git-scm.com/downloads' | Out-Null
Test-Binary -Name 'node'    -Fix 'Install Node.js LTS 20 or newer from https://nodejs.org' | Out-Null
Test-Binary -Name 'npm'     -Fix 'npm ships with Node.js' | Out-Null
Test-Binary -Name 'python'  -Fix 'Install Python 3.12 or newer from https://python.org' | Out-Null
Test-Binary -Name 'ffmpeg'  -VersionArgs @('-version') -Fix 'winget install Gyan.FFmpeg' | Out-Null
Test-Binary -Name 'ffprobe' -VersionArgs @('-version') -Fix 'winget install Gyan.FFmpeg' | Out-Null
$hasUv = Test-Binary -Name 'uv' -Fix 'winget install astral-sh.uv'
Test-Binary -Name 'uvx' -Fix 'winget install astral-sh.uv' -Optional | Out-Null

$gitLfsOk = $false
try {
    $lfsVersion = (& git lfs version 2>&1 | Out-String).Trim()
    $gitLfsOk = $LASTEXITCODE -eq 0
} catch { $lfsVersion = 'not found' }
if ($gitLfsOk) {
    Add-Row 'tool' 'git-lfs' 'PASS' $lfsVersion ''
} else {
    Add-Row 'tool' 'git-lfs' 'FAIL' 'not found' 'winget install GitHub.GitLFS, then run: git lfs install'
}

$ytDlp = Get-Command 'yt-dlp' -ErrorAction SilentlyContinue
if (-not $ytDlp) {
    $fallback = Join-Path $env:USERPROFILE '.local\bin\yt-dlp.exe'
    if (Test-Path -LiteralPath $fallback) { $ytDlp = Get-Item -LiteralPath $fallback }
}
if ($ytDlp) {
    Add-Row 'tool' 'yt-dlp' 'PASS' 'present' ''
} else {
    Add-Row 'tool' 'yt-dlp' 'WARN' 'not found' 'uv tool install yt-dlp'
    if ($Install -and $hasUv) {
        Write-Output 'Installing yt-dlp with uv...'
        & uv tool install yt-dlp
        & uv tool update-shell
    }
}

$higgsfield = Get-Command 'higgsfield' -ErrorAction SilentlyContinue
if ($higgsfield) {
    Add-Row 'tool' 'higgsfield' 'PASS' (& higgsfield --version 2>&1 | Select-Object -First 1) ''
} else {
    Add-Row 'tool' 'higgsfield' 'WARN' 'not found' 'npm install --global @higgsfield/cli@latest'
    if ($Install) {
        Write-Output 'Installing the Higgsfield CLI...'
        & npm install --global '@higgsfield/cli@latest'
    }
}

# ---------------------------------------------------------------- 2. Python packages
$pythonPackages = 'requests librosa matplotlib pillow numpy'
$importCheck = & python -c 'import librosa, matplotlib, PIL, numpy, requests' 2>&1
$pythonOk = $LASTEXITCODE -eq 0
if ($pythonOk) {
    Add-Row 'tool' 'python-packages' 'PASS' 'librosa, matplotlib, pillow, numpy, requests import' ''
} else {
    Add-Row 'tool' 'python-packages' 'FAIL' 'one or more imports failed' "python -m pip install $pythonPackages"
    if ($Install) {
        Write-Output 'Installing the Python packages...'
        & python -m pip install requests librosa matplotlib pillow numpy
    }
}

# ---------------------------------------------------------------- 3. Repository state
$insideRepo = $false
& git -C $repoRoot rev-parse --is-inside-work-tree > $null 2>&1
if ($LASTEXITCODE -eq 0) { $insideRepo = $true }
if ($insideRepo) {
    $branch = (& git -C $repoRoot rev-parse --abbrev-ref HEAD).Trim()
    Add-Row 'repo' 'git-clone' 'PASS' "branch $branch" ''
} else {
    Add-Row 'repo' 'git-clone' 'FAIL' 'not a git work tree' 'Clone the repository first. See docs/SOP-00-SETUP.md step 1.'
}

if ($insideRepo -and $gitLfsOk) {
    if ($Install) {
        Write-Output 'Running git lfs install and git lfs pull...'
        & git -C $repoRoot lfs install | Out-Null
        & git -C $repoRoot lfs pull
    }
    $pointerFiles = [System.Collections.Generic.List[string]]::new()
    $lfsPaths = @(& git -C $repoRoot lfs ls-files --name-only 2>$null)
    foreach ($relative in $lfsPaths) {
        if (-not $relative) { continue }
        $full = Join-Path $repoRoot ($relative -replace '/', '\')
        if (-not (Test-Path -LiteralPath $full)) { $pointerFiles.Add($relative); continue }
        if ((Get-Item -LiteralPath $full).Length -lt 1024) { $pointerFiles.Add($relative) }
    }
    if ($lfsPaths.Count -eq 0) {
        Add-Row 'repo' 'git-lfs-media' 'WARN' 'no LFS files listed on this branch' 'Confirm you are on the branch that carries the showcase videos.'
    } elseif ($pointerFiles.Count -eq 0) {
        Add-Row 'repo' 'git-lfs-media' 'PASS' "$($lfsPaths.Count) LFS file(s) present as real media" ''
    } else {
        Add-Row 'repo' 'git-lfs-media' 'FAIL' "$($pointerFiles.Count) file(s) are still pointers" 'git lfs install; git lfs pull'
    }
}

$dotenvPath = Join-Path $repoRoot '.env'
$dotenvIgnored = $false
if ($insideRepo) {
    & git -C $repoRoot check-ignore -q -- '.env'
    $dotenvIgnored = $LASTEXITCODE -eq 0
}
if ($dotenvIgnored) {
    Add-Row 'repo' 'dotenv-ignored' 'PASS' '.env is ignored by Git' ''
} else {
    Add-Row 'repo' 'dotenv-ignored' 'FAIL' '.env is not ignored' 'Never commit .env. Restore the .gitignore rule before adding any key.'
}

$mcpPath = Join-Path $repoRoot '.mcp.json'
if (Test-Path -LiteralPath $mcpPath) {
    $mcpRaw = Get-Content -LiteralPath $mcpPath -Raw
    $mcpDirty = [bool]($mcpRaw -match '(?i)api[_-]?key\s*["'']?\s*[:=]\s*["'']?[A-Za-z0-9_-]{16,}')
    if ($mcpDirty) {
        Add-Row 'repo' 'mcp-no-secrets' 'FAIL' 'a key-shaped value is present in .mcp.json' 'Remove the value and rotate that credential now.'
    } else {
        Add-Row 'repo' 'mcp-no-secrets' 'PASS' 'no key-shaped value in .mcp.json' ''
    }

    $mcp = $mcpRaw | ConvertFrom-Json
    foreach ($serverName in $mcp.mcpServers.PSObject.Properties.Name) {
        $server = $mcp.mcpServers.$serverName
        $commandPath = [string]$server.command
        $resolvable = $false
        if ($commandPath -match '[\\/]') {
            $resolvable = Test-Path -LiteralPath $commandPath
        } else {
            $resolvable = [bool](Get-Command $commandPath -ErrorAction SilentlyContinue)
        }
        $required = $serverName -eq 'ElevenLabs'
        if ($resolvable) {
            Add-Row 'mcp' $serverName 'PASS' 'command resolves on this machine' ''
        } elseif ($required) {
            Add-Row 'mcp' $serverName 'FAIL' "command not found: $commandPath" 'Install uv, then set the ElevenLabs command path in .mcp.json for this machine.'
        } else {
            Add-Row 'mcp' $serverName 'WARN' "optional server; command not found: $commandPath" 'Optional. Remove the entry or fix the path if you want Resolve control.'
        }
    }
} else {
    Add-Row 'repo' 'mcp-config' 'FAIL' '.mcp.json missing' 'Restore .mcp.json from Git.'
}

# ---------------------------------------------------------------- 4. Credentials, presence only
$elevenProcess = -not [string]::IsNullOrWhiteSpace($env:ELEVENLABS_API_KEY)
$elevenUser = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('ELEVENLABS_API_KEY', 'User'))
if ($elevenProcess -or $elevenUser) {
    Add-Row 'credential' 'ELEVENLABS_API_KEY' 'PASS' 'present in the environment; value not displayed' ''
} else {
    Add-Row 'credential' 'ELEVENLABS_API_KEY' 'HUMAN' 'absent' 'Set the user environment variable ELEVENLABS_API_KEY.'
    Add-Human 'Create an ElevenLabs API key and set the Windows user environment variable ELEVENLABS_API_KEY. Open a new terminal afterwards.'
}

$sarvamPresent = -not [string]::IsNullOrWhiteSpace($env:SARVAM_API_KEY)
if (-not $sarvamPresent -and (Test-Path -LiteralPath $dotenvPath)) {
    $sarvamPresent = [bool](Get-Content -LiteralPath $dotenvPath | Where-Object {
        $_ -match '^\s*(?:export\s+)?SARVAM_API_KEY\s*='
    } | Select-Object -First 1)
}
if ($sarvamPresent) {
    Add-Row 'credential' 'SARVAM_API_KEY' 'PASS' 'present; value not displayed' ''
} else {
    Add-Row 'credential' 'SARVAM_API_KEY' 'WARN' 'absent' 'Optional. Only needed for Sarvam Indian-English narration experiments.'
}

$higgsfieldAuthed = $false
if ($higgsfield) {
    $statusText = (& higgsfield account status --json 2>&1 | Out-String)
    if ($LASTEXITCODE -eq 0) {
        try { $null = $statusText | ConvertFrom-Json; $higgsfieldAuthed = $true } catch {}
    }
}
if ($higgsfieldAuthed) {
    Add-Row 'credential' 'higgsfield-login' 'PASS' 'authenticated; account details not displayed' ''
} elseif ($higgsfield) {
    Add-Row 'credential' 'higgsfield-login' 'HUMAN' 'not authenticated' 'Run: higgsfield auth login'
    Add-Human 'Run "higgsfield auth login" yourself in an interactive terminal. An agent must not do this for you.'
} else {
    Add-Row 'credential' 'higgsfield-login' 'WARN' 'CLI absent' 'Install the CLI first, then run: higgsfield auth login'
    Add-Human 'Install the Higgsfield CLI, then run "higgsfield auth login" yourself in an interactive terminal.'
}

# ---------------------------------------------------------------- 5. Project skills and agents
if ($Install) {
    Write-Output 'Synchronizing project skills and agents...'
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot 'tools\sync-script-video-skills.ps1') | Out-Null
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot 'tools\sync-script-video-agents.ps1') | Out-Null
    & powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot 'tools\sync-ramayana-video-skills.ps1') | Out-Null
}

$syncChecks = @(
    @{ Name = 'skills:script-video'; Script = 'tools\sync-script-video-skills.ps1' },
    @{ Name = 'agents:shared';       Script = 'tools\sync-script-video-agents.ps1' },
    @{ Name = 'skills:ramayana';     Script = 'tools\sync-ramayana-video-skills.ps1' }
)
foreach ($item in $syncChecks) {
    $scriptPath = Join-Path $repoRoot $item.Script
    if (-not (Test-Path -LiteralPath $scriptPath)) {
        Add-Row 'parity' $item.Name 'FAIL' "missing $($item.Script)" 'Restore the file from Git.'
        continue
    }
    $output = (& powershell -ExecutionPolicy Bypass -File $scriptPath -Check 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -eq 0) {
        Add-Row 'parity' $item.Name 'PASS' 'Codex and Claude copies match' ''
    } else {
        Add-Row 'parity' $item.Name 'FAIL' 'mirror differs from the canonical copy' "powershell -ExecutionPolicy Bypass -File $($item.Script)"
    }
}

# ---------------------------------------------------------------- 6. User-level host skills
$hostSkillRoots = @{
    'claude' = Join-Path $env:USERPROFILE '.claude\skills'
    'codex'  = Join-Path $env:USERPROFILE '.codex\skills'
}
$requiredHostSkills = @('higgsfield', 'higgsfield-generate', 'higgsfield-soul-id', 'video-use')
$optionalHostSkills = @('hyperframes', 'hyperframes-cli', 'media-use', 'remotion-create', 'remotion-render')
foreach ($hostName in $hostSkillRoots.Keys) {
    $root = $hostSkillRoots[$hostName]
    $missingRequired = @($requiredHostSkills | Where-Object { -not (Test-Path -LiteralPath (Join-Path $root "$_\SKILL.md")) })
    $missingOptional = @($optionalHostSkills | Where-Object { -not (Test-Path -LiteralPath (Join-Path $root "$_\SKILL.md")) })
    if ($missingRequired.Count -eq 0) {
        Add-Row 'host-skill' "${hostName}:required" 'PASS' 'higgsfield, higgsfield-generate, higgsfield-soul-id, video-use present' ''
    } else {
        Add-Row 'host-skill' "${hostName}:required" 'HUMAN' ("missing: " + ($missingRequired -join ', ')) 'Install the upstream skills. See docs/SOP-00-SETUP.md step 5.'
        Add-Human "Install the missing $hostName skills listed in docs/SOP-00-SETUP.md step 5, then restart the agent."
    }
    if ($missingOptional.Count -eq 0) {
        Add-Row 'host-skill' "${hostName}:optional" 'PASS' 'HyperFrames and Remotion skills present' ''
    } else {
        Add-Row 'host-skill' "${hostName}:optional" 'WARN' ("missing: " + ($missingOptional -join ', ')) 'npx hyperframes skills update'
    }
}

# ---------------------------------------------------------------- Report
if ($Json) {
    [pscustomobject]@{
        repoRoot     = $repoRoot
        results      = $results
        humanActions = $humanActions
    } | ConvertTo-Json -Depth 6
} else {
    $results | Format-Table Area, Check, Status, Evidence -AutoSize

    $failed = @($results | Where-Object { $_.Status -eq 'FAIL' })
    $human = @($results | Where-Object { $_.Status -eq 'HUMAN' })
    $warned = @($results | Where-Object { $_.Status -eq 'WARN' })

    if ($failed.Count -gt 0) {
        Write-Output ''
        Write-Output 'MACHINE FIXES REQUIRED'
        foreach ($row in $failed) { Write-Output ("  [{0}] {1}" -f $row.Check, $row.Fix) }
    }
    if ($human.Count -gt 0 -or $humanActions.Count -gt 0) {
        Write-Output ''
        Write-Output 'HUMAN ACTIONS REQUIRED (an agent must not do these for you)'
        foreach ($action in $humanActions) { Write-Output "  - $action" }
    }
    if ($warned.Count -gt 0) {
        Write-Output ''
        Write-Output 'OPTIONAL'
        foreach ($row in $warned) { Write-Output ("  [{0}] {1}" -f $row.Check, $row.Fix) }
    }

    Write-Output ''
    Write-Output ("Summary: {0} pass, {1} fail, {2} human, {3} optional." -f
        @($results | Where-Object { $_.Status -eq 'PASS' }).Count,
        $failed.Count, $human.Count, $warned.Count)

    if ($failed.Count -gt 0) { exit 1 }
    if ($human.Count -gt 0) { exit 2 }
    Write-Output 'Environment is ready. Read docs/SOP-01-STORY-FILM.md or docs/SOP-02-PRODUCT-EXPLAINER.md next.'
}
