# PixelCue: complete capability reference

Inspected stable source: [v0.9.1](https://github.com/kieransimkin/PixelCue/releases/tag/v0.9.1), commit `d09861b04dea033d26303d6099837785eeb48686`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md).

## Choose and use a route

| Goal | Supported route and evidence |
|---|---|
| Discover and tag media | Use scoped image/video/archive discovery, model selection, search/filter/tag clouds and persistent analysis/history/resume. Reuse ThumbMoves cache previews before source decoding where useful. |
| Measure images | Use public visual_analysis APIs for decoding, palette, texture, composition, frequency and explicit cached-model hypotheses. Individual unavailable model receipts preserve deterministic statistics. |
| Measure sequences | Use dense temporal evidence, bounded batches and shared model sessions; frame captions do not establish rotation or rhythmic motion. |
| Compose services | Use the documented loopback REST/Socket.IO service, health/model profiles and request-scoped progress. Optional face clustering, downloads and hosted exposure require their actual scope. |

## Released reference coverage

Each entry links to the exact released explanation, options, example or limitation. These are documented capabilities, not a claim that every option was run on this computer. Review the relevant source before configuring it.

- [Temporal evidence and efficient visual batches (0.9.1)](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#temporal-evidence-and-efficient-visual-batches-091) — `README.md`.
- [Visual analysis API (0.9.0)](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#visual-analysis-api-090) — `README.md`.
- [Agents and contributors](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#agents-and-contributors) — `README.md`.
- [Behaviour](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#behaviour) — `README.md`.
- [Image tagging model choice](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#image-tagging-model-choice) — `README.md`.
- [JoyCaption / GPU](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#joycaption--gpu) — `README.md`.
- [Installation (uv)](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#installation-uv) — `README.md`.
- [Prerequisites](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#prerequisites) — `README.md`.
- [Full install (recommended)](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#full-install-recommended) — `README.md`.
- [REST and Socket.IO service](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#rest-and-socketio-service) — `README.md`.
- [Install without DeepFace](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#install-without-deepface) — `README.md`.
- [Lockfile](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#lockfile) — `README.md`.
- [Development environment](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#development-environment) — `README.md`.
- [Model download and diagnostics](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#model-download-and-diagnostics) — `README.md`.
- [0.4.0 selectable lightweight VLM taggers](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#040-selectable-lightweight-vlm-taggers) — `README.md`.
- [Version notes (historical)](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#version-notes-historical) — `README.md`.
- [Metadata lookup cannot block downloads](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#metadata-lookup-cannot-block-downloads) — `README.md`.
- [0.1.5 model worker fix](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#015-model-worker-fix) — `README.md`.
- [0.1.6 true parallel filesystem discovery](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#016-true-parallel-filesystem-discovery) — `README.md`.
- [0.1.7 CUDA/runtime compatibility fix](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#017-cudaruntime-compatibility-fix) — `README.md`.
- [0.1.8 JoyCaption 4-bit SigLIP dtype repair](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#018-joycaption-4-bit-siglip-dtype-repair) — `README.md`.
- [0.1.9 media queue ordering by size](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#019-media-queue-ordering-by-size) — `README.md`.
- [0.1.10 continue after per-file JoyCaption failures](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#0110-continue-after-per-file-joycaption-failures) — `README.md`.
- [0.1.11 libmagic-gated media queue](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#0111-libmagic-gated-media-queue) — `README.md`.
- [0.1.11 content-based queue admission](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#0111-content-based-queue-admission) — `README.md`.
- [0.1.13 official JoyCaption NF4 loading path](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#0112-official-joycaption-nf4-loading-path) — `README.md`.
- [0.1.13 minimum JoyCaption file size](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#0113-minimum-joycaption-file-size) — `README.md`.
- [0.1.14 Transformers 5.x LLaVA component layout](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#0114-transformers-5x-llava-component-layout) — `README.md`.
- [0.1.15 low-VRAM loading and CPU offload](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#0115-low-vram-loading-and-cpu-offload) — `README.md`.
- [0.2.0 DeepFace identity pipeline and diverse video sampling](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#020-deepface-identity-pipeline-and-diverse-video-sampling) — `README.md`.
- [0.2.2 faster non-blocking video handling](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#022-faster-non-blocking-video-handling) — `README.md`.
- [0.2.3 DeepFace dependency preflight](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#023-deepface-dependency-preflight) — `README.md`.
- [0.2.4 TensorFlow/Keras DeepFace preflight](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#024-tensorflowkeras-deepface-preflight) — `README.md`.
- [0.2.5 stable DeepFace runtime](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#025-stable-deepface-runtime) — `README.md`.
- [0.3.0 uv-managed environment](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#030-uv-managed-environment) — `README.md`.
- [0.3.1 current uv installation path](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#031-current-uv-installation-path) — `README.md`.
- [0.4.1 robust DeepFace detector selection](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#041-robust-deepface-detector-selection) — `README.md`.
- [0.4.2 safe top-level gallery lifetime tracking](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#042-safe-top-level-gallery-lifetime-tracking) — `README.md`.
- [0.4.3 DeepFace legacy-Keras initialization](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#043-deepface-legacy-keras-initialization) — `README.md`.
- [0.4.4 FaceIdentity confirmation and detector fallback](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#044-faceidentity-confirmation-and-detector-fallback) — `README.md`.
- [0.5.0 cluster-level face attributes](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#050-cluster-level-face-attributes) — `README.md`.
- [0.6.0 responsive GUI, process-isolated clustering, and verbose worker logs](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#060-responsive-gui-process-isolated-clustering-and-verbose-worker-logs) — `README.md`.
- [0.6.1 LZ4 cleanup-warning filtering](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#061-lz4-cleanup-warning-filtering) — `README.md`.
- [0.6.2 explicit descending image queue](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#062-explicit-descending-image-queue) — `README.md`.
- [0.6.3 instant tag-cloud search](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#063-instant-tag-cloud-search) — `README.md`.
- [0.7.0 cumulative tag filtering inside galleries](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#070-cumulative-tag-filtering-inside-galleries) — `README.md`.
- [0.8.0 permanent analysis history and restart/resume](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#080-permanent-analysis-history-and-restartresume) — `README.md`.
- [0.8.1 reliable instant tag filtering](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#081-reliable-instant-tag-filtering) — `README.md`.
- [0.8.2 more tolerant person clustering](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#082-more-tolerant-person-clustering) — `README.md`.
- [0.8.4 thumbmoves extracted as reusable library](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#084-thumbmoves-extracted-as-reusable-library) — `README.md`.
- [0.8.5 ThumbMoves rename](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#085-thumbmoves-rename) — `README.md`.
- [Starting a scan from the command line](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#starting-a-scan-from-the-command-line) — `README.md`.
- [Notes on archive support](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#notes-on-archive-support) — `README.md`.
- [Safety / scale](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#safety--scale) — `README.md`.
- [0.8.3 operating-system thumbnail-cache reuse](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/README.md#083-operating-system-thumbnail-cache-reuse) — `README.md`.
- [PixelCue releases](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/RELEASING.md#pixelcue-releases) — `docs/RELEASING.md`.
- [Potential problems](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/RELEASING.md#potential-problems) — `docs/RELEASING.md`.
- [Visual analysis contract](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/visual-analysis.md#visual-analysis-contract) — `docs/visual-analysis.md`.
- [Measurement conditions](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/visual-analysis.md#measurement-conditions) — `docs/visual-analysis.md`.
- [Model receipts](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/visual-analysis.md#model-receipts) — `docs/visual-analysis.md`.
- [Comparison](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/visual-analysis.md#comparison) — `docs/visual-analysis.md`.
- [Potential problems](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/visual-analysis.md#potential-problems) — `docs/visual-analysis.md`.
- [Local temporal and batch APIs](https://github.com/kieransimkin/PixelCue/blob/v0.9.1/docs/visual-sequence.md#local-temporal-and-batch-apis) — `docs/visual-sequence.md`.

## Examples and media

Use the runnable examples and actual screenshots/videos linked from the released references. Keep their documented version/context and distinguish synthetic fixtures, model hypotheses and real captured output. Do not represent a guide link as proof that a model, GPU, physical phone or production host was tested. New decorative generated imagery adds no feature evidence to this reference index.
