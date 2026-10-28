# 05 — Planned Experimental Methodology and Research Direction

**Status: proposed protocol, not completed model experiments.**

## A — Reference baseline verification

- Use the existing, separately credited [team notebook](https://github.com/nitya-goyal/SOTA-Image-Denoising) for reference U-Net and standard NAFNet.
- Record the source revision, dataset path, scene-disjoint splitting rule, hyperparameters and hardware.
- Start with a short sanity test, then use resumable checkpoints on Google Drive.
- Compare methods on the *same* held-out images and with the same PSNR/SSIM conventions.
- Distinguish preliminary validation measurements from final held-out results.

## B — Independent implementation, led in this repository

Build an independently maintained PyTorch project for data handling, paired cropping, training, checkpointing, and reproducible metrics. Develop model components with conceptual grounding in the original U-Net and NAFNet papers; do not present the standard architectures as original inventions.

## C — Research hypothesis suggested by course notes

Course notes discuss NAFNet's **SimpleGate** and an *adaptive gating* direction. A working hypothesis is to ask whether an input-dependent gate can improve denoising of challenging real noise with reasonable cost. This is **not yet an architecture, novel claim, paper result or implemented algorithm**. Perform a literature check first to determine what already exists, then specify a falsifiable comparison and ablation.

## Experimental fairness checklist

1. Fix a seed and save a scene-disjoint split manifest, using physical scene IDs rather than treating all related captures as independent.
2. Preserve original dataset, pixel type, and consistent normalization.
3. Record patch size, model width, parameters, optimizer, total steps, evaluation intervals, training time and GPU.
4. Keep the original U-Net and NAFNet as explicit baselines, not modified silently.
5. Report PSNR/SSIM, visual comparisons, checkpoint step, test split and inference-time conditions.
6. If reduced model sizes are necessary due to GPU memory, name them clearly; don't claim equivalence to full published models.
7. Use a pre-defined held-out test set to avoid choosing settings on the final evaluation data.

## Paper and authorship

Dataset preparation and experimental design are substantive contributions. Team-wide paper author order and formal leadership should be agreed based on actual contributions with the supervisor. Repository ownership by itself is not first-author evidence.
