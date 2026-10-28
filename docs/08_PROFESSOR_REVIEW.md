# 08 — Professor Review Brief · 29 October 2026

## Work completed and available to demonstrate

- SIDD-Medium sRGB dataset selected and locally acquired.
- 160 scene-instance directories inventoried and 320 noisy/clean filename pairs identified.
- Image dimensions, RGB/uint8 representation, camera identifiers, ISO and lighting conditions studied.
- Original noisy/GT pixel inspection code and example intensity/alignment diagnostics recorded.
- Original 320-record candidate-ranking data, ten visual comparisons and dataset diagrams supplied.

## Existing published baseline approaches

U-Net supplies an encoder–decoder with skip connections. NAFNet provides a simpler restoration design with mechanisms including SimpleGate. Baseline training code exists in a separately credited teammate repository. No completed full training runs or benchmark results have been established by the materials in this repository.

## Next experiment stages

1. Transfer the locally acquired SIDD archive to Drive and verify image-pair decoding in Colab.
2. Run the baseline sanity checks and initiate resumable training.
3. Implement the independent model/training pipeline with documented code changes.
4. Study whether adaptive gating is justified by related work; define a concrete ablation only after review.
5. Evaluate under a fixed scene-disjoint split and report measured PSNR, SSIM, latency and failure cases.

## Research question to discuss

**Does input-dependent gating offer a measurable benefit over standard NAFNet's SimpleGate for real smartphone noise under a controlled SIDD protocol?** This is a proposed question, not a claimed discovery.

## Suggested evidence for the discussion

Show the original PowerShell matching screenshot privately if asked, the publicly shareable profiling plots, the original Python pixel check and the top-10 figure. Distinguish archived experimental evidence from actual trained models.
