# 04 — Pixel-Level Inspection and Noisy-Input Quality Checks

**Original Python source:** [`check_sidd_pixels.py`](../scripts/check_sidd_pixels.py) — provided by the maintainer as an October 21 local source file.

The script loads a matched `_010` pair for scene instance `0104_005_S6_03200_01600_4400_L`, converts both images into RGB float32 arrays, checks equal shapes, then examines channel brightness and searches small integer shifts on a central crop using mean absolute difference.

## Original screenshot values (single pair only)

| Measurement | Recorded observation |
|---|---|
| Noisy image shape | `(3000, 5328, 3)` |
| Clean GT image shape | `(3000, 5328, 3)` |
| Noisy per-channel means | `[99.3, 72.3, 73.7]` |
| GT per-channel means | `[117.1, 80.6, 86.8]` |
| Noisy 99.9th intensity percentile | `204.0` |
| GT 99.9th intensity percentile | `159.0` |
| Best integer shift, 512×512 central-crop search | `(dy=0, dx=0)` |
| Central-crop minimum mean absolute difference | `24.98` |
| Full-image mean absolute difference (separate screenshot) | `30.86` |
| Noisy-input vs GT PSNR (separate screenshot) | `16.08 dB` |

The supplied screenshots also show sample image dimensions of 5312×2988, 4032×3024, 4048×3044 and 5328×3000; these demonstrate why a loader must not assume all scenes have identical full-image dimensions.

### Interpretation and caveats

- **16.08 dB is a noisy-input PSNR**, not a PSNR achieved by a trained denoising model.
- The central-crop shift result is a local heuristic. `(0,0)` minimizes the tested shifts on that crop; it does not certify geometric alignment for the full dataset.
- The central-crop MAD and full-image MAD are computed over different regions; they should not be compared as identical measurements.
- Original analysis screenshots show RGB/uint8 pixel values in `[0,255]`. A subsequent PyTorch loader should convert these to suitable floating-point tensors and consistently normalize the inputs.
- The uploaded original Python file produces the brightness/alignment output. The Python source generating the separate 16.08 dB PSNR screenshot was **not included** and should not be attributed to this script without verification.

## Next verification stage

Re-run RGB decoding, spatial size matching, noisy/GT matching and numerical input validation in Google Colab on the actual archived dataset. Keep per-image results for reproducibility.
