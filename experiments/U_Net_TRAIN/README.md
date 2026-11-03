# U-Net training and evaluation evidence — SIDD-Medium sRGB

**Experiment:** `sidd_unet_seed42_v1` · **Seed:** 42 · **Architecture:** U-Net · **Run:** 20,000 reported successful optimizer updates (7 AMP-skipped attempts).  
**Recorded source revision:** `89c18654b5e034aa7c93dc050fbf6ec15dde9050` (retained for experiment reproducibility).  
**Hardware:** Kaggle, single Tesla T4 for this U-Net run; final held-out inference was separately performed on CPU from the saved checkpoint.

## Experiment contribution

**U-Net training experiment, modified workflow and recorded results:** **[@Tanika-git](https://github.com/Tanika-git)** (Kaggle experiment `sidd_unet_seed42_v1`). This experiment record documents the configuration/adaptation of the training workflow, execution through the 20,000-step milestone, checkpoint preservation, training/validation measurements, and held-out evaluation evidence. Git commits and privately retained Kaggle logs/checkpoints provide dated evidence of the work.

**Research context:** U-Net is an established architecture; SIDD-Medium sRGB is a published dataset. This record establishes work on this training/evaluation experiment, rather than a claim to have invented either. See [`CONTRIBUTIONS_AND_PROVENANCE.md`](CONTRIBUTIONS_AND_PROVENANCE.md).

## Results (different splits; do not mix them)

| Dataset and purpose | PSNR (dB) | SSIM | Status |
|---|---:|---:|---|
| **Internal validation**, 20,000 steps | **36.5328** | **0.900644** | Logged during training |
| **Internal held-out test**, 20,000-step checkpoint | **41.2316** | **0.952857** | Independently evaluated after training on 60 frozen 256 x 256 test crops |

**NOT the official SIDD benchmark.** These scores are not directly comparable to results measured on another scene split, dataset, crop selection, pre/postprocessing pipeline, or metric definition. In particular, do **not** claim superiority over another U-Net or NAFNet score based only on these numbers.

The test data comes from **one held-out physical-scene group**, and the difference between validation and test scores likely reflects the different image content/noise difficulty; this is a plausible interpretation, not a proven cause. The exact per-image source filenames were not independently checked against `test_crop_manifest.json` after export; the checkpoint's split-protocol digest matched the experiment configuration.

## Experiment setup

- SIDD-Medium sRGB: 320 image pairs, split into 220 training, 70 validation, 30 test pairs; scene-disjoint splitting as recorded in `run_info.json`.
- Training uses 128 x 128 random crops, batch size 4, L1 objective, AdamW and a cosine learning-rate schedule (see config/source for implementation details).
- Validation/test: fixed 256 x 256 RGB crops, mean of **per-crop** PSNR and 11 x 11 Gaussian SSIM; per-patch images and predictions interpreted on 0–1 scale.
- 100 U-Net optimizer updates originated from an earlier pilot checkpoint; the remaining run continued to the 20,000-step milestone. See `legacy_100_import.json` in the private experiment archive for optimizer-state provenance.
- Test results use the `step_020000.pt` milestone weights; they are **not** from `best_weights.pt` selected by validation.

## Files

| File | Purpose |
|---|---|
| `history.csv` | Logged training / validation metrics; 500-step sampling up to 20K |
| `train_log.jsonl` | Training updates and timestamps |
| `run_info.json` | Architecture, configuration and split fingerprints |
| `test_summary.json` | Held-out test score and evaluation details |
| `test_per_crop.csv` | Per-crop PSNR, SSIM, errors and noisy baseline |
| `validation_psnr.png` | Validation PSNR plot derived from `history.csv` |
| `validation_ssim.png` | Validation SSIM plot derived from `history.csv` |
| `validation_loss.png` | Validation L1 loss plot derived from `history.csv` |

## Collaboration and reproducibility

This folder preserves evidence of **@Tanika-git's 20K U-Net training/evaluation experiment**, including workflow adjustments, results and reproducibility details. The recorded source revision is retained in the metadata.

The checkpoint `step_020000.pt` (~94 MB) is **not included in this public folder**. Share privately with teammates when needed to reproduce inference, together with the matching U-Net model code. The raw SIDD training/test images and cropped reference images are **not included** in this public upload. A separate private evidence package holds example Noisy | Prediction | Ground Truth images.

## Public-package labeling note

The original evaluation function labeled its L1 error as `val_l1` even for held-out test data. In this public package, **only** that field name has been changed to `test_l1` in `test_summary.json` and `test_per_crop.csv`. All metrics and values are otherwise unchanged. This does not replace the original private evaluation artifacts.


The experiment's internal validation results must not be presented as official SIDD benchmark scores.

---

**Research project:** Real-World Image Denoising Using Deep Learning  
**Experiment:** U-Net — 20K Training  
**Repository:** `Tanika-git/SIDD-Image-Denoising-S-rgb-medium`  
**Record date:** November 3, 2026
