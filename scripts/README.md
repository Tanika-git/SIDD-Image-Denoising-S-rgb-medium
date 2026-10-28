# Original inspection code and reproducibility utilities

- `check_sidd_pixels.py` — **original source as uploaded by @Tanika-git**, recorded with the October 21 local investigation. It measures example RGB shape, means, percentiles and a rough crop shift. This script references a user desktop folder relative to `Path.home()`, so its root must be updated for other machines or Colab. **Its output is not a trained-model score.**
- `verify_sidd_inventory.ps1` — a **portable, assistant-assisted adaptation compiled October 28** from the user's original PowerShell commands visible in a dated screenshot. It includes reverse GT-to-noisy matching. Not yet rerun on the full dataset in this package build.

The uploaded `check_sidd_pixels_0104.py` was byte-identical to `check_sidd_pixels.py`; both originals are retained in the private evidence package, while one exact version is published here.

Unrelated exploratory download utilities are kept in the private research archive, not the public SIDD-Medium pipeline.
