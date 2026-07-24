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

$qwenPython = Join-Path $repoRoot 'Ramayana-ZebpaySIP\.venv-qwen3-tts\Scripts\python.exe'
$qwenCheck = ''
$qwenPassed = $false
if (Test-Path -LiteralPath $qwenPython) {
    $qwenCheck = (& $qwenPython -c "import importlib.metadata, torch; assert torch.cuda.is_available(); x=torch.ones(1, device='cuda'); print('qwen-tts=' + importlib.metadata.version('qwen-tts') + '; torch=' + torch.__version__ + '; gpu=' + torch.cuda.get_device_name(0) + '; tensor=' + str(x.item()))" 2>&1 | Out-String).Trim()
    $qwenPassed = $LASTEXITCODE -eq 0
} else {
    $qwenCheck = 'project environment not found'
}
Add-Result 'local-tts:qwen3-cuda' $qwenPassed $qwenCheck

$qwenGenerator = Join-Path $repoRoot 'Ramayana-ZebpaySIP\tools\generate_qwen3_tts.py'
$qwenRecipe = Join-Path $repoRoot '.agent-harness\recipes\local-qwen3-tts-narration.md'
Add-Result 'local-tts:generator' (Test-Path -LiteralPath $qwenGenerator) $qwenGenerator
Add-Result 'local-tts:recipe' (Test-Path -LiteralPath $qwenRecipe) $qwenRecipe

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
