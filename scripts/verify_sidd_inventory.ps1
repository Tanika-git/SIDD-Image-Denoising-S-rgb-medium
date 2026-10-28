# Reusable adaptation prepared 2026-10-28 from the maintainer's
# PowerShell commands recorded in 2026-10-21 screenshots.
# This version has not yet been executed on the local dataset.
param(
    [Parameter(Mandatory=$true)][string]$DatasetRoot
)
if (-not (Test-Path -LiteralPath $DatasetRoot -PathType Container)) {
    throw "Dataset directory not found: $DatasetRoot"
}
$folders = @(Get-ChildItem -LiteralPath $DatasetRoot -Directory)
$noisy = @(Get-ChildItem -LiteralPath $DatasetRoot -Recurse -File -Filter '*.PNG' |
           Where-Object { $_.Name -match '_NOISY_SRGB_' })
$clean = @(Get-ChildItem -LiteralPath $DatasetRoot -Recurse -File -Filter '*.PNG' |
           Where-Object { $_.Name -match '_GT_SRGB_' })
$matched = @($noisy | Where-Object {
    $candidate = $_.FullName -replace '_NOISY_SRGB_', '_GT_SRGB_'
    Test-Path -LiteralPath $candidate -PathType Leaf
})
$cleanOnly = @($clean | Where-Object {
    $candidate = $_.FullName -replace '_GT_SRGB_', '_NOISY_SRGB_'
    -not (Test-Path -LiteralPath $candidate -PathType Leaf)
})
Write-Host '=== SIDD-Medium file inventory ==='
Write-Host "Folders: $($folders.Count)"
Write-Host "Noisy PNGs: $($noisy.Count)"
Write-Host "GT PNGs: $($clean.Count)"
Write-Host "Filename-matched pairs: $($matched.Count)"
Write-Host "Unpaired GT files: $($cleanOnly.Count)"
Write-Host "Total paired-class PNGs: $($noisy.Count + $clean.Count)"
if ($folders.Count -ne 160 -or $noisy.Count -ne 320 -or $clean.Count -ne 320 -or
    $matched.Count -ne 320 -or $cleanOnly.Count -ne 0) {
    Write-Warning 'Inventory does not match the expected 160 folders / 320 pairs; investigate before training.'
} else {
    Write-Host 'Metadata/path inventory matches the expected SIDD-Medium layout.'
}
# Filename matches do NOT guarantee the image file can be decoded or pixel alignment.
