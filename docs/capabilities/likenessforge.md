# LikenessForge: complete capability reference

Inspected stable source: [v0.4.5](https://github.com/kieransimkin/LikenessForge/releases/tag/v0.4.5), commit `cc0ff31717bf69a98c6a59eaf9e9a1cdc1783024`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md).

## Choose and use a route

| Goal | Supported route and evidence |
|---|---|
| Choose the workflow | Use explicit face indexing and detector/segmenter/modifier/trainer plugins in the shared CLI or desktop GUI. Use repair and repair-wizard comparisons for authorised references. |
| Prepare training | Inspect dataset/holdout preparation, train/train-wizard, selected revisions, LoRA settings and real low-VRAM/offload limits. Training is conditional on an actual identity task. |
| Review candidates | Keep originals, identity references/weights, intermediate traces and candidate sheets controlled. Model progress and pipeline completion do not replace likeness/full-composition review. |

## Released reference coverage

Each entry links to the exact released explanation, options, example or limitation. These are documented capabilities, not a claim that every option was run on this computer. Review the relevant source before configuring it.

- [Requirements and scope](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#requirements-and-scope) — `README.md`.
- [What it does](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#what-it-does) — `README.md`.
- [Built-in plugins](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#built-in-plugins) — `README.md`.
- [Model storage and cleanup](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#model-storage-and-cleanup) — `README.md`.
- [8 GB GPUs](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#8-gb-gpus) — `README.md`.
- [Start the desktop GUI (recommended)](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#start-the-desktop-gui-recommended) — `README.md`.
- [Manual install](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#manual-install) — `README.md`.
- [Inspect plugins and models](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#inspect-plugins-and-models) — `README.md`.
- [Identify the face index](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#identify-the-face-index) — `README.md`.
- [Repair a face](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#repair-a-face) — `README.md`.
- [Repair wizard](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#repair-wizard) — `README.md`.
- [Train a LoRA](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#train-a-lora) — `README.md`.
- [Training wizard](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#training-wizard) — `README.md`.
- [FLUX.2 Klein LoRA](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#flux2-klein-lora) — `README.md`.
- [Configuration file](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#configuration-file) — `README.md`.
- [Third-party/custom plugins](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#third-partycustom-plugins) — `README.md`.
- [Debugging](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#debugging) — `README.md`.
- [Tests and GitHub CI](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#tests-and-github-ci) — `README.md`.
- [Privacy and responsible use](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#privacy-and-responsible-use) — `README.md`.
- [Contribute](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/README.md#contribute) — `README.md`.
- [Architecture](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/ARCHITECTURE.md#architecture) — `docs/ARCHITECTURE.md`.
- [Repair data flow](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/ARCHITECTURE.md#repair-data-flow) — `docs/ARCHITECTURE.md`.
- [Training data flow](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/ARCHITECTURE.md#training-data-flow) — `docs/ARCHITECTURE.md`.
- [Desktop GUI](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/ARCHITECTURE.md#desktop-gui) — `docs/ARCHITECTURE.md`.
- [Bootstrap and CI](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/ARCHITECTURE.md#bootstrap-and-ci) — `docs/ARCHITECTURE.md`.
- [LikenessForge image preparation in DanceFlow](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/DANCEFLOW.md#likenessforge-image-preparation-in-danceflow) — `docs/DANCEFLOW.md`.
- [Choose and record the inputs](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/DANCEFLOW.md#choose-and-record-the-inputs) — `docs/DANCEFLOW.md`.
- [Prepare and review a repair](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/DANCEFLOW.md#prepare-and-review-a-repair) — `docs/DANCEFLOW.md`.
- [Hand the selected asset to the next tool](https://github.com/kieransimkin/LikenessForge/blob/v0.4.5/docs/DANCEFLOW.md#hand-the-selected-asset-to-the-next-tool) — `docs/DANCEFLOW.md`.

## Examples and media

Use the runnable examples and actual screenshots/videos linked from the released references. Keep their documented version/context and distinguish synthetic fixtures, model hypotheses and real captured output. Do not represent a guide link as proof that a model, GPU, physical phone or production host was tested. New decorative generated imagery adds no feature evidence to this reference index.
