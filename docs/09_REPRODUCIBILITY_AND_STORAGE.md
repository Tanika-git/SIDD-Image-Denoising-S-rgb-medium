# 09 — Storage, Privacy and Reproducibility

## Public repository

Publish human-readable methodology, source code, aggregated metadata, model configurations (when created), small analysis figures, accurately attributed sample images and measured result tables.

## Not included in Git history

- Original `train.zip`, extracted multi-GB SIDD images and full dataset subsets.
- Large model checkpoints and optimizer states; keep in Google Drive, with safe references/checksums in logs.
- Windows usernames, absolute private directory paths, tokens, API keys and private credentials.
- Raw screenshots containing personal desktop locations, unfinished drafts or unrelated exploratory datasets; those remain in the **private repository**, after its visibility is verified.

## How to reproduce original dataset checks

1. Obtain SIDD from the cited source under applicable dataset terms.
2. Place the local extracted training directory outside the GitHub repository.
3. Run `scripts/verify_sidd_inventory.ps1 -DatasetRoot <extracted-path>` as documented.
4. If desired, adjust the local path in `scripts/check_sidd_pixels.py` and execute its specific example-pair checks.
5. The bundled metadata CSV can reproduce distributions without the multi-GB dataset. The original ranking-score algorithm has not yet been supplied; the ranking CSV is a preserved research artifact, not a reproducible ranking algorithm.

## Experiment logs to add later

Dataset variant and checksum (where available); script/commit version; split manifest and seed; patch size; model hyperparameters; exact training steps and wall time; GPU memory; validation history; best/last checkpoints; PSNR/SSIM conventions; inference latency method; side-by-side PNG samples. Do not claim equivalence to official published benchmark settings without validating the protocol.
