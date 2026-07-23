param(
    [string]$Output = "audio/music/short-v001-elevenlabs-music-v2.mp3",
    [string]$Status = "edit/music-short-v001-status.json"
)

$ErrorActionPreference = "Stop"
$project = Split-Path -Parent $PSScriptRoot
$outputPath = Join-Path $project $Output
$statusPath = Join-Path $project $Status

if (Test-Path -LiteralPath $outputPath) {
    $existing = Get-Item -LiteralPath $outputPath
    if ($existing.Length -gt 0) {
        [pscustomobject]@{
            state = "already_complete"
            output = $Output.Replace("\", "/")
            bytes = $existing.Length
            completed_at = (Get-Date).ToString("o")
        } | ConvertTo-Json | Set-Content -LiteralPath $statusPath -Encoding UTF8
        exit 0
    }
}

$apiKey = [Environment]::GetEnvironmentVariable("ELEVENLABS_API_KEY", "User")
if ([string]::IsNullOrWhiteSpace($apiKey)) {
    throw "ELEVENLABS_API_KEY is not available in the Windows user environment."
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $outputPath) | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $statusPath) | Out-Null

[pscustomobject]@{
    state = "generating"
    output = $Output.Replace("\", "/")
    started_at = (Get-Date).ToString("o")
} | ConvertTo-Json | Set-Content -LiteralPath $statusPath -Encoding UTF8

$prompt = @"
Instrumental cinematic Indian mythological score for a 52.2-second vertical social film. No vocals
and no lyrics. Begin reverent and spacious with bansuri, tanpura-like drone and restrained low
strings. Build gentle momentum under the squirrel's repeated effort with soft tabla, hand
percussion and a warm string pulse. At the Rama recognition beat around 17.5 seconds, briefly thin
to tender sarangi and breathy flute. From 25.4 seconds, rebuild with patient rhythmic confidence.
At 32.8 seconds, transition cleanly into a modern but organic SIP explanation with subtle plucked
strings and even pulse, never electronic or corporate. From 43.4 seconds, rise to an earned,
hopeful orchestral resolution with low brass, strings and Indian percussion, then leave space for
the spoken end line and finish with one clean warm resolve at 52.2 seconds. Grounded, photoreal,
reverent, emotionally controlled, narration-friendly, no trailer booms, no overpowering drums.
"@

$body = @{
    prompt = $prompt
    music_length_ms = 52200
    model_id = "music_v2"
    force_instrumental = $true
    sign_with_c2pa = $true
} | ConvertTo-Json -Depth 4

$headers = @{
    "xi-api-key" = $apiKey
    "Content-Type" = "application/json"
}

try {
    $response = Invoke-WebRequest `
        -Uri "https://api.elevenlabs.io/v1/music?output_format=mp3_48000_192" `
        -Method Post `
        -Headers $headers `
        -Body $body `
        -OutFile $outputPath `
        -TimeoutSec 600 `
        -UseBasicParsing

    $item = Get-Item -LiteralPath $outputPath
    [pscustomobject]@{
        state = "complete"
        output = $Output.Replace("\", "/")
        bytes = $item.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $outputPath).Hash
        song_id = [string]$response.Headers["song-id"]
        completed_at = (Get-Date).ToString("o")
    } | ConvertTo-Json | Set-Content -LiteralPath $statusPath -Encoding UTF8
}
catch {
    [pscustomobject]@{
        state = "failed"
        output = $Output.Replace("\", "/")
        error = $_.Exception.Message
        failed_at = (Get-Date).ToString("o")
    } | ConvertTo-Json | Set-Content -LiteralPath $statusPath -Encoding UTF8
    throw
}
