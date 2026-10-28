

from pathlib import Path
from PIL import Image
import numpy as np

# STEP 1: Locate SIDD dataset
root = Path.home() / "Desktop" / "Image and Video_Project" / "train"

# STEP 2: Find the folder starting with 0104_
folders = [p for p in root.glob("0104_*") if p.is_dir()]

if len(folders) != 1:
    raise FileNotFoundError("Could not find a unique 0104 folder.")

folder = folders[0]

# STEP 3: Load noisy and ground-truth images
noisy_path = folder / "0104_NOISY_SRGB_010.PNG"
gt_path = folder / "0104_GT_SRGB_010.PNG"

noisy = np.asarray(
    Image.open(noisy_path).convert("RGB"),
    dtype=np.float32
)

gt = np.asarray(
    Image.open(gt_path).convert("RGB"),
    dtype=np.float32
)

print("Folder:", folder.name)
print("Noisy shape:", noisy.shape)
print("GT shape:", gt.shape)

if noisy.shape != gt.shape:
    raise ValueError("Noisy and GT dimensions do not match.")

# STEP 4: Brightness comparison
print("\n--- BRIGHTNESS COMPARISON ---")

print("Mean per channel, noisy:",
      noisy.mean(axis=(0, 1)).round(1))

print("Mean per channel, GT:",
      gt.mean(axis=(0, 1)).round(1))

print("99.9th percentile, noisy:",
      round(float(np.percentile(noisy, 99.9)), 2))

print("99.9th percentile, GT:",
      round(float(np.percentile(gt, 99.9)), 2))

# STEP 5: Alignment comparison
print("\n--- ALIGNMENT COMPARISON ---")

# Downsample both images for a faster initial check.
# This is an approximate alignment test.
step = 4
noisy_small = noisy[::step, ::step]
gt_small = gt[::step, ::step]

# Check shifts from -4 to +4 ORIGINAL image pixels,
# evaluated on the corresponding subpixel grid.
# Here we instead use full-resolution coordinates
# on a central crop to preserve exact pixel shifts.
h, w = noisy.shape[:2]
crop = 512
cy, cx = h // 2, w // 2

noisy_crop = noisy[
    cy - crop // 2:cy + crop // 2,
    cx - crop // 2:cx + crop // 2
]

gt_crop = gt[
    cy - crop // 2:cy + crop // 2,
    cx - crop // 2:cx + crop // 2
]

best = None

for dy in range(-4, 5):
    for dx in range(-4, 5):

        a = noisy_crop[
            max(0, dy):crop + min(0, dy),
            max(0, dx):crop + min(0, dx)
        ]

        b = gt_crop[
            max(0, -dy):crop + min(0, -dy),
            max(0, -dx):crop + min(0, -dx)
        ]

        mad = np.mean(np.abs(a - b))

        if best is None or mad < best[0]:
            best = (float(mad), dy, dx)

print("Best shift (dy, dx):", (best[1], best[2]))
print("Lowest mean absolute difference:", round(best[0], 2))

print("\nAnalysis completed!")
