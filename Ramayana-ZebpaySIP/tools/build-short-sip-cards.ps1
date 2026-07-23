param(
    [string]$ProjectRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$sourcePath = Join-Path $ProjectRoot 'keyframes\S6_calm.png'
$outputDir = Join-Path $ProjectRoot 'edit\graphics\sip-animatic'
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$cards = @(
    @{
        File = 'S6-01-perfect-moment.png'
        Kicker = 'THE SIP PARALLEL'
        Line1 = "DON'T WAIT FOR"
        Line2 = 'THE PERFECT MOMENT'
        Detail = 'Markets move. Consistency is the part you control.'
    },
    @{
        File = 'S6-02-regularly.png'
        Kicker = 'A SIMPLE RHYTHM'
        Line1 = 'THE SAME AMOUNT'
        Line2 = 'REGULARLY'
        Detail = 'A disciplined contribution, repeated over time.'
    },
    @{
        File = 'S6-03-ups-downs.png'
        Kicker = 'KEEP SHOWING UP'
        Line1 = 'THROUGH THE UPS'
        Line2 = 'AND THE DOWNS'
        Detail = 'Small steps. Repeated consistently.'
    }
)

$source = [System.Drawing.Image]::FromFile($sourcePath)
try {
    foreach ($card in $cards) {
        $bitmap = New-Object System.Drawing.Bitmap 1080, 1920
        $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
        try {
            $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
            $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
            $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

            $scale = [Math]::Max(1080.0 / $source.Width, 1920.0 / $source.Height)
            $drawWidth = [int][Math]::Ceiling($source.Width * $scale)
            $drawHeight = [int][Math]::Ceiling($source.Height * $scale)
            $drawX = [int][Math]::Floor((1080 - $drawWidth) / 2.0)
            $drawY = [int][Math]::Floor((1920 - $drawHeight) / 2.0)
            $graphics.DrawImage($source, $drawX, $drawY, $drawWidth, $drawHeight)

            $wash = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(174, 8, 20, 48))
            $graphics.FillRectangle($wash, 0, 0, 1080, 1920)
            $wash.Dispose()

            $accent = [System.Drawing.Color]::FromArgb(255, 47, 111, 246)
            $white = [System.Drawing.Color]::FromArgb(255, 250, 252, 255)
            $muted = [System.Drawing.Color]::FromArgb(255, 199, 213, 236)

            $accentBrush = New-Object System.Drawing.SolidBrush $accent
            $whiteBrush = New-Object System.Drawing.SolidBrush $white
            $mutedBrush = New-Object System.Drawing.SolidBrush $muted
            $kickerFont = New-Object System.Drawing.Font 'Segoe UI Semibold', 30, ([System.Drawing.FontStyle]::Bold)
            $headlineFont = New-Object System.Drawing.Font 'Segoe UI', 72, ([System.Drawing.FontStyle]::Bold)
            $detailFont = New-Object System.Drawing.Font 'Segoe UI', 31, ([System.Drawing.FontStyle]::Regular)
            $sipFont = New-Object System.Drawing.Font 'Segoe UI', 32, ([System.Drawing.FontStyle]::Bold)

            $center = New-Object System.Drawing.StringFormat
            $center.Alignment = [System.Drawing.StringAlignment]::Center
            $center.LineAlignment = [System.Drawing.StringAlignment]::Center

            $graphics.FillRectangle($accentBrush, 430, 360, 220, 8)
            $graphics.DrawString($card.Kicker, $kickerFont, $mutedBrush, (New-Object System.Drawing.RectangleF 90, 400, 900, 70), $center)
            $graphics.DrawString($card.Line1, $headlineFont, $whiteBrush, (New-Object System.Drawing.RectangleF 65, 650, 950, 120), $center)
            $graphics.DrawString($card.Line2, $headlineFont, $whiteBrush, (New-Object System.Drawing.RectangleF 65, 780, 950, 120), $center)
            $graphics.FillRectangle($accentBrush, 155, 965, 770, 3)
            $graphics.DrawString($card.Detail, $detailFont, $mutedBrush, (New-Object System.Drawing.RectangleF 120, 1020, 840, 170), $center)

            $graphics.FillEllipse($accentBrush, 430, 1400, 220, 74)
            $graphics.DrawString('SIP', $sipFont, $whiteBrush, (New-Object System.Drawing.RectangleF 430, 1398, 220, 74), $center)

            $destination = Join-Path $outputDir $card.File
            $bitmap.Save($destination, [System.Drawing.Imaging.ImageFormat]::Png)

            $center.Dispose()
            $sipFont.Dispose()
            $detailFont.Dispose()
            $headlineFont.Dispose()
            $kickerFont.Dispose()
            $mutedBrush.Dispose()
            $whiteBrush.Dispose()
            $accentBrush.Dispose()
        }
        finally {
            $graphics.Dispose()
            $bitmap.Dispose()
        }
    }
}
finally {
    $source.Dispose()
}

