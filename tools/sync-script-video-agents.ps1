param(
    [switch]$Check
)

$ErrorActionPreference = 'Stop'

$workspace = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$sourceRoot = Join-Path $workspace 'video-production-system\agents'
$targetRoot = Join-Path $workspace '.claude\agents'
$agents = @(
    'script-rewriter.md',
    'assistant-director.md',
    'scene-expectations.md',
    'prompt-reviewer.md',
    'video-editor.md',
    'video-reviewer.md'
)

foreach ($agent in $agents) {
    $source = Join-Path $sourceRoot $agent
    $target = Join-Path $targetRoot $agent
    if (-not (Test-Path -LiteralPath $source)) {
        throw "Missing canonical agent: $source"
    }

    if ($Check) {
        if (-not (Test-Path -LiteralPath $target)) {
            throw "Missing Claude agent mirror: $target"
        }
        if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash -ne
            (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash) {
            throw "Agent parity failed: $agent"
        }
        Write-Output "PASS $agent"
        continue
    }

    Copy-Item -LiteralPath $source -Destination $target -Force
    Write-Output "SYNC $agent"
}
