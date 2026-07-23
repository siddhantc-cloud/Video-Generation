param(
    [switch]$Check
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$RepoRoot = Split-Path -Parent $PSScriptRoot
$CodexRoot = Join-Path $RepoRoot '.codex\skills'
$ClaudeRoot = Join-Path $RepoRoot '.claude\skills'
$SkillNames = @(
    'ramayana-cinema-navigation',
    'ramayana-video-plan',
    'ramayana-elements-continuity',
    'ramayana-shot-generate',
    'ramayana-video-review',
    'ramayana-video-post',
    'ramayana-learn'
)

function Get-RelativeFileMap {
    param([Parameter(Mandatory)][string]$Root)

    $map = @{}
    if (-not (Test-Path -LiteralPath $Root)) {
        return $map
    }

    foreach ($file in Get-ChildItem -LiteralPath $Root -Recurse -File) {
        $relative = $file.FullName.Substring($Root.Length).TrimStart('\', '/')
        $map[$relative] = $file.FullName
    }
    return $map
}

function Test-SkillParity {
    $issues = New-Object System.Collections.Generic.List[string]

    foreach ($name in $SkillNames) {
        $source = Join-Path $CodexRoot $name
        $target = Join-Path $ClaudeRoot $name
        $sourceFiles = Get-RelativeFileMap -Root $source
        $targetFiles = Get-RelativeFileMap -Root $target

        if ($sourceFiles.Count -eq 0) {
            $issues.Add("Missing canonical skill: $source")
            continue
        }
        if ($targetFiles.Count -eq 0) {
            $issues.Add("Missing Claude mirror: $target")
            continue
        }

        foreach ($relative in $sourceFiles.Keys) {
            if (-not $targetFiles.ContainsKey($relative)) {
                $issues.Add("Missing mirror file: $name/$relative")
                continue
            }
            $sourceHash = (Get-FileHash -LiteralPath $sourceFiles[$relative] -Algorithm SHA256).Hash
            $targetHash = (Get-FileHash -LiteralPath $targetFiles[$relative] -Algorithm SHA256).Hash
            if ($sourceHash -ne $targetHash) {
                $issues.Add("Content drift: $name/$relative")
            }
        }

        foreach ($relative in $targetFiles.Keys) {
            if (-not $sourceFiles.ContainsKey($relative)) {
                $issues.Add("Mirror-only file: $name/$relative")
            }
        }
    }

    if ($issues.Count -gt 0) {
        $issues | ForEach-Object { Write-Host "ERROR: $_" }
        return $false
    }

    Write-Host "Ramayana video skills are byte-equivalent across Codex and Claude ($($SkillNames.Count) skills)."
    return $true
}

if ($Check) {
    if (-not (Test-SkillParity)) { exit 1 }
    exit 0
}

foreach ($name in $SkillNames) {
    $source = Join-Path $CodexRoot $name
    $target = Join-Path $ClaudeRoot $name
    if (-not (Test-Path -LiteralPath $source)) {
        throw "Canonical skill does not exist: $source"
    }

    New-Item -ItemType Directory -Path $target -Force | Out-Null
    foreach ($file in Get-ChildItem -LiteralPath $source -Recurse -File) {
        $relative = $file.FullName.Substring($source.Length).TrimStart('\', '/')
        $destination = Join-Path $target $relative
        New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force | Out-Null
        Copy-Item -LiteralPath $file.FullName -Destination $destination -Force
    }
}

if (-not (Test-SkillParity)) { exit 1 }