$endCardDir = Join-Path $ProjectRoot 'edit\graphics\end-card-short'
New-Item -ItemType Directory -Force -Path $endCardDir | Out-Null
$logoPath = Join-Path $ProjectRoot 'assets\brand\zebpay_logo.png'
$logo = [System.Drawing.Image]::FromFile($logoPath)
$endBitmap = New-Object System.Drawing.Bitmap 1080, 1920
$endGraphics = [System.Drawing.Graphics]::FromImage($endBitmap)
try {
    $endGraphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $endGraphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $endGraphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $endGraphics.Clear([System.Drawing.Color]::FromArgb(255, 6, 18, 48))

    $blue = [System.Drawing.Color]::FromArgb(255, 47, 111, 246)
    $white = [System.Drawing.Color]::FromArgb(255, 250, 252, 255)
    $muted = [System.Drawing.Color]::FromArgb(255, 190, 207, 234)
    $blueBrush = New-Object System.Drawing.SolidBrush $blue
    $whiteBrush = New-Object System.Drawing.SolidBrush $white
    $mutedBrush = New-Object System.Drawing.SolidBrush $muted
    $glowBrush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(36, 47, 111, 246))
    $brandFont = New-Object System.Drawing.Font 'Segoe UI', 68, ([System.Drawing.FontStyle]::Bold)
    $ctaFont = New-Object System.Drawing.Font 'Segoe UI Semibold', 42, ([System.Drawing.FontStyle]::Bold)
    $smallFont = New-Object System.Drawing.Font 'Segoe UI', 28, ([System.Drawing.FontStyle]::Regular)
    $center = New-Object System.Drawing.StringFormat
    $center.Alignment = [System.Drawing.StringAlignment]::Center
    $center.LineAlignment = [System.Drawing.StringAlignment]::Center

    $endGraphics.FillEllipse($glowBrush, 225, 410, 630, 630)
    $endGraphics.DrawImage($logo, 390, 570, 300, 300)
    $endGraphics.DrawString('ZebPay', $brandFont, $whiteBrush, (New-Object System.Drawing.RectangleF 90, 940, 900, 120), $center)
    $endGraphics.FillRectangle($blueBrush, 350, 1090, 380, 6)
    $endGraphics.DrawString('START YOUR SIP', $ctaFont, $whiteBrush, (New-Object System.Drawing.RectangleF 90, 1150, 900, 100), $center)
    $endGraphics.DrawString('Small steps. Repeated consistently.', $smallFont, $mutedBrush, (New-Object System.Drawing.RectangleF 120, 1270, 840, 100), $center)

    $endPath = Join-Path $endCardDir 'end-card-clean.png'
    $endBitmap.Save($endPath, [System.Drawing.Imaging.ImageFormat]::Png)

    $center.Dispose()
    $smallFont.Dispose()
    $ctaFont.Dispose()
    $brandFont.Dispose()
    $glowBrush.Dispose()
    $mutedBrush.Dispose()
    $whiteBrush.Dispose()
    $blueBrush.Dispose()
}
finally {
    $endGraphics.Dispose()
    $endBitmap.Dispose()
    $logo.Dispose()
}

Get-ChildItem -LiteralPath $outputDir -Filter 'S6-*.png' |
    Select-Object Name, Length, LastWriteTime
Get-ChildItem -LiteralPath $endCardDir -Filter '*.png' |
    Select-Object Name, Length, LastWriteTime
