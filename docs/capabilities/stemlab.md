# StemLab: capability and package reference

Audited 23 October 2026: **v1.11.0**, exact source [`f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0`](https://github.com/kieransimkin/stemlab/tree/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0). This is a dated source/documentation audit, not installed-runtime or end-to-end acceptance. [Check current releases before use](../workflows/release-preflight.md).

## Current README feature routes

- [Before every new workflow](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#before-every-new-workflow)
- [Find your route](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#find-your-route)
- [Synopsis](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#synopsis)
- [Install](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#install)
- [CLI](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#cli)
- [Output layout](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#output-layout)
- [Analysis performed](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#analysis-performed)
- [Curated default model set (September 2026)](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#curated-default-model-set-september-2026)
- [Speech transcription](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#speech-transcription)
- [Comprehensive sonic, harmonic, rhythmic and semantic analysis](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#comprehensive-sonic-harmonic-rhythmic-and-semantic-analysis)
- [Find DanceRudiments matching candidates from each stem](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#find-dancerudiments-matching-candidates-from-each-stem)
- [Measured Arcadians benchmark](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#measured-arcadians-benchmark)
- [BPM-synchronised recordings, harness and batch generation](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#bpm-synchronised-recordings-harness-and-batch-generation)
- [Export a master or stem as a signed waveform rudiment](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#export-a-master-or-stem-as-a-signed-waveform-rudiment)
- [Correct beats and export variable-tempo synchronisation](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#correct-beats-and-export-variable-tempo-synchronisation)
- [First-beat alignment and tempo families](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#first-beat-alignment-and-tempo-families)
- [Editable song timing: fixed/variable BPM, lyrics, words and cue sections](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#editable-song-timing-fixedvariable-bpm-lyrics-words-and-cue-sections)
- [Loop discovery and playback](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#loop-discovery-and-playback)
- [Recover a Short or video's source timing](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#recover-a-short-or-videos-source-timing)
- [Audio-to-MIDI model comparison](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#audio-to-midi-model-comparison)
- [Align timed musical cues to detected beats](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#align-timed-musical-cues-to-detected-beats)
- [Complementary evidence models](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#complementary-evidence-models)
- [Arcadians: complete analysis timeline and four movement demos](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#arcadians-complete-analysis-timeline-and-four-movement-demos)
- [Build and publish all five examples](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#build-and-publish-all-five-examples)
- [Export an existing analysis as a static timeline](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#export-an-existing-analysis-as-a-static-timeline)
- [Timeline analysis gallery](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#timeline-analysis-gallery)
- [1. Separation, spectrograms, beats and sections](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#1-separation-spectrograms-beats-and-sections)
- [2. Lyrics, speech regions and transcript QA](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#2-lyrics-speech-regions-and-transcript-qa)
- [3. Harmony, melody and song-map fusion](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#3-harmony-melody-and-song-map-fusion)
- [4. Sonic profile, rhythm regimes and semantics](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#4-sonic-profile-rhythm-regimes-and-semantics)
- [5. Where loops fit in](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#5-where-loops-fit-in)
- [Timeline overlays and movement display modes](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#timeline-overlays-and-movement-display-modes)
- [Web service](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#web-service)
- [Python API](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#python-api)
- [Codex plugin and MCP server](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#codex-plugin-and-mcp-server)
- [Codex skill](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#codex-skill)
- [DanceFlow and DanceMoves](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#danceflow-and-dancemoves)
- [Documentation](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#documentation)
- [External runtime/cache details](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#external-runtimecache-details)
- [Releases](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#releases)
- [Coordinated releases and latest-release dependencies](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#coordinated-releases-and-latest-release-dependencies)
- [Standalone Linux CLI release gate](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#standalone-linux-cli-release-gate)
- [Windows pytest temporary-directory permissions](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#windows-pytest-temporary-directory-permissions)
- [Reproducibility and licensing](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#reproducibility-and-licensing)
- [Arcadians timeline CI decoder and artifact checks](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#arcadians-timeline-ci-decoder-and-artifact-checks)
- [Separated-stem movement batches and controlled smoothing](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#separated-stem-movement-batches-and-controlled-smoothing)
- [Beat detection after separation: master and percussion hypotheses](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#beat-detection-after-separation-master-and-percussion-hypotheses)
- [Agents and contributors](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md#agents-and-contributors)

## Source documentation and examples

- [`README.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md)
- [`docs/ECOSYSTEM.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/ECOSYSTEM.md)
- [`docs/README.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/README.md)
- [`docs/arcadians-complete-analysis.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/arcadians-complete-analysis.md)
- [`docs/arcadians-release-demo.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/arcadians-release-demo.md)
- [`docs/arcadians-timeline.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/arcadians-timeline.md)
- [`docs/beat-inputs.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/beat-inputs.md)
- [`docs/beat-offsets.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/beat-offsets.md)
- [`docs/beat-timeline.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/beat-timeline.md)
- [`docs/beatnet.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/beatnet.md)
- [`docs/branding/README.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/branding/README.md)
- [`docs/clip-matching.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/clip-matching.md)
- [`docs/codex-plugin.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/codex-plugin.md)
- [`docs/codex-publishing.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/codex-publishing.md)
- [`docs/containers.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/containers.md)
- [`docs/cue-alignment.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/cue-alignment.md)
- [`docs/danceflow.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/danceflow.md)
- [`docs/evidence-models.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/evidence-models.md)
- [`docs/loop-validation.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/loop-validation.md)
- [`docs/loops.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/loops.md)
- [`docs/lyric-audition.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/lyric-audition.md)
- [`docs/midi.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/midi.md)
- [`docs/phrase-loops.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/phrase-loops.md)
- [`docs/publishing.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/publishing.md)
- [`docs/recording-pairs.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/recording-pairs.md)
- [`docs/released-viewers.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/released-viewers.md)
- [`docs/rudiment-recordings.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/rudiment-recordings.md)
- [`docs/rudiments.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/rudiments.md)
- [`docs/viewer-controls.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/viewer-controls.md)
- [`docs/web.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/web.md)
- [`docs/wordpress-beatnet-update-2026-10-01.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/docs/wordpress-beatnet-update-2026-10-01.md)
- [`examples/arcadians/README.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/examples/arcadians/README.md)
- [`examples/recordings/README.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/examples/recordings/README.md)
- [`examples/the-truth-is-a-virus/README.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/examples/the-truth-is-a-virus/README.md)

## Package evidence

- [`README.md`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/README.md) — SHA-256 `10ff259ce0f6340a65f6d11c028c52d64d1bb3127e50544c3355fffcc7e1a5ac`.
- [`pyproject.toml`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/pyproject.toml) — SHA-256 `e14a6826aa2d6476c650e326a526720a91e33d647e5d622b16ba1439c36e60d6`.
- [`package.json`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/package.json) — SHA-256 `4ae19e074b522e65f1e461b1635f4b91ca65aac4a6b3812b7b439f1d95bbcc1d`.
- [`MANIFEST.in`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/MANIFEST.in) — SHA-256 `6ef9c450dc2eb2c6226811b957163344029cb40f8dc6f6c5762c7d18df0be203`.
- [`LICENSE`](https://github.com/kieransimkin/stemlab/blob/f15f3d38c5e337e7ddd86d36878b61a99bf8f5b0/LICENSE) — SHA-256 `2cf0f6145baaa037c259c986f3fc2b7053b37fdbae9f48cec9875111c97c02b0`.

Package files were read at the pinned source. Published distributions, installed identity, working host examples, rights and reviewed output require their own verification.

## Historical detailed reference

The following older index is retained for detailed routes. Its earlier version is historical; the audited source links above identify current documented availability.

# stemlab: complete capability reference

Inspected stable source: [v1.8.0](https://github.com/kieransimkin/stemlab/releases/tag/v1.8.0), commit `589eeb1be9dab6a9e4596cfd089b1ef87d2dc2cc`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md).

## Choose and use a route

| Goal | Supported route and evidence |
|---|---|
| Choose saved evidence or new analysis | Reuse existing stems/reports first; inspect the analysis profile and exact model/runtime choices. Full analysis covers structure, harmony, sonic/rhythm evidence, lyrics and independent optional models. |
| Time and align the recording | Use the master plus saved drums/percussion detections, tempo-family/first-beat review and source-bound beat-offset/beat-timeline exports. Preserve detector evidence, signed fractional phase and exact source frames. |
| Record or match native motion | Export signed bipolar recordings, stem pairs/averages and 4–128 calibrated Fourier channels on the native 64-pip clock. Use saved evidence and the native candidate matcher before new movement choices. |
| Recover and edit words, lines and cues | Compare singing-preserving full-audio recovery with the speech-mask hypothesis. Preserve canonical wording, source clocks, locks, observed anchors and the independent 70-percent/listening requirements. Keep editable timing as separate revisions. |
| Inspect and select | Use the released shared timeline, editable timing lanes, waveform/spectrogram composites, overlays, sample-exact loops and source-clip matching. MIDI/model comparisons remain explicit optional analysis. |
| Use services and exports | Choose CLI, Python, local web/MCP or static exports deliberately. Keep five Arcadians pages and the frozen beat reference distinct from newly run inference. |

## Released reference coverage

Each entry links to the exact released explanation, options, example or limitation. These are documented capabilities, not a claim that every option was run on this computer. Review the relevant source before configuring it.

- [Agents and contributors](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#agents-and-contributors) — `README.md`.
- [Synopsis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#synopsis) — `README.md`.
- [DanceFlow and DanceMoves](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#danceflow-and-dancemoves) — `README.md`.
- [Curated default model set (September 2026)](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#curated-default-model-set-september-2026) — `README.md`.
- [Analysis performed](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#analysis-performed) — `README.md`.
- [Speech transcription](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#speech-transcription) — `README.md`.
- [Comprehensive sonic, harmonic, rhythmic and semantic analysis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#comprehensive-sonic-harmonic-rhythmic-and-semantic-analysis) — `README.md`.
- [Find DanceRudiments matching candidates from each stem](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#find-dancerudiments-matching-candidates-from-each-stem) — `README.md`.
- [Measured Arcadians benchmark](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#measured-arcadians-benchmark) — `README.md`.
- [BPM-synchronised recordings, harness and batch generation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#bpm-synchronised-recordings-harness-and-batch-generation) — `README.md`.
- [Export a master or stem as a signed waveform rudiment](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#export-a-master-or-stem-as-a-signed-waveform-rudiment) — `README.md`.
- [Correct beats and export variable-tempo synchronisation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#correct-beats-and-export-variable-tempo-synchronisation) — `README.md`.
- [First-beat alignment and tempo families](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#first-beat-alignment-and-tempo-families) — `README.md`.
- [Arcadians: complete analysis timeline and four movement demos](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#arcadians-complete-analysis-timeline-and-four-movement-demos) — `README.md`.
- [Build and publish all five examples](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#build-and-publish-all-five-examples) — `README.md`.
- [Export an existing analysis as a static timeline](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#export-an-existing-analysis-as-a-static-timeline) — `README.md`.
- [Timeline analysis gallery](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#timeline-analysis-gallery) — `README.md`.
- [1. Separation, spectrograms, beats and sections](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#1-separation-spectrograms-beats-and-sections) — `README.md`.
- [2. Lyrics, speech regions and transcript QA](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#2-lyrics-speech-regions-and-transcript-qa) — `README.md`.
- [3. Harmony, melody and song-map fusion](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#3-harmony-melody-and-song-map-fusion) — `README.md`.
- [4. Sonic profile, rhythm regimes and semantics](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#4-sonic-profile-rhythm-regimes-and-semantics) — `README.md`.
- [5. Where loops fit in](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#5-where-loops-fit-in) — `README.md`.
- [Loop discovery and playback](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#loop-discovery-and-playback) — `README.md`.
- [Recover a Short or video's source timing](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#recover-a-short-or-videos-source-timing) — `README.md`.
- [Audio-to-MIDI model comparison](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#audio-to-midi-model-comparison) — `README.md`.
- [Align timed musical cues to detected beats](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#align-timed-musical-cues-to-detected-beats) — `README.md`.
- [Complementary evidence models](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#complementary-evidence-models) — `README.md`.
- [Install](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#install) — `README.md`.
- [CLI](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#cli) — `README.md`.
- [Output layout](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#output-layout) — `README.md`.
- [Web service](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#web-service) — `README.md`.
- [Documentation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#documentation) — `README.md`.
- [Codex plugin and MCP server](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#codex-plugin-and-mcp-server) — `README.md`.
- [Codex skill](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#codex-skill) — `README.md`.
- [Python API](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#python-api) — `README.md`.
- [External runtime/cache details](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#external-runtimecache-details) — `README.md`.
- [Releases](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#releases) — `README.md`.
- [Reproducibility and licensing](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#reproducibility-and-licensing) — `README.md`.
- [Arcadians timeline CI decoder and artifact checks](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#arcadians-timeline-ci-decoder-and-artifact-checks) — `README.md`.
- [Separated-stem movement batches and controlled smoothing](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#separated-stem-movement-batches-and-controlled-smoothing) — `README.md`.
- [Beat detection after separation: master and percussion hypotheses](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#beat-detection-after-separation-master-and-percussion-hypotheses) — `README.md`.
- [Timeline overlays and movement display modes](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#timeline-overlays-and-movement-display-modes) — `README.md`.
- [Coordinated releases and latest-release dependencies](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#coordinated-releases-and-latest-release-dependencies) — `README.md`.
- [Standalone Linux CLI release gate](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#standalone-linux-cli-release-gate) — `README.md`.
- [Editable song timing: fixed/variable BPM, lyrics, words and cue sections](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#editable-song-timing-fixedvariable-bpm-lyrics-words-and-cue-sections) — `README.md`.
- [Windows pytest temporary-directory permissions](https://github.com/kieransimkin/stemlab/blob/v1.8.0/README.md#windows-pytest-temporary-directory-permissions) — `README.md`.
- [Arcadians release demos and GitHub Pages](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#arcadians-release-demos-and-github-pages) — `docs/arcadians-release-demo.md`.
- [Hearing and viewing the demo](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#hearing-and-viewing-the-demo) — `docs/arcadians-release-demo.md`.
- [Batch recipe](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#batch-recipe) — `docs/arcadians-release-demo.md`.
- [Release workflow](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#release-workflow) — `docs/arcadians-release-demo.md`.
- [Audio-seeking regression and failure evidence](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#audio-seeking-regression-and-failure-evidence) — `docs/arcadians-release-demo.md`.
- [Publish an already-tested demo now](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#publish-an-already-tested-demo-now) — `docs/arcadians-release-demo.md`.
- [One-time Pages setup](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#one-time-pages-setup) — `docs/arcadians-release-demo.md`.
- [Reproduce the movement builder locally](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#reproduce-the-movement-builder-locally) — `docs/arcadians-release-demo.md`.
- [Additional stem-pair and amplitude-mode galleries](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#additional-stem-pair-and-amplitude-mode-galleries) — `docs/arcadians-release-demo.md`.
- [Full-master Fourier page](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-release-demo.md#full-master-fourier-page) — `docs/arcadians-release-demo.md`.
- [Complete Arcadians timeline on GitHub Pages](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#complete-arcadians-timeline-on-github-pages) — `docs/arcadians-timeline.md`.
- [What “complete” means](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#what-complete-means) — `docs/arcadians-timeline.md`.
- [Run and publish](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#run-and-publish) — `docs/arcadians-timeline.md`.
- [Runtime and artifacts](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#runtime-and-artifacts) — `docs/arcadians-timeline.md`.
- [Export any existing StemLab analysis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#export-any-existing-stemlab-analysis) — `docs/arcadians-timeline.md`.
- [Browser implementation and QA scope](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#browser-implementation-and-qa-scope) — `docs/arcadians-timeline.md`.
- [Decoder preflight and CI output ownership](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#decoder-preflight-and-ci-output-ownership) — `docs/arcadians-timeline.md`.
- [Late lyric-semantic import failure](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#late-lyric-semantic-import-failure) — `docs/arcadians-timeline.md`.
- [Core v2 and reuse of the separated stems](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/arcadians-timeline.md#core-v2-and-reuse-of-the-separated-stems) — `docs/arcadians-timeline.md`.
- [Master and percussion beat analysis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-inputs.md#master-and-percussion-beat-analysis) — `docs/beat-inputs.md`.
- [Outputs and attribution](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-inputs.md#outputs-and-attribution) — `docs/beat-inputs.md`.
- [Consensus and failures](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-inputs.md#consensus-and-failures) — `docs/beat-inputs.md`.
- [First-beat pip offsets and tempo interpretations](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-offsets.md#first-beat-pip-offsets-and-tempo-interpretations) — `docs/beat-offsets.md`.
- [Two complementary real-song examples](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-offsets.md#two-complementary-real-song-examples) — `docs/beat-offsets.md`.
- [Keep the two clocks separate](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-offsets.md#keep-the-two-clocks-separate) — `docs/beat-offsets.md`.
- [Editable nonuniform beat correction](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-offsets.md#editable-nonuniform-beat-correction) — `docs/beat-offsets.md`.
- [Editable variable-tempo beat timeline and DanceMoves handoff](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-timeline.md#editable-variable-tempo-beat-timeline-and-dancemoves-handoff) — `docs/beat-timeline.md`.
- [Browser editing](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-timeline.md#browser-editing) — `docs/beat-timeline.md`.
- [Single JSON value](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-timeline.md#single-json-value) — `docs/beat-timeline.md`.
- [DanceMoves fixed and variable tempo handoff](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-timeline.md#dancemoves-fixed-and-variable-tempo-handoff) — `docs/beat-timeline.md`.
- [Developer checks](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-timeline.md#developer-checks) — `docs/beat-timeline.md`.
- [Editable song timing: fixed/variable BPM, lyrics, words and cue sections](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beat-timeline.md#editable-song-timing-fixedvariable-bpm-lyrics-words-and-cue-sections) — `docs/beat-timeline.md`.
- [BeatNet compatibility](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beatnet.md#beatnet-compatibility) — `docs/beatnet.md`.
- [Current StemLab route](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beatnet.md#current-stemlab-route) — `docs/beatnet.md`.
- [Verified result](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beatnet.md#verified-result) — `docs/beatnet.md`.
- [Upstream proposal](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beatnet.md#upstream-proposal) — `docs/beatnet.md`.
- [Potential problems](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beatnet.md#potential-problems) — `docs/beatnet.md`.
- [Resolver says BeatNet and madmom-prebuilt are incompatible](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beatnet.md#resolver-says-beatnet-and-madmom-prebuilt-are-incompatible) — `docs/beatnet.md`.
- [Blogworthiness assessment](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/beatnet.md#blogworthiness-assessment) — `docs/beatnet.md`.
- [Recover an excerpt's source clock](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/clip-matching.md#recover-an-excerpts-source-clock) — `docs/clip-matching.md`.
- [Reproducible synthetic example](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/clip-matching.md#reproducible-synthetic-example) — `docs/clip-matching.md`.
- [StemLab Codex plugin](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#stemlab-codex-plugin) — `docs/codex-plugin.md`.
- [Install from the patched repository](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#install-from-the-patched-repository) — `docs/codex-plugin.md`.
- [Install the plugin in Codex](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#install-the-plugin-in-codex) — `docs/codex-plugin.md`.
- [Direct MCP connection](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#direct-mcp-connection) — `docs/codex-plugin.md`.
- [Tools](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#tools) — `docs/codex-plugin.md`.
- [Example: a music bed for a Shorts video](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#example-a-music-bed-for-a-shorts-video) — `docs/codex-plugin.md`.
- [Preferred inspection: existing React timeline](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#preferred-inspection-existing-react-timeline) — `docs/codex-plugin.md`.
- [Job lifecycle and limits](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#job-lifecycle-and-limits) — `docs/codex-plugin.md`.
- [Security and privacy](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#security-and-privacy) — `docs/codex-plugin.md`.
- [Build, test and distribution](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#build-test-and-distribution) — `docs/codex-plugin.md`.
- [Reference specifications (checked 29 September 2026)](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-plugin.md#reference-specifications-checked-29-september-2026) — `docs/codex-plugin.md`.
- [Codex and MCP distribution](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#codex-and-mcp-distribution) — `docs/codex-publishing.md`.
- [Release automation included in this patch](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#release-automation-included-in-this-patch) — `docs/codex-publishing.md`.
- [OpenAI public Plugins Directory](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#openai-public-plugins-directory) — `docs/codex-publishing.md`.
- [Official MCP Registry: prepared, disabled by default](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#official-mcp-registry-prepared-disabled-by-default) — `docs/codex-publishing.md`.
- [Other directories](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#other-directories) — `docs/codex-publishing.md`.
- [Local validation and honest limits](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#local-validation-and-honest-limits) — `docs/codex-publishing.md`.
- [Sources checked 29 September 2026](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#sources-checked-29-september-2026) — `docs/codex-publishing.md`.
- [Potential problems](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#potential-problems) — `docs/codex-publishing.md`.
- [MCP Registry description length](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/codex-publishing.md#mcp-registry-description-length) — `docs/codex-publishing.md`.
- [StemLab containers](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/containers.md#stemlab-containers) — `docs/containers.md`.
- [GitHub Container Registry](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/containers.md#github-container-registry) — `docs/containers.md`.
- [Docker Hub](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/containers.md#docker-hub) — `docs/containers.md`.
- [Reproducibility](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/containers.md#reproducibility) — `docs/containers.md`.
- [Snap timed cues to detected beats](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/cue-alignment.md#snap-timed-cues-to-detected-beats) — `docs/cue-alignment.md`.
- [Reuse saved analysis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/cue-alignment.md#reuse-saved-analysis) — `docs/cue-alignment.md`.
- [Highlight cues without a nearby beat](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/cue-alignment.md#highlight-cues-without-a-nearby-beat) — `docs/cue-alignment.md`.
- [Precision: exact beats versus LRC player compatibility](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/cue-alignment.md#precision-exact-beats-versus-lrc-player-compatibility) — `docs/cue-alignment.md`.
- [Files written](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/cue-alignment.md#files-written) — `docs/cue-alignment.md`.
- [Add cue alignment to a new analysis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/cue-alignment.md#add-cue-alignment-to-a-new-analysis) — `docs/cue-alignment.md`.
- [Verification](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/cue-alignment.md#verification) — `docs/cue-alignment.md`.
- [StemLab in the DanceFlow workflow](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/danceflow.md#stemlab-in-the-danceflow-workflow) — `docs/danceflow.md`.
- [Complementary evidence models](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#complementary-evidence-models) — `docs/evidence-models.md`.
- [Models](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#models) — `docs/evidence-models.md`.
- [Inspect availability](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#inspect-availability) — `docs/evidence-models.md`.
- [Reuse an existing analysis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#reuse-an-existing-analysis) — `docs/evidence-models.md`.
- [New analyses](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#new-analyses) — `docs/evidence-models.md`.
- [Interpretation rules](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#interpretation-rules) — `docs/evidence-models.md`.
- [Downloads and trust](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#downloads-and-trust) — `docs/evidence-models.md`.
- [SongFormer bridge](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#songformer-bridge) — `docs/evidence-models.md`.
- [Evaluation corpus](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#evaluation-corpus) — `docs/evidence-models.md`.
- [Experimental third-group bridges](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/evidence-models.md#experimental-third-group-bridges) — `docs/evidence-models.md`.
- [Loop feature validation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loop-validation.md#loop-feature-validation) — `docs/loop-validation.md`.
- [Baselines](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loop-validation.md#baselines) — `docs/loop-validation.md`.
- [Checks executed](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loop-validation.md#checks-executed) — `docs/loop-validation.md`.
- [Build and coverage limits](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loop-validation.md#build-and-coverage-limits) — `docs/loop-validation.md`.
- [Discover, audition and export loops](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#discover-audition-and-export-loops) — `docs/loops.md`.
- [Quick start](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#quick-start) — `docs/loops.md`.
- [Exploratory cut-point search](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#exploratory-cut-point-search) — `docs/loops.md`.
- [Workflow in the existing analysis frontend](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#workflow-in-the-existing-analysis-frontend) — `docs/loops.md`.
- [1. Inspect the discovered regions](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#1-inspect-the-discovered-regions) — `docs/loops.md`.
- [2. Select and enable a loop](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#2-select-and-enable-a-loop) — `docs/loops.md`.
- [3. Inspect boundaries and export status](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#3-inspect-boundaries-and-export-status) — `docs/loops.md`.
- [Outputs and indexing](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#outputs-and-indexing) — `docs/loops.md`.
- [Candidate selection and safeguards](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#candidate-selection-and-safeguards) — `docs/loops.md`.
- [Limitations and tuning](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#limitations-and-tuning) — `docs/loops.md`.
- [Rebuild the component/frontend pair](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#rebuild-the-componentfrontend-pair) — `docs/loops.md`.
- [Reproduce the workflow and tests](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/loops.md#reproduce-the-workflow-and-tests) — `docs/loops.md`.
- [Audio-to-MIDI extraction](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#audio-to-midi-extraction) — `docs/midi.md`.
- [Models and appropriate inputs](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#models-and-appropriate-inputs) — `docs/midi.md`.
- [Install only the backends needed](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#install-only-the-backends-needed) — `docs/midi.md`.
- [Transcribe one audio file](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#transcribe-one-audio-file) — `docs/midi.md`.
- [Reuse existing StemLab results](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#reuse-existing-stemlab-results) — `docs/midi.md`.
- [Include MIDI in a new full analysis](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#include-midi-in-a-new-full-analysis) — `docs/midi.md`.
- [Isolate conflicting model environments](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#isolate-conflicting-model-environments) — `docs/midi.md`.
- [Checkpoint downloads, caching and trust](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#checkpoint-downloads-caching-and-trust) — `docs/midi.md`.
- [Outputs and timing conventions](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#outputs-and-timing-conventions) — `docs/midi.md`.
- [Codex integration](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#codex-integration) — `docs/midi.md`.
- [Validation and real-model smoke tests](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#validation-and-real-model-smoke-tests) — `docs/midi.md`.
- [Upstream references and licence boundaries](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/midi.md#upstream-references-and-licence-boundaries) — `docs/midi.md`.
- [Phrase loops and musical restarts](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/phrase-loops.md#phrase-loops-and-musical-restarts) — `docs/phrase-loops.md`.
- [What changes the ranking](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/phrase-loops.md#what-changes-the-ranking) — `docs/phrase-loops.md`.
- [Explicit artist feedback](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/phrase-loops.md#explicit-artist-feedback) — `docs/phrase-loops.md`.
- [Evidence and limitations](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/phrase-loops.md#evidence-and-limitations) — `docs/phrase-loops.md`.
- [Publishing StemLab](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#publishing-stemlab) — `docs/publishing.md`.
- [Destinations](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#destinations) — `docs/publishing.md`.
- [One-time PyPI Trusted Publisher setup](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#one-time-pypi-trusted-publisher-setup) — `docs/publishing.md`.
- [GitHub environment](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#github-environment) — `docs/publishing.md`.
- [Releasing StemLab 1.0.0](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#releasing-stemlab-100) — `docs/publishing.md`.
- [Manual workflow runs](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#manual-workflow-runs) — `docs/publishing.md`.
- [Public attribution](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#public-attribution) — `docs/publishing.md`.
- [Required one-file CLI](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/publishing.md#required-one-file-cli) — `docs/publishing.md`.
- [StemLab documentation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/README.md#stemlab-documentation) — `docs/README.md`.
- [Stem pairs and amplitude-mode comparisons](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/recording-pairs.md#stem-pairs-and-amplitude-mode-comparisons) — `docs/recording-pairs.md`.
- [Separate once, pair different stems](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/recording-pairs.md#separate-once-pair-different-stems) — `docs/recording-pairs.md`.
- [Peak, average and moving average are different modes](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/recording-pairs.md#peak-average-and-moving-average-are-different-modes) — `docs/recording-pairs.md`.
- [Controlled comparison batch](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/recording-pairs.md#controlled-comparison-batch) — `docs/recording-pairs.md`.
- [Four Arcadians Pages examples](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/recording-pairs.md#four-arcadians-pages-examples) — `docs/recording-pairs.md`.
- [Reproducible synthetic example](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/recording-pairs.md#reproducible-synthetic-example) — `docs/recording-pairs.md`.
- [Coordinated released-viewer workflow](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#coordinated-released-viewer-workflow) — `docs/released-viewers.md`.
- [Checkout layout and command](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#checkout-layout-and-command) — `docs/released-viewers.md`.
- [Release order and version selection](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#release-order-and-version-selection) — `docs/released-viewers.md`.
- [Latest stable releases, with an auditable build snapshot](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#latest-stable-releases-with-an-auditable-build-snapshot) — `docs/released-viewers.md`.
- [What must be committed together in StemLab](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#what-must-be-committed-together-in-stemlab) — `docs/released-viewers.md`.
- [Publication and Pages verification](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#publication-and-pages-verification) — `docs/released-viewers.md`.
- [Interrupted runs and failures](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#interrupted-runs-and-failures) — `docs/released-viewers.md`.
- [Source of truth](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#source-of-truth) — `docs/released-viewers.md`.
- [This repository's role](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/released-viewers.md#this-repositorys-role) — `docs/released-viewers.md`.
- [BPM-synchronised recordings, visualizer and batch generation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#bpm-synchronised-recordings-visualizer-and-batch-generation) — `docs/rudiment-recordings.md`.
- [Install both companion updates](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#install-both-companion-updates) — `docs/rudiment-recordings.md`.
- [BPM and beat phase](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#bpm-and-beat-phase) — `docs/rudiment-recordings.md`.
- [Fourier frequency bands to N dimensions](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#fourier-frequency-bands-to-n-dimensions) — `docs/rudiment-recordings.md`.
- [Fourier resolution problems](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#fourier-resolution-problems) — `docs/rudiment-recordings.md`.
- [Signed waveform resampling](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#signed-waveform-resampling) — `docs/rudiment-recordings.md`.
- [Single recording: bass on X, treble on Y](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#single-recording-bass-on-x-treble-on-y) — `docs/rudiment-recordings.md`.
- [Independently route any number of dimensions](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#independently-route-any-number-of-dimensions) — `docs/rudiment-recordings.md`.
- [Window and filter semantics](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#window-and-filter-semantics) — `docs/rudiment-recordings.md`.
- [Generate a varied batch and comparison page](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#generate-a-varied-batch-and-comparison-page) — `docs/rudiment-recordings.md`.
- [The existing DanceRudiments visualizer, not a lookalike](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#the-existing-dancerudiments-visualizer-not-a-lookalike) — `docs/rudiment-recordings.md`.
- [Reproducible demo and validation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#reproducible-demo-and-validation) — `docs/rudiment-recordings.md`.
- [Arcadians release publication](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiment-recordings.md#arcadians-release-publication) — `docs/rudiment-recordings.md`.
- [DanceRudiments matching — audio stem peaks → candidate motion patterns](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiments.md#dancerudiments-matching--audio-stem-peaks--candidate-motion-patterns) — `docs/rudiments.md`.
- [Interpretation and methodology](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiments.md#interpretation-and-methodology) — `docs/rudiments.md`.
- [Outputs](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiments.md#outputs) — `docs/rudiments.md`.
- [Arcadians reproducible validation](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiments.md#arcadians-reproducible-validation) — `docs/rudiments.md`.
- [Native GitHub Actions gate](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiments.md#native-github-actions-gate) — `docs/rudiments.md`.
- [Licensing / caveats](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/rudiments.md#licensing--caveats) — `docs/rudiments.md`.
- [Shared viewer display controls](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#shared-viewer-display-controls) — `docs/viewer-controls.md`.
- [Timeline: one audio channel, two aligned layers](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#timeline-one-audio-channel-two-aligned-layers) — `docs/viewer-controls.md`.
- [DanceRudiments: X–Y or per-dimension bars](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#dancerudiments-xy-or-per-dimension-bars) — `docs/viewer-controls.md`.
- [Beat analysis includes BOTH source types](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#beat-analysis-includes-both-source-types) — `docs/viewer-controls.md`.
- [Install the released shared APIs](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#install-the-released-shared-apis) — `docs/viewer-controls.md`.
- [Relative source-bundle handoff correction](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#relative-source-bundle-handoff-correction) — `docs/viewer-controls.md`.
- [Sample-exact loop regression](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#sample-exact-loop-regression) — `docs/viewer-controls.md`.
- [Editable nonuniform beat correction](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/viewer-controls.md#editable-nonuniform-beat-correction) — `docs/viewer-controls.md`.
- [StemLab web service](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/web.md#stemlab-web-service) — `docs/web.md`.
- [Windows](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/web.md#windows) — `docs/web.md`.
- [Linux](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/web.md#linux) — `docs/web.md`.
- [Docker Compose](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/web.md#docker-compose) — `docs/web.md`.
- [HTTP / Socket.IO service](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/web.md#http--socketio-service) — `docs/web.md`.
- [WordPress update: BeatNet on current Python](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/wordpress-beatnet-update-2026-10-01.md#wordpress-update-beatnet-on-current-python) — `docs/wordpress-beatnet-update-2026-10-01.md`.
- [Exact WordPress block source](https://github.com/kieransimkin/stemlab/blob/v1.8.0/docs/wordpress-beatnet-update-2026-10-01.md#exact-wordpress-block-source) — `docs/wordpress-beatnet-update-2026-10-01.md`.

## Examples and media

Use the runnable examples and actual screenshots/videos linked from the released references. Keep their documented version/context and distinguish synthetic fixtures, model hypotheses and real captured output. Do not represent a guide link as proof that a model, GPU, physical phone or production host was tested. New decorative generated imagery adds no feature evidence to this reference index.

## Default-branch availability

The official default branch was also inspected at [`ffb903eeeaea3f45b77c7dc0743ac785bb478593`](https://github.com/kieransimkin/stemlab/tree/ffb903eeeaea3f45b77c7dc0743ac785bb478593). It differs from the audited stable tag. [Read that exact README](https://github.com/kieransimkin/stemlab/blob/ffb903eeeaea3f45b77c7dc0743ac785bb478593/README.md) for later source/documentation work; this does not establish a newer release, registry version or installed runtime.
