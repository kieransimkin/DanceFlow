# PrismMoves: capability and package reference

Audited 23 October 2026: **v0.2.0**, exact source [`b9cb0ade27b844674012fe289fcd949ce113ea8e`](https://github.com/kieransimkin/PrismMoves/tree/b9cb0ade27b844674012fe289fcd949ce113ea8e). This is a dated source/documentation audit, not installed-runtime or end-to-end acceptance. [Check current releases before use](../workflows/release-preflight.md).

## Current README feature routes

- [Visualiser descriptions: temporal-first analysis](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md#visualiser-descriptions-temporal-first-analysis)
- [Install and run](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md#install-and-run)
- [What PixelCue contributes](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md#what-pixelcue-contributes)
- [Project-local models](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md#project-local-models)
- [Evidence contract](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md#evidence-contract)
- [Interpretation limits](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md#interpretation-limits)
- [Development and Potential problems](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md#development-and-potential-problems)

## Source documentation and examples

- [`README.md`](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md)
- [`docs/branding/README.md`](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/docs/branding/README.md)
- [`docs/preset-behaviour.md`](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/docs/preset-behaviour.md)

## Package evidence

- [`README.md`](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/README.md) — SHA-256 `ba27729414b649da1ccaaec9ba55a21b25076090b227f026c23833fb8acaa512`.
- [`pyproject.toml`](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/pyproject.toml) — SHA-256 `c0e543c8aa3efe2590984fe836ab283b90cd5ddc74b0984c0c62a3885e600c9a`.
- [`MANIFEST.in`](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/MANIFEST.in) — SHA-256 `61b88c119219722aa559181e228443a3c0a99a2e07c170580e37ea8e6d4d90dc`.
- [`LICENSE`](https://github.com/kieransimkin/PrismMoves/blob/b9cb0ade27b844674012fe289fcd949ce113ea8e/LICENSE) — SHA-256 `bc73e5152b5fe1716c5c8b5cb2b83d51b2e5300827bfa580eeb7a07a498aeafc`.

Package files were read at the pinned source. Published distributions, installed identity, working host examples, rights and reviewed output require their own verification.

## Historical detailed reference

The following older index is retained for detailed routes. Its earlier version is historical; the audited source links above identify current documented availability.

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

## Default-branch availability

The official default branch was also inspected at [`bc0a1bd3e21e1e94e1510d40f4011be624c45b14`](https://github.com/kieransimkin/PrismMoves/tree/bc0a1bd3e21e1e94e1510d40f4011be624c45b14). It differs from the audited stable tag. [Read that exact README](https://github.com/kieransimkin/PrismMoves/blob/bc0a1bd3e21e1e94e1510d40f4011be624c45b14/README.md) for later source/documentation work; this does not establish a newer release, registry version or installed runtime.
