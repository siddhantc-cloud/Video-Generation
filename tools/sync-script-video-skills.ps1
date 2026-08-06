param(
    [switch]$Check
)

$ErrorActionPreference = 'Stop'

$workspace = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$sourceRoot = Join-Path $workspace '.codex\skills'
$targetRoot = Join-Path $workspace '.claude\skills'
$skills = @(
    'script-video-setup',
    'script-video-production',
    'script-video-bootstrap',
    'script-video-plan',
    'script-video-continuity',
    'script-video-animatic',
    'script-video-cinema-navigation',
    'script-video-generate',
    'script-video-review',
    'script-video-motion-graphics',
    'script-video-post',
    'script-video-learn'
)

function Get-RelativeFiles([string]$Root) {
    if (-not (Test-Path -LiteralPath $Root)) { return @() }
    return @(Get-ChildItem -LiteralPath $Root -File -Recurse | ForEach-Object {
        $_.FullName.Substring($Root.Length).TrimStart('\').Replace('\', '/')
    } | Sort-Object)
}

function Compare-Skill([string]$Source, [string]$Target) {
    $sourceFiles = @(Get-RelativeFiles $Source)
    $targetFiles = @(Get-RelativeFiles $Target)
    if (($sourceFiles -join "`n") -ne ($targetFiles -join "`n")) { return $false }
    foreach ($relative in $sourceFiles) {
        $sourceFile = Join-Path $Source $relative
        $targetFile = Join-Path $Target $relative
        if ((Get-FileHash -LiteralPath $sourceFile -Algorithm SHA256).Hash -ne
            (Get-FileHash -LiteralPath $targetFile -Algorithm SHA256).Hash) {
            return $false
        }
    }
    return $true
}

foreach ($skill in $skills) {
    $source = Join-Path $sourceRoot $skill
    $target = Join-Path $targetRoot $skill
    if (-not (Test-Path -LiteralPath $source)) {
        throw "Missing canonical skill: $source"
    }

    if ($Check) {
        if (-not (Compare-Skill $source $target)) {
            throw "Skill parity failed: $skill"
        }
        Write-Output "PASS $skill"
        continue
    }

    if (Test-Path -LiteralPath $target) {
        $resolvedTarget = (Resolve-Path -LiteralPath $target).Path
        if (-not $resolvedTarget.StartsWith($targetRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
            throw "Unsafe target: $resolvedTarget"
        }
        Remove-Item -LiteralPath $resolvedTarget -Recurse -Force
    }
    New-Item -ItemType Directory -Path $target -Force | Out-Null
    Copy-Item -Path (Join-Path $source '*') -Destination $target -Recurse -Force
    Write-Output "SYNC $skill"
}
