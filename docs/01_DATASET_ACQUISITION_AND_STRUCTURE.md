# 01 — SIDD-Medium sRGB: Dataset Selection and Acquisition

**Documented investigator:** @Tanika-git · **Local artifacts dated:** October 21, 2026 · **Documentation compiled:** October 28, 2026.

## Why SIDD-Medium sRGB

The project investigates supervised real-world smartphone denoising. The maintainer selected SIDD-Medium sRGB after considering its use in denoising research and its paired noisy/clean training targets. The original SIDD dataset is a scientific benchmark, not a dataset produced by this project.

**Original source:** [SIDD dataset](https://abdokamel.github.io/sidd/index.html) / [CVPR 2018 publication](https://openaccess.thecvf.com/content_cvpr_2018/html/Abdelhamed_A_High-Quality_Denoising_CVPR_2018_paper.html).

## Existing local archive and inspection

- Local research screenshot shows a `train` compressed archive and an extracted scene-folder tree.
- The maintainer reported a roughly **12 GB** archive and an acquisition that took at least about an hour, with significant free-disk requirements. The exact original archive checksum and byte size have not been supplied here.
- The original directory listing and metadata/ranking records cover **160 scene-instance directories**.
- In each such directory there are expected to be two `NOISY_SRGB` captures (`_010`, `_011`) and two corresponding `GT_SRGB` captures of the same indices.
- The relative names `NOISY_SRGB` and `GT_SRGB` identify the input and reference role of each image. They are files in the **same** scene-instance folder, not separate pools of 160 directories each.

## Representative scene-folder name

`0104_005_S6_03200_01600_4400_L`

| Token | Interpretation |
|---|---|
| `0104` | Scene-instance identifier |
| `005` | Physical scene ID (can group multiple instances) |
| `S6` | Camera code |
| `03200` | ISO 3200 |
| `01600` | Exposure/shutter denominator: approximately 1/1600 second |
| `4400` | Color temperature in kelvin |
| `L` | Low-light category |

A scene-instance folder contains names such as `0104_NOISY_SRGB_010.PNG` and `0104_GT_SRGB_010.PNG`. A second matched pair uses `_011`.

## Verification boundaries

The PowerShell count and 320-row CSV support an internally consistent inventory. **Full pixel integrity, RGB decoding, matching sizes for all pairs and leakage-safe splits must be verified when the actual archive is available in Colab.** There is no completed model training result in the supplied material.
