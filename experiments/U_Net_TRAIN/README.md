# U-Net Training on SIDD-Medium sRGB — 20,000 Steps

## Experiment Overview

This folder documents my U-Net image-denoising training experiment conducted on the SIDD-Medium sRGB dataset as part of our team's image restoration research project.

**Experiment ID:** `sidd_unet_seed42_v1`  
**Experiment date:** November 3, 2026  
**Platform:** Kaggle  
**GPU:** NVIDIA Tesla T4  
**Training target:** 20,000 steps  
**Dataset:** SIDD-Medium sRGB  
**Training objective:** Restore clean RGB images from real noisy smartphone images.

This is an independently executed U-Net training experiment contributing to our team's comparative study of image-denoising architectures.

## 1. Dataset and Methodology

The experiment uses paired noisy and ground-truth images from SIDD-Medium sRGB.

The prepared dataset contains 320 noisy/clean image pairs, with a previously verified scene-grouped split:

| Split | Image pairs |
|---|---:|
| Training | 220 |
| Validation | 70 |
| Test | 30 |

The training pipeline uses 128×128 image patches, L1 reconstruction loss, AdamW optimization, mixed precision and a cosine learning-rate schedule.

The experiment continued from a previously saved 100-step U-Net checkpoint. The import was recorded in `legacy_100_import.json`.

Changes between the original 100-step experiment and the subsequent training configuration should be considered when interpreting the results.

## 2. Training Results

**Status: 20,000 reported training steps completed.**

| Metric | Final logged value |
|---|---:|
| Training target | 20,000 steps |
| Internal validation PSNR | **36.533 dB** |
| Internal validation SSIM | **0.90064** |
| Logged training L1 loss at 20K | **0.01287** |
| Logged AMP skipped updates | 7 |

The training logs report reaching step 20,000. The seven skipped mixed-precision updates should be considered when documenting the exact number of successful optimizer updates.

These PSNR and SSIM values are from **internal validation**, not the official SIDD benchmark or the final held-out test set.

## 3. Permanent Model Checkpoints

The following milestone checkpoints were saved in the project's private Hugging Face storage:

| Milestone | Checkpoint |
|---|---|
| 1,000 steps | `step_001000.pt` |
| 5,000 steps | `step_005000.pt` |
| 10,000 steps | `step_010000.pt` |
| 20,000 steps | `step_020000.pt` |

Each checkpoint is approximately 94.2 MB.

**Private checkpoint location:**

`tanvash/SIDD_RESEARCH_TRAINING/runs/sidd_unet_seed42_v1/unet/milestones/`

The 20K checkpoint has also been downloaded for private sharing and further verification.

Checkpoint files are deliberately not included in this public GitHub directory. Access can be arranged with the experiment owner.

## 4. Training Evidence and Figures

The experiment produces and preserves research evidence including:

- Training loss
- Validation L1 loss
- Validation PSNR
- Validation SSIM
- Checkpoint and training metadata
- Training logs
- Fixed validation-image selection metadata

Graphs for the 1K and 5K milestones were confirmed in Hugging Face storage. Remaining figures, complete metric histories and final denoising image comparisons require verification before inclusion in the final paper.

No unverified metrics or generated images are reported as experimental results.

## 5. Reproducibility and Experiment Records

The experiment uses a fixed random seed of 42 and an internal scene-disjoint data split.

Supporting records in private experiment storage include:

- `run_info.json`
- `history.csv`
- `train_log.jsonl`
- `legacy_100_import.json`
- `fixed_validation_selection.json`
- `selected_batch.json`
- `backup_status.jsonl`

The original training notebook, checkpoint metadata and exact runtime configuration should be used when reproducing the experiment.

## 6. Individual Contribution and Team Collaboration

This folder documents my contribution to the research project, including conducting and monitoring the U-Net training experiment, troubleshooting the Kaggle workflow, preserving model checkpoints, tracking validation performance and organizing experimental evidence.

The overall project is a team effort. Other team members have also worked on U-Net and NAFNet implementations and experiments.

The U-Net architecture itself and any reused or adapted implementation code are credited to their respective original authors and contributors. This record does not claim invention of the architecture or exclusive authorship of shared code.

Results from this experiment may contribute to our team's research paper with appropriate acknowledgment of the individual experimental work.

## 7. Evaluation Status and Limitations

**Completed:**
- U-Net training to the configured 20K target
- Final internal validation logging
- Cloud storage of all four permanent milestone checkpoint files
- Preservation of key experimental records

**Remaining verification:**
- Loading and checking the archived checkpoints for reproducible inference
- Final held-out test metrics
- Complete 10K/20K research figures
- Four-image denoising comparisons
- Comparison with the teammate's U-Net experiment under a consistent evaluation protocol

The experiment's internal validation results must not be presented as official SIDD benchmark scores.

---

**Research project:** Real-World Image Denoising Using Deep Learning  
**Experiment:** U-Net — 20K Training  
**Repository:** `Tanika-git/SIDD-Image-Denoising-S-rgb-medium`  
**Record date:** November 3, 2026
