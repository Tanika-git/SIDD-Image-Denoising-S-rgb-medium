# Paired image candidate ranking (pretraining exploration)

**Original data:** 320-record CSV submitted by @Tanika-git, plus a selected top-10 JSON file and collage. The published JSON excludes the original absolute Windows root path; the full original file is retained locally, outside GitHub.

- `SIDD_Pair_Ranking.csv`: contains relative noisy and GT filenames, heuristic `score`, `noise_estimate`, `detail`, ISO, lighting and selected crop coordinates. This is **not a PSNR/SSIM benchmark**.
- `sidd_ranked_pairs_public.json`: top 10 entries and metadata with personal root stripped. No image pixels inside.
- `scene_instance_metadata.csv`: deterministic folder-level parsing of the original CSV, used for the public plots. 160 scene-instance rows; one row per folder.

## Internal checks performed during packaging

- Exactly 320 original pair records.
- Exactly 160 unique folder strings, with exactly two rows per folder.
- 320 unique noisy paths and 320 unique GT paths in the CSV.
- Replacing `_NOISY_SRGB_` with `_GT_SRGB_` in a noisy path matches its recorded paired GT path for all rows.
- ISO, scene ID, camera, color-temperature and lighting distributions sum to 160 unique folder records.

These are consistency checks on supplied **text files**. They are not claims that every original PNG was decoded or that ranking scores were independently recalculated. The script that generated the score has not been supplied; its method and exact parameters are presently unverified.
