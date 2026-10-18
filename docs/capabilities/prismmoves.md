# PrismMoves: complete capability reference

Inspected stable source: [v0.2.0](https://github.com/kieransimkin/PrismMoves/releases/tag/v0.2.0), commit `b9cb0ade27b844674012fe289fcd949ce113ea8e`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md).

## Choose and use a route

| Goal | Supported route and evidence |
|---|---|
| Profile images | Use CLI/Python or the existing PixelCue service; write JSON, Markdown, HTML, SVG and checksum evidence without modifying inputs. |
| Describe presets | Use prismmoves-preset analyse for dense temporal measurements first, bounded nonblank representative frames and per-preset evidence-linked descriptions. Legacy report replay does not invent motion or rerun inference. |
| Interpret the evidence | Keep measured facts, model hypotheses and unknowns separate. Compare independent image lineages before inferring recurring visual identity; no overall brand/quality score is invented. |

## Released reference coverage

Each entry links to the exact released explanation, options, example or limitation. These are documented capabilities, not a claim that every option was run on this computer. Review the relevant source before configuring it.

- [Visualiser descriptions: temporal-first analysis](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/README.md#visualiser-descriptions-temporal-first-analysis) — `README.md`.
- [Install and run](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/README.md#install-and-run) — `README.md`.
- [What PixelCue contributes](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/README.md#what-pixelcue-contributes) — `README.md`.
- [Project-local models](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/README.md#project-local-models) — `README.md`.
- [Evidence contract](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/README.md#evidence-contract) — `README.md`.
- [Interpretation limits](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/README.md#interpretation-limits) — `README.md`.
- [Development and Potential problems](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/README.md#development-and-potential-problems) — `README.md`.
- [Preset behaviour: temporal first, semantics selectively](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/docs/preset-behaviour.md#preset-behaviour-temporal-first-semantics-selectively) — `docs/preset-behaviour.md`.
- [Recommended path](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/docs/preset-behaviour.md#recommended-path) — `docs/preset-behaviour.md`.
- [Measurements and limits](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/docs/preset-behaviour.md#measurements-and-limits) — `docs/preset-behaviour.md`.
- [Caching and interrupted work](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/docs/preset-behaviour.md#caching-and-interrupted-work) — `docs/preset-behaviour.md`.
- [Reuse the reports you already paid to generate](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/docs/preset-behaviour.md#reuse-the-reports-you-already-paid-to-generate) — `docs/preset-behaviour.md`.
- [Development](https://github.com/kieransimkin/PrismMoves/blob/v0.2.0/docs/preset-behaviour.md#development) — `docs/preset-behaviour.md`.

## Examples and media

Use the runnable examples and actual screenshots/videos linked from the released references. Keep their documented version/context and distinguish synthetic fixtures, model hypotheses and real captured output. Do not represent a guide link as proof that a model, GPU, physical phone or production host was tested. New decorative generated imagery adds no feature evidence to this reference index.
