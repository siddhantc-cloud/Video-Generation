param(
    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Output,

    [string]$Report
)

$ErrorActionPreference = "Stop"

$sourcePath = [System.IO.Path]::GetFullPath($Source)
$outputPath = [System.IO.Path]::GetFullPath($Output)
if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
    throw "Source render not found: $sourcePath"
}

$outputDirectory = Split-Path -Parent $outputPath
New-Item -ItemType Directory -Force -Path $outputDirectory | Out-Null

& ffmpeg `
    -hide_banner `
    -loglevel error `
    -y `
    -i $sourcePath `
    -map 0:v:0 `
    -map "0:a:0?" `
    -vf "fps=30,scale=1080:1920:flags=lanczos,format=yuv420p" `
    -c:v libx264 `
    -preset slow `
    -b:v 2400k `
    -maxrate 3000k `
    -bufsize 6000k `
    -g 60 `
    -movflags +faststart `
    -af "loudnorm=I=-16:TP=-1.5:LRA=11" `
    -c:a aac `
    -ar 48000 `
    -b:a 160k `
    $outputPath
if ($LASTEXITCODE -ne 0) {
    throw "FFmpeg review encode failed with exit code $LASTEXITCODE"
}

$probeJson = & ffprobe `
    -v error `
    -show_entries "format=duration,size,bit_rate:stream=index,codec_name,codec_type,width,height,r_frame_rate,pix_fmt,sample_rate,channels" `
    -of json `
    $outputPath
if ($LASTEXITCODE -ne 0) {
    throw "FFprobe failed with exit code $LASTEXITCODE"
}

$probe = $probeJson | ConvertFrom-Json
$hash = (Get-FileHash -LiteralPath $outputPath -Algorithm SHA256).Hash
$record = [ordered]@{
    generated_at = [DateTime]::UtcNow.ToString("o")
    status = "review-cut-not-promoted"
    source = $sourcePath
    output = $outputPath
    sha256 = $hash
    probe = $probe
}

if (-not $Report) {
    $Report = [System.IO.Path]::ChangeExtension($outputPath, ".json")
}
$reportPath = [System.IO.Path]::GetFullPath($Report)
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $reportPath) | Out-Null
$record | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $reportPath -Encoding utf8

Write-Output "Review cut: $outputPath"
Write-Output "SHA-256: $hash"
Write-Output "Report: $reportPath"
