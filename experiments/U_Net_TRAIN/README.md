# U-Net Image Denoising on SIDD-Medium (sRGB)

**20,000-step training experiment · Real-world image noise · Reproducible experiment records**

This folder documents a completed U-Net denoising experiment on the **SIDD-Medium sRGB** dataset. It includes the training configuration, validation history, held-out test measurements, and plots used in our research analysis.

**Experiment lead (training workflow, execution, and result documentation): [@Tanika-git](https://github.com/Tanika-git)**  
**Experiment ID:** `sidd_unet_seed42_v1` · **Completed:** 3 November 2026 · **Random seed:** `42`

> **Evaluation scope:** These are results from a **custom, scene-disjoint, fixed-crop evaluation** of SIDD-Medium sRGB—not scores from the official SIDD benchmark. Scores from different test protocols should not be compared directly.

## Results at a glance

| Evaluation set | Noisy input PSNR | U-Net PSNR | U-Net SSIM | What it measures |
|---|---:|---:|---:|---|
| **Validation** | 27.727 dB | **36.533 dB** | **0.90064** | Fixed validation crops evaluated during training |
| **Held-out test** | 28.259 dB | **41.232 dB** | **0.95286** | 60 fixed test crops evaluated after training |

**Higher PSNR and SSIM indicate better reconstruction quality.** Both reported U-Net scores are averages over individual RGB crops, not full-resolution images. Validation and test use different physical-scene groups, so the two scores are **not interchangeable**.

The test figures above were calculated using the **saved step-20,000 checkpoint**, not the validation-selected `best_weights.pt`. See [`test_summary.json`](test_summary.json) and [`test_per_crop.csv`](test_per_crop.csv) for the test measurements.

## Training progress

Validation metrics were logged every **500 optimizer steps**, from step 500 through step 20,000.

| Validation PSNR | Validation SSIM |
|---|---|
| ![Validation PSNR across 20K steps](validation_psnr.png) | ![Validation SSIM across 20K steps](validation_ssim.png) |

**Validation reconstruction loss (L1)**

![Validation L1 error across 20K steps](validation_loss.png)

The plots are derived from [`history.csv`](history.csv). They describe **validation performance**, not the final held-out test curve.

## Dataset and evaluation design

We used **320 noisy/clean image pairs** from SIDD-Medium sRGB, split by physical scene rather than randomly mixing crops from the same scene:

| Split | Image pairs | Use |
|---|---:|---|
| Training | 220 | Learn to map noisy sRGB images to clean images |
| Validation | 70 | Track training and checkpoint quality |
| Held-out test | 30 | Assess the trained model on a separate physical-scene group |

For evaluation, two predetermined **256 × 256 RGB crops** were sampled per image pair. The held-out test therefore contains **60 crops**. Metrics are computed **per crop and then averaged**. PSNR uses float RGB intensities; SSIM uses an 11 × 11 Gaussian window. Predictions are clamped to the 0–1 intensity range before evaluation.

Exact scene assignments and dataset-manifest fingerprints are recorded in [`run_info.json`](run_info.json).

## Model and training configuration

| Setting | Recorded value |
|---|---|
| Architecture | U-Net for RGB image restoration |
| Model parameters | 7,846,723 |
| Training target | 20,000 successful optimizer updates |
| Starting point | Earlier 100-step U-Net pilot checkpoint |
| Training input | Random 128 × 128 subcrops from cached 192 × 192 patches |
| Batch size | 4 |
| Objective | L1 reconstruction loss |
| Optimizer | AdamW |
| Learning rate | 0.0002 to 0.000001, cosine schedule |
| Precision | CUDA automatic mixed precision (AMP) |
| Training hardware | Kaggle, one NVIDIA Tesla T4 GPU |
| Saved milestones | 1K, 5K, 10K, and 20K steps |

The log records **7 AMP-skipped update attempts**; the step counter refers to successful optimizer updates. Pilot checkpoint import and optimizer-state details are retained in the private run archive. See [`train_log.jsonl`](train_log.jsonl) for the recorded training events.

## Files in this experiment

| File | Contents |
|---|---|
| [`history.csv`](history.csv) | Step-wise training/validation metrics and learning rate |
| [`train_log.jsonl`](train_log.jsonl) | Timestamped training progress and system measurements |
| [`run_info.json`](run_info.json) | Model settings, dataset split, source revision, and environment |
| [`test_summary.json`](test_summary.json) | Final held-out test metrics and evaluation conditions |
| [`test_per_crop.csv`](test_per_crop.csv) | All 60 individual test-crop measurements |
| `validation_psnr.png` | Validation PSNR progression |
| `validation_ssim.png` | Validation SSIM progression |
| `validation_loss.png` | Validation reconstruction-loss progression |
| [`CONTRIBUTIONS_AND_PROVENANCE.md`](CONTRIBUTIONS_AND_PROVENANCE.md) | Experiment contributions and checkpoint provenance |

## Contribution and reproducibility

**[@Tanika-git](https://github.com/Tanika-git)** carried out and documented this U-Net experiment, including the adapted training workflow, checkpoint management, 20K-step run, results collection, and evaluation evidence. The dated configuration and result files provide a traceable record of the work. Additional details are in [`CONTRIBUTIONS_AND_PROVENANCE.md`](CONTRIBUTIONS_AND_PROVENANCE.md).

The saved **`step_020000.pt` checkpoint (~94 MB)** and raw SIDD images are retained **privately**, not published here. Re-running inference requires the checkpoint, matching U-Net implementation, and the same test inputs/preprocessing. The specific source-code revision is recorded in `run_info.json`.

### Reporting limitations

- **Not the official SIDD benchmark:** this is a project-defined fixed-crop, scene-disjoint protocol.
- **One held-out physical-scene group:** the test result should not be generalized to every device, scene, or noise condition.
- **Test provenance check pending:** the full test-crop manifest has not been independently matched crop-by-crop against the original source files after export; the saved checkpoint and recorded split fingerprints were checked.
- **Fair model comparisons require the same evaluation:** if another U-Net, NAFNet, or baseline reports a different PSNR, confirm the test images, metric implementation, preprocessing, and averaging first.

**Research use:** Cite the validation and held-out test values separately, and describe them as **internal SIDD-Medium sRGB fixed-crop results**.

