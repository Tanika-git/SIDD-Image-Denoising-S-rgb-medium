# SIDD-Medium sRGB: preliminary U-Net & NAFNet smoke tests

**Experiment date:** 29 October 2026  
**Status:** Two-step CPU pipeline verification; **not** full-dataset training or benchmark reproduction.

## What was completed

- Verified the presence and filename pairing of the original SIDD-Medium sRGB training data: **160 scene-instance directories; 320 noisy and 320 ground-truth PNGs (320 matched pairs)**. This is an inventory check, not a full-file integrity or image-alignment audit.
- Selected **three distinct physical scenes**, using one paired image per scene and assigning one scene to each of train, validation, and test.
- Ran **2 optimizer steps on CPU** for each of the existing U-Net and NAFNet baseline implementations, with batch size 1 and training patch size 64 x 64.
- Confirmed checkpoint saving and loading, produced inference images, and calculated preliminary PSNR on matching 64 x 64 centre crops.

**Crucial distinction:** The 320-pair dataset was verified, but **training was only performed on one image pair in the tiny subset**. These tests check that the software runs; they do not demonstrate effective denoising or quantify performance across SIDD-Medium.

## Results: 2-step CPU smoke test

| Scene split | Noisy-input PSNR (dB) | U-Net, 2 steps (dB) | NAFNet, 2 steps (dB) |
|:--|--:|--:|--:|
| Train | 32.94 | 17.28 | 13.84 |
| Validation | 34.37 | 17.29 | 11.31 |
| Test | 31.95 | 19.24 | 23.71 |

PSNR is calculated against the corresponding ground-truth crop. **Both models scored worse than leaving the noisy input unchanged** in this tiny test. Two training steps are not sufficient for meaningful architecture comparison.

### Visual results

**Noisy input | U-Net | NAFNet | Ground truth**, at identical crop locations:

![Two-step U-Net and NAFNet predictions compared with the same noisy and ground-truth crops](results/unet_vs_nafnet_step2.png)

Additional figures: [U-Net-only predictions](results/unet_step2_predictions.png), [three scene-separated pairs](results/three_scene_split.png), [additional noisy/ground-truth comparisons](results/three_sidd_comparisons.png).

The corresponding numbers are stored in [`results/metrics_summary.csv`](results/metrics_summary.csv). The small experiment configurations are in [`configs/`](configs/).

**Presentation PDF:** [Tanika - SIDD Denoising Results](Tanika_SIDD_Denoising_Results_GitHub.pdf). This is a presentation record of the same preliminary two-step experiment; it does not add new training results.

## Provenance and attribution

- **Baseline model, training and evaluation implementation:** [nitya-goyal/SOTA-Image-Denoising](https://github.com/nitya-goyal/SOTA-Image-Denoising), reference commit `cfb53ca3033b4a31f4a91d1fcd45c2e06f46d3c2` recorded during the Colab run. The model source itself is **not redistributed in this folder**.
- **Dataset verification, tiny-experiment preparation, execution and result compilation in this repository:** [@Tanika-git](https://github.com/Tanika-git), as part of the image-denoising team project.
- **Dataset:** Abdelhamed, Lin and Brown, *A High-Quality Denoising Dataset for Smartphone Cameras*, CVPR 2018. [Official SIDD site](https://abdokamel.github.io/sidd/index.html). Dataset copyright and license remain with its original authors (official website lists an MIT license).

## Next research steps

Train U-Net and NAFNet using a properly scene-separated full-dataset protocol and compare results on a sufficiently sized, held-out split; report PSNR, SSIM, and visual examples with training budget and hardware details. Investigating alternative gating mechanisms is **proposed future work**, not an experimentally established improvement.

## Sharing and reproducibility notes

This public folder is a **report of the smoke-test outputs**. It intentionally excludes the full SIDD dataset, full executable notebook, personal Drive paths, model checkpoints, and private development logs. The original development artifacts are retained separately by their owners. The images are derived from SIDD examples and must retain dataset attribution when reused.
