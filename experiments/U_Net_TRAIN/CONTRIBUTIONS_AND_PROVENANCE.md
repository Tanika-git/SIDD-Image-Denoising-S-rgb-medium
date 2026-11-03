# Experiment contributions and provenance — U-Net 20K

**Public GitHub experiment record:** `experiments/U_Net_TRAIN/` in `Tanika-git/SIDD-Image-Denoising-S-rgb-medium`  
**Experiment operator / results:** **[@Tanika-git](https://github.com/Tanika-git)**  
**Experiment ID:** `sidd_unet_seed42_v1`  
**Date of completed saved milestone:** **2026-11-03** (UTC timestamp stored inside checkpoint: `2026-11-03T02:36:06+00:00`)

## Documented work attributable to @Tanika-git

- Configured/adapted the U-Net training workflow and ran/managed the SIDD-Medium sRGB experiment through the saved 20,000-step milestone, beginning from an earlier 100-step pilot checkpoint.
- Monitored and retained training history, validation statistics, timestamps, model configurations, run logs, and milestone artifacts.
- Preserved checkpoints, including `step_020000.pt`, and organized the experiment's public research evidence.
- Collected the matching fixed-crop held-out test arrays and completed/recorded the post-training evaluation with the trained checkpoint; metrics and limitations are in `test_summary.json` and `README.md`.
- Documented the experiment results and evaluation protocol for team research reporting.

These statements record the **workflow changes, execution, results and saved evidence** of this experiment by **@Tanika-git**. The reference code revision is preserved in `run_info.json` for technical reproducibility. This record does not claim that U-Net or the SIDD dataset were invented in this experiment.

## Original private evidence (not in the public ZIP)

- Final saved milestone: `step_020000.pt` (94,214,219 bytes)
- SHA-256: `cf4a28c5f97d6b1a4c4a2a6fa256fbc0d51a147c36128d773bf89c43d949e073`
- Save time in checkpoint: `2026-11-03T02:36:06+00:00` UTC
- Retained under private bucket: `tanvash/SIDD_RESEARCH_TRAINING/runs/sidd_unet_seed42_v1/unet/milestones/`
- Kaggle's saved run version, original checkpoints, training histories and experiment artifacts should be kept unchanged for independent verification.

## Results and limitations

- 20K **internal validation**: **36.5328 dB PSNR**, **0.900644 SSIM**.
- 20K **internal held-out test**: **41.2316 dB PSNR**, **0.952857 SSIM** on 60 fixed 256×256 crops supplied with the experiment record.
- This is an **internal custom physical-scene-disjoint SIDD-Medium sRGB evaluation**; it is **not** an official SIDD benchmark result.
- Full independent matching of test crops to the original dataset's test-crop manifest has **not** been completed; preserve that caveat in any report.
- Comparisons with teammates' scores require a matching evaluation protocol (same images, preprocessing, metrics and averaging).

## Sharing boundary

The public ZIP includes metadata, logs, plots and metric summaries. It **does not** contain the final model weights, SIDD source images, or access credentials. Do not give unrestricted access to the private checkpoint bucket. If sharing checkpoint access, use a restricted recipient-specific link.
