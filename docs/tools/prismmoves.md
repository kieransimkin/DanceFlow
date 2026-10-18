# PrismMoves

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/PrismMoves)

Understand an image before extending its visual language. PrismMoves turns PixelCue measurements and selected model hypotheses into an inspectable colour, texture and composition profile, with JSON, Markdown, HTML and a measured SVG summary.

![Original synthetic image and actual PixelCue measurements, composed into a PrismMoves profile](https://raw.githubusercontent.com/kieransimkin/PrismMoves/main/docs/images/visual-profile-example.png)

This generated measurement figure uses PixelCue 0.9.0 and an original synthetic fixture; it is not a UI screenshot or an accuracy evaluation.

Install PrismMoves from its tested GitHub release. It calls installed PixelCue 0.9.0+ in-process, or its loopback /v1/analysis service. For example: `prismmoves cover.png --pixelcue-url http://127.0.0.1:8765 --out analysis/new-cover`. Optional CLIP, DINOv2, BLIP and OCR need their dependencies and selected local models. Keep weights and caches inside the owning project's ignored models/ directory. No downloads occur by default. The hub's pixelcue_visual_analysis MCP tool calls the same PixelCue endpoint; it returns receipts, while the PrismMoves CLI produces the reports.

Measurements, model interpretations and unavailable evidence remain distinct. One image does not establish recurring brand rules, rights, artist intent or audience response. Use assess-visual-identity with approved independent comparison evidence for those collection conclusions.

See the canonical README for options, explicit model installation, versions and limitations. Engine improvements belong in PixelCue; reporting improvements belong in PrismMoves.

## Full feature workflow

[Read the released feature references](../capabilities/prismmoves.md) and [check current releases before every new run](../workflows/release-preflight.md). Consider the whole ecosystem, use and improve applicable shared capabilities, and keep actual runtime/output evidence separate from availability.
