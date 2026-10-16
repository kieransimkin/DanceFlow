# Image evidence and visual-language profiles

Use PixelCue to analyse, PrismMoves to organise its receipts, and the visual-identity workflow to reason about independent approved assets. The tools keep measurements, model hypotheses, interpretations and proposals separate.

![Synthetic fixture with actual measured palette and the PixelCue-to-PrismMoves handoff](https://raw.githubusercontent.com/kieransimkin/PrismMoves/main/docs/images/visual-profile-example.png)

Generated measurement figure from PixelCue 0.9.0; not a screenshot or proof of semantic accuracy.

1. Select explicit authorised images. Record roles, dates, provenance and lineage without inferring approval from a filename.
2. Inspect PixelCue /health. Use pixelcue_visual_analysis for a bounded MCP receipt, or run PrismMoves against PixelCue's Python API or loopback service to generate JSON, Markdown, HTML and the measured SVG summary.
3. Request only useful optional cached models, with explicit inference consent for MCP calls. Install any authorised weights and caches inside the owning project's ignored models/. No hidden global-cache downloads, face identification or training are part of this workflow.
4. Review the actual image and every model receipt. Missing models are unavailable evidence; CLIP similarity is prompt-relative, OCR/captions/tags can be wrong, palette contrast is not actual text contrast, and signal novelty is not gaze.
5. For a collection, compare approved independent lineages, identify coherent families and contextualise outliers. Avoid turning one asset or several crops into a recurring brand rule.

RasterMoves applies only when an authorised derivative is required. ThumbMoves supports browsing without a second thumbnail cache. KeywordMoves can organise truthful source language but does not turn image hypotheses into search-demand evidence. Audio/motion/rendering tools apply when there is a real creative handoff, not just to populate a checklist.
