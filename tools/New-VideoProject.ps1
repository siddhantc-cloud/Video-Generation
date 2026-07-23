[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ProjectName,

    [string]$ScriptPath,

    [string]$WorkspaceRoot,

    [ValidateSet('9:16', '16:9', '1:1')]
    [string]$AspectRatio = '9:16',

    [ValidateSet(24, 30, 60)]
    [int]$Fps = 30,

    [ValidateSet('480x854', '854x480', '480x480', '720x1280', '1280x720', '720x720', '1080x1920', '1920x1080', '1080x1080')]
    [string]$Resolution = '1080x1920'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if ([string]::IsNullOrWhiteSpace($WorkspaceRoot)) {
    $WorkspaceRoot = Split-Path -Parent $PSScriptRoot
}

if ($ProjectName -match '[\\/:*?"<>|]') {
    throw 'ProjectName must be a folder name, not a path.'
}

$resolvedWorkspace = [System.IO.Path]::GetFullPath($WorkspaceRoot)
$templateRoot = Join-Path $resolvedWorkspace 'video-production-system\templates'
$target = [System.IO.Path]::GetFullPath((Join-Path $resolvedWorkspace $ProjectName))

if (-not $target.StartsWith($resolvedWorkspace + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw 'Target project escaped the workspace root.'
}
if (-not (Test-Path -LiteralPath $templateRoot)) {
    throw "Missing project template: $templateRoot"
}
if (Test-Path -LiteralPath $target) {
    throw "Target project already exists: $target"
}

$directories = @(
    'assets\brand',
    'assets\characters',
    'assets\locations',
    'assets\props',
    'assets\references',
    'audio\narration',
    'audio\music',
    'audio\sfx',
    'deliverables\review-cuts',
    'deliverables\final',
    'edit\animations',
    'edit\captions',
    'edit\timelines',
    'edit\verify',
    'footage\raw',
    'footage\selects',
    'keyframes\look-lock',
    'keyframes\shots',
    'project',
    'review\criteria',
    'review\takes',
    'scripts',
    'storyboard',
    'tools'
)

if ($PSCmdlet.ShouldProcess($target, 'Create script-to-video production workspace')) {
    New-Item -ItemType Directory -Path $target | Out-Null
    foreach ($relative in $directories) {
        New-Item -ItemType Directory -Force -Path (Join-Path $target $relative) | Out-Null
    }

    foreach ($file in Get-ChildItem -LiteralPath $templateRoot -Recurse -File) {
        $relative = $file.FullName.Substring($templateRoot.Length).TrimStart('\', '/')
        $destination = Join-Path $target $relative
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
        Copy-Item -LiteralPath $file.FullName -Destination $destination
    }

    if ($ScriptPath) {
        $resolvedScript = (Resolve-Path -LiteralPath $ScriptPath).Path
        $extension = [System.IO.Path]::GetExtension($resolvedScript)
        if ([string]::IsNullOrWhiteSpace($extension)) {
            $extension = '.txt'
        }
        Copy-Item -LiteralPath $resolvedScript -Destination (Join-Path $target "scripts\source-script-original$extension")
        if ($extension -in @('.md', '.txt')) {
            Copy-Item -LiteralPath $resolvedScript -Destination (Join-Path $target 'scripts\source-script.md') -Force
        }
    }

    $settings = [ordered]@{
        project_name = $ProjectName
        aspect_ratio = $AspectRatio
        fps = $Fps
        resolution = $Resolution
        created_at = (Get-Date).ToString('o')
        production_system = 'video-production-system/PRODUCTION_SYSTEM.md'
    }
    $settings | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $target 'project\project-settings.json') -Encoding UTF8
}

Write-Host "Created video production workspace: $target"
