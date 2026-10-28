# 06 — Evidence-Based Research Timeline

**Workstream maintainer:** @Tanika-git. Historical work dates here are *file/screenshot dates supplied by the maintainer*; they are not Git commit timestamps. GitHub will record the actual upload dates.

| Date or period | Documented work | Evidence and limitations |
|---|---|---|
| By Oct 21, 2026 | Investigated and acquired SIDD-Medium sRGB; extracted and inspected original training archive | Screenshots of archive and folders; exact archive checksum not supplied |
| Oct 21, 2026 | Used PowerShell to count 160 scene folders, 320 noisy files, 320 GT files and 320 matched pairs | Dated terminal screenshot; portable script later adapted from the commands |
| Oct 21, 2026 | Investigated scene naming, ISO, camera IDs, exposure and lighting distributions | Original frequency-table screenshots; independently re-derived from original ranking CSV during package preparation |
| Oct 21, 2026 | Ran example RGB/uint8 pixel inspections and noisy/GT comparisons | Uploaded Python source and terminal results; supplementary PSNR-producing source not supplied |
| Oct 21, 2026 | Built 320-pair ranking table, selected 10 example comparisons and developed SIDD diagrams | Original CSV/JSON/top-10 PNG and original editable presentation; ranking algorithm source not supplied |
| Oct 28, 2026 | Collated public research documentation, portable PowerShell inventory adaptation and metadata figures | New assistant-assisted packaging work; no baseline training claimed |
| Future | Train U-Net/NAFNet, independently code a methodology, evaluate, investigate improvements | Must record actual execution dates and logs as completed |

## Recording new work

For each training run, append actual date, Git commit SHA, configuration, split manifest, GPU, step count, checkpoint reference, PSNR/SSIM and comparison image. Avoid rewriting history to imply older work was committed earlier than it was.
