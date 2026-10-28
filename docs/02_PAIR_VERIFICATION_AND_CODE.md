# 02 — Dataset Inventory and Noisy/GT Pairing Verification

**Source:** Original Windows PowerShell screenshot from the maintainer's October 21, 2026 investigation.

## What the original check actually did

The supplied terminal screenshot shows `Get-ChildItem` used to list scene folders and noisy/GT PNGs, `Test-Path` to test whether a GT counterpart exists for a noisy filename, and a final summary printed by `Write-Host`.

**Recorded output:** 160 scene folders · 320 noisy images · 320 GT images · **320 filename-matched pairs** · 640 classified PNGs.

## Reusable version of the command

The script [`scripts/verify_sidd_inventory.ps1`](../scripts/verify_sidd_inventory.ps1) is a **portable adaptation compiled on October 28** from those original commands. It includes a check in both directions to detect GT-only records.

Example usage in PowerShell from your repository:

```powershell
& .\scripts\verify_sidd_inventory.ps1 -DatasetRoot "D:\Datasets\SIDD_Medium_Srgb\train"
```

Substitute the *actual* extracted dataset directory. The provided path is illustrative; do not copy the example blindly. Run the command only in a PowerShell session configured to permit scripts according to your system policy.

## Limits of the result

A successful filename check does not prove that every image decodes correctly, contains RGB pixels, or is pixel-aligned to its reference. Those tests belong in the new Colab verification stage. The source archive itself has not been uploaded here.
