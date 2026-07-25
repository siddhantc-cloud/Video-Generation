[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$codexRoot = 'C:\Users\SE\.codex\skills'
$claudeRoot = 'C:\Users\SE\.claude\skills'
$skillNames = @(
    'higgsfield',
    'higgsfield-generate',
    'higgsfield-soul-id',
    'video-use',
    'remotion-best-practices',
    'remotion-create',
    'remotion-render',
    'remotion-captions'
)
$results = [System.Collections.Generic.List[object]]::new()

function Add-Result {
    param(
        [string]$Check,
        [bool]$Passed,
        [string]$Evidence
    )
    $script:results.Add([pscustomobject]@{
        Check = $Check
        Passed = $Passed
        Evidence = $Evidence
    })
}

function Get-DirectoryManifest {
    param([string]$Root)
    if (-not (Test-Path -LiteralPath $Root)) { return @() }
    return @(
        Get-ChildItem -LiteralPath $Root -Recurse -File |
            Where-Object {
                $_.Name -ne '.env' -and
                $_.Extension -ne '.pyc' -and
                $_.FullName -notmatch '[\\/]__pycache__[\\/]'
            } |
            Sort-Object FullName |
            ForEach-Object {
                $relative = $_.FullName.Substring($Root.Length).TrimStart('\') -replace '\\', '/'
                "$relative`t$((Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash)"
            }
    )
}

foreach ($skill in $skillNames) {
    $codexPath = Join-Path $codexRoot $skill
    $claudePath = Join-Path $claudeRoot $skill
    $codexSkill = Join-Path $codexPath 'SKILL.md'
    $claudeSkill = Join-Path $claudePath 'SKILL.md'
    $present = (Test-Path -LiteralPath $codexSkill) -and (Test-Path -LiteralPath $claudeSkill)
    Add-Result "skill:$skill" $present 'SKILL.md present on Codex and Claude'

    if ($present) {
        $difference = Compare-Object (Get-DirectoryManifest $codexPath) (Get-DirectoryManifest $claudePath)
        Add-Result "parity:$skill" ($null -eq $difference) 'Codex and Claude file manifests match'
    }
}

foreach ($command in @('higgsfield', 'ffmpeg', 'ffprobe', 'python', 'node', 'npm')) {
    $resolved = Get-Command $command -ErrorAction SilentlyContinue
    Add-Result "command:$command" ($null -ne $resolved) $(if ($resolved) { $resolved.Source } else { 'not found' })
}

$higgsfieldStatusText = (& higgsfield account status --json 2>&1 | Out-String)
$higgsfieldStatusExit = $LASTEXITCODE
$higgsfieldStatusStructured = $false
if ($higgsfieldStatusExit -eq 0) {
    try {
        $null = $higgsfieldStatusText | ConvertFrom-Json
        $higgsfieldStatusStructured = $true
    } catch {}
}
Add-Result 'higgsfield:authenticated-workspace' (($higgsfieldStatusExit -eq 0) -and $higgsfieldStatusStructured) 'Authenticated account status returned structured data; account details not displayed'

$ytDlp = Get-Command 'yt-dlp' -ErrorAction SilentlyContinue
if (-not $ytDlp) {
    $fallback = Join-Path $env:USERPROFILE '.local\bin\yt-dlp.exe'
    if (Test-Path -LiteralPath $fallback) { $ytDlp = Get-Item -LiteralPath $fallback }
}
$ytDlpEvidence = if (-not $ytDlp) {
    'not found'
} elseif ($ytDlp.PSObject.Properties.Name -contains 'Source' -and $ytDlp.Source) {
    $ytDlp.Source
} else {
    $ytDlp.FullName
}
Add-Result 'command:yt-dlp' ($null -ne $ytDlp) $ytDlpEvidence

$importCheck = & python -c 'import librosa, matplotlib, PIL, numpy, requests' 2>&1
Add-Result 'video-use:python-dependencies' ($LASTEXITCODE -eq 0) $(if ($LASTEXITCODE -eq 0) { 'imports succeeded' } else { [string]$importCheck })

$qwenEnvironment = Join-Path $repoRoot 'Ramayana-ZebpaySIP\.venv-qwen3-tts'
$qwenModelCache = Join-Path $repoRoot '_cache\huggingface'
$qwenPackageCache = Join-Path $repoRoot '_cache\uv'
Add-Result 'local-tts:qwen3-runtime-removed' (-not (Test-Path -LiteralPath $qwenEnvironment)) 'Owner removed the project-local Qwen environment on 2026-07-25'
Add-Result 'local-tts:qwen3-caches-removed' ((-not (Test-Path -LiteralPath $qwenModelCache)) -and (-not (Test-Path -LiteralPath $qwenPackageCache))) 'Dedicated Qwen Hugging Face and UV caches are absent'

$qwenGenerator = Join-Path $repoRoot 'Ramayana-ZebpaySIP\tools\generate_qwen3_tts.py'
$qwenRecipe = Join-Path $repoRoot '.agent-harness\recipes\local-qwen3-tts-narration.md'
Add-Result 'historical-qwen:generator' (Test-Path -LiteralPath $qwenGenerator) $qwenGenerator
Add-Result 'historical-qwen:recipe' (Test-Path -LiteralPath $qwenRecipe) $qwenRecipe

$sarvamGenerator = Join-Path $repoRoot 'Ramayana-ZebpaySIP\tools\generate_sarvam_tts.py'
$sarvamRecipe = Join-Path $repoRoot '.agent-harness\recipes\sarvam-bulbul-v3-narration.md'
$sarvamCompile = ''
$sarvamGeneratorPassed = Test-Path -LiteralPath $sarvamGenerator
if ($sarvamGeneratorPassed) {
    $sarvamCompile = (& python -m py_compile $sarvamGenerator 2>&1 | Out-String).Trim()
    $sarvamGeneratorPassed = $LASTEXITCODE -eq 0
}
Add-Result 'hosted-tts:sarvam-generator' $sarvamGeneratorPassed $(if ($sarvamGeneratorPassed) { $sarvamGenerator } else { $sarvamCompile })
Add-Result 'hosted-tts:sarvam-recipe' (Test-Path -LiteralPath $sarvamRecipe) $sarvamRecipe

$dotenvPath = Join-Path $repoRoot '.env'
$sarvamCredentialPresent = $false
$dotenvIgnored = $false
if (Test-Path -LiteralPath $dotenvPath) {
    $sarvamCredentialPresent = [bool](Get-Content -LiteralPath $dotenvPath | Where-Object {
        $_ -match '^\s*(?:export\s+)?SARVAM_API_KEY\s*='
    } | Select-Object -First 1)
    & git -C $repoRoot check-ignore -q -- '.env'
    $dotenvIgnored = $LASTEXITCODE -eq 0
}
Add-Result 'credential:sarvam-ignored-env' ($sarvamCredentialPresent -and $dotenvIgnored) $(if ($sarvamCredentialPresent -and $dotenvIgnored) { 'SARVAM_API_KEY entry present in ignored .env; value not displayed' } else { 'Missing key entry or .env is not ignored' })

$mcpPath = Join-Path $repoRoot '.mcp.json'
$mcpSafe = $false
if (Test-Path -LiteralPath $mcpPath) {
    $mcpRaw = Get-Content -LiteralPath $mcpPath -Raw
    $mcpSafe = -not [bool]($mcpRaw -match '(?i)api[_-]?key\s*["'']?\s*[:=]\s*["'']?[A-Za-z0-9_-]{16,}')
}
Add-Result 'credential:mcp-config' $mcpSafe 'No literal API-key-shaped value found in .mcp.json'

$elevenLabsPresent = -not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable('ELEVENLABS_API_KEY', 'User'))
Add-Result 'credential:elevenlabs-user-env' $elevenLabsPresent 'Windows user environment variable is present; value not displayed'

$timelinePath = Join-Path $repoRoot '.agent-harness\evidence\video-environment\video-use-timeline.png'
Add-Result 'smoke-test:video-use-timeline' (Test-Path -LiteralPath $timelinePath) $timelinePath

$results | Format-Table -AutoSize
$failed = @($results | Where-Object { -not $_.Passed })
if ($failed.Count -gt 0) {
    Write-Error "$($failed.Count) video-environment check(s) failed."
    exit 1
}

Write-Output "All $($results.Count) video-environment checks passed."
