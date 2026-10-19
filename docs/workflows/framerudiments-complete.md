# Use the full FrameRudiments compositor

Read the [release preflight](release-preflight.md) before every new run. The baseline for this guide is the inspected FrameRudiments **0.4.1** release, not a promise that the version will stay latest. Use the [indexed released references](../capabilities/framerudiments.md) for exact option names and every documented feature. Keep music analysis in StemLab, native movement in DanceRudiments, web playback in DanceMoves and timeline mechanics in React Timeline Sequence.

## Choose inputs and clocks first

Hash the authorised source audio, artwork, fonts, lyrics, cues and recordings. Reuse saved StemLab analyses. Accepted `stemlab.loops.v1` IDs can supply sample-exact clip bounds; exploratory cuts need independent review. A native `dancerudiments.recording` is bounded captured data, not a looping procedural pattern. A calibrated Fourier recording is required for spectral displays; generic motion values are not spectrum measurements.

Keep three clocks explicit: source audio time, output excerpt/repeat time, and rhythmic phase. A fixed BPM, fractional `clock.beat_alignment`, or source-bound `clock.beat_timeline` may drive procedural movement. The variable-tempo route accepts `stemlab.beat-timeline.v1` with exact sample-frame anchors. Do not retime audio, LRC/CUE timestamps or recorded Rudiments to make a beat map fit. Native beats have 64 pips; DanceMoves ticks have 16 subdivisions per beat.

## Select the feature route

| Need | Configuration or maintained entry point | Required evidence and useful limits |
|---|---|---|
| Excerpts, repeats and endpoint fades | Project audio source sample intervals, repeats and `audio.fade_seconds` | Retain start-inclusive/end-exclusive samples; default short edits have .12-second quarter-sine fades; visualiser/Canvas defaults differ. No source remix/stretch is implied. |
| Canonical line and word lyrics | `lyrics`, pinned `word_lyrics`, `word_captions`; enhanced LRC | One frame ledger supplies painted transitions and line/word SRT/ASS. Preserve canonical words, clears, carry-in and repeat boundaries. |
| Rich text and active-word markers | Caption/title `font`, `effects`, `word_indicator` | Font hashes, stroke/bevel/emboss/gradient/glow/shadow, word-following native sprite and independent particle windows. Check final processed glyphs and phone crops. |
| Native procedural or saved motion | named/table/composite/matched `motion`, or bounded recording | Select actual axes and match windows. Native sampling stays in DanceRudiments; extrapolation/interpolation require explicit choices. |
| Modular renderer catalogue | `renderers`; layer `type: "rudiment"`, stable `renderer` name | Particles/trails, bipolar bars, waveform histories, XY/phase paths, calibrated spectral/peak views and their complete catalogue. Select a view, not another analysis engine. |
| Native rangoli petals | `renderer: "rangoli"`; `demo --rangoli` | Independent native scale/rotation/lift axes, transparent fills, stroke/halo bounds and optional glow. The released texture-free projectM background uses existing routing; preserve clean petal/lyric overlays and review the final encoded frame. |
| Annular views and style modulation | Circular spectra/spectrogram/waveform renderer names and native `style.*` modulation | Frequency geometry is presentation of the existing calibrated bands. Colour gradients and the native modulation lab have separate examples. |
| Image-backed views | `sprites`; 52 sprite/atlas renderer modes and pinned assets | Preserve atlas grid, hash, alpha, axis semantics, source clock and transformed bounds. Arbitrary private art is never silently substituted. |
| Spatial views | Wire, `spatial-solid-*` and `spatial-music-*` torus/sphere/terrain | CPU depth/lighting/fog; optional ModernGL shadows/volumetrics; calibrated FFT-history terrain. CPU and GPU acceptance remain separate. |
| Multiple stem drivers | `stem_sources` aliases and `stem_blend` | Pin each native recording. Weighted blends require matching dimension names and reject calibrated spectral views; never average motion values and call them FFT. |
| Track mattes | `layer_masks` with earlier layer/background alpha or luminance, invert and keyframed opacity | Prior-surface ordering prevents cycles. Missing masks stay transparent before inversion. Keyframes use output seconds. |
| Layer motion, clips and displacement | `layer_animations`, normalized envelopes, fixed/animated polygon `clip`, `layer_displacement` | Finite validated property ranges; equal polygon vertex counts; earlier displacement source. Presentation does not rewrite analysis or captured movement. |
| Smoke, sparks and weather | `type: "emitter"`, continuous/cue/hybrid modes, pinned optional particle PNG | Native motion and numeric style modulation. Verify cue-triggered bursts, transformed region and maximum extent. |
| Scoped or final post effects | Per-element post passes and frame effects | Streaks, blur, glow, colour/geometry effects and expanded spectrum/waveform families use the existing compositor. Check the complete effect catalogue and strict style schema. |
| Feedback GPU visualisers | Butterchurn/projectM, pinned runtime/preset/library identities | Sequential feedback must replay all preceding frames. Install only the required runtime and authorised preset packs; preserve upstream licences and GPU limitations. |
| Choose what enters feedback | `visualiser_routing` feed windows/final overlays; `visualiser_stage_injections` before selected effect stages | Layer, lyric, word sprite, emitter and background routing remain independent. A clean final overlay can preserve legibility. |
| Render quality | `render_quality`, spatial scale 1–4, temporal samples 1–8, final AA | Default maximum quality is expensive. Record explicit preview reductions; full-quality final rendering and encoded QA remain required. |
| Release-owned scene design | Trusted Python scene hook/renderer registry | Reuse the shared frame loop, encoder, clocks and native samplers. Keep artwork/layout decisions in adapters; add reusable mechanics to FrameRudiments. |
| Author with a timeline | `authoring/`, `scripts/authoring_preview.py`, released React Timeline Sequence | LRC/word/cue/layer lanes, shared tempo grid, draggable keys, routing graph/presets, undo/redo, PNG preview and export-only drafts. Preview does not replay feedback effects and never edits canonical files. |
| Inspect the atlas | Visualisation Atlas, complete coverage matrix and public gallery | Distinguish exact renderer identity, input class and actual tested variants. A gallery frame does not establish all GPUs or all parameter combinations. |
| Profile preset response | `presets-install`, `presets-profile`, `scripts/profile_visualisers.py` | Cover/lyric/static-card conditions crossed with programme/silence, exact frame/sample clocks, preset hashes, resume and failed/untested receipts. |
| Controlled audio probes | `Run-ControlledPresetAnalysis.ps1`, `scripts/controlled_preset_analysis.py` | Deterministic tone/noise/silence inputs and sample clocks describe renderer response only. Keep StemLab as music-analysis owner; retain probe/config/runtime hashes and unavailable cases. |
| Efficient temporal descriptions | `Run-PresetBehaviourAnalysis.ps1`, coordinated `analysis-releases.json` | Measure dense frames first; select bounded nonblank representative frames for explicit cached models. `-DescribeExisting` reuses evidence without inference. Semantic budget 0 is measurement-only. |
| Legacy full analysis | `Run-FullPresetAnalysis.ps1`, explicit `-Limit`, `-UpgradeCoverage`, ordering seed | Preserve earlier results and coverage protocol. Use bounded pilots; a complete catalogue run is a separate resource decision, not routine preflight. |
| Windows projectM loading | `scripts/ensure_projectm_runtime.py` | Matching compiler/runtime provenance, checked transitive DLLs and fresh-process load receipt under project-local models/runtimes. No global PATH change or arbitrary DLL source. |

## Run a small real example

Use the actual installed Python/launcher and a selected local font. The built-in fixture creates synthetic audio, a sprite, line/cue timing and a four-dimensional recording. It does not expose private songs or download neural weights.

```sh
framerudiments --version
framerudiments renderers
framerudiments sprites
framerudiments visualisers
framerudiments demo runs/new-demo --rudiments --font /path/to/font.ttf
framerudiments plan runs/new-demo/project.json --output runs/new-plan.json
framerudiments preflight runs/new-demo/project.json --output runs/new-preflight --ffmpeg /path/to/ffmpeg
framerudiments render runs/new-demo/project.json --output runs/new-render --ffmpeg /path/to/ffmpeg
```

For spectral fixtures, `demo --spectrum` explicitly needs the supported StemLab runtime. For actual work use a pinned source project; do not replace approved art or masters with the fixture. Every output directory is new. The planning/preflight/render chain validates the project, hashes, timing and encoded technical output; visual review and attended listening are separate.

## Author and preview safely

From the matching release checkout, install the frontend's exact dependencies, then use `scripts/authoring_preview.py PROJECT --port PORT`. Keep the server on loopback. The released shared timeline supplies playhead, zoom, loops and timing edits; do not draw an imitation. Layer keys, style presets and the routing graph produce exportable draft changes. Preserve source assets and import the exported patch deliberately. Fast preview is 1×/1-sample; sequential feedback is absent from the interactive PNG preview. Approve feedback through a real sequential encoded render.

![Actual synthetic original/aligned clock composition](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.4.1/docs/media/beat-alignment.png)

[Play the synthetic example](https://github.com/kieransimkin/FrameRudiments/blob/v0.4.1/docs/media/beat-alignment.mp4). The right-hand motion uses the explicit phase correction; source-timed text and recorded bands retain their clock. This is a reproducible software example, not musical approval.

[Browse the renderer gallery](https://kieransimkin.github.io/FrameRudiments/) and its linked timing, rich-lyrics, particles and routing examples. These are actual bounded synthetic examples; retain controls and their captions. An illustration adds no evidence where the native rendered example already explains the feature.

## Verify the final output and improve the owner

Inspect decoded frame zero, every lyric/scene state, adjacent cue frames, motion extrema, loop seams, phone crops and the ending. Check final effect output rather than only pre-effect layer bounds. Retain source/software/preset/font/render hashes, frame ledgers, CFR/decode/alpha bounds and listening state. Respect reduced-motion/flash and intermittent-effect region rules appropriate to the delivery surface. An offline render is not an upload, schedule, publication or website save.

Keep weights and model-specific caches in the owning project's ignored `models/`. Use cached models and saved reports first. Do not run face processing, full-library inference or paid sources because a feature list exists. Implement a demonstrated reusable renderer/composition/evidence improvement in FrameRudiments; improve analysis in StemLab/PixelCue, reporting in PrismMoves, movement in DanceRudiments and the actual timeline in its own repository.

## Potential problems

- **The CLI wheel lacks authoring or analysis helper scripts.** Use the verified matching source distribution/checkout for `scripts/` and `authoring/`; the universal wheel supplies the portable renderer. A loaded wheel alone does not establish the frontend or native GPU runtime.
- **New renderer names are missing.** Inspect the actual imported package and catalogue, not an older source tree or directory label. Install the current verified stable release and retain the prior package for rollback.
- **Text fits before feedback but becomes unreadable afterwards.** Inspect encoded frames; use deliberate clean final overlays/routing where the visual brief calls for it. Do not claim pre-effect bounds prove final legibility.
- **Variable tempo alters lyrics or a recording drifts.** Check source/excerpt/output/phase mapping. Only procedural motion follows corrected phase; source audio, lyrics/cues and captured native recordings retain their original clocks.
- **Semantic captions describe rotation from a still image.** Use PixelCue temporal measurements plus PrismMoves' bounded representative-frame route. Sparse/failed evidence stays limited; model language is a hypothesis.
- **A prototype appears only on main.** Keep it explicitly developmental. The release baseline above includes authoring/compositing guides but does not include the later controlled-audio-response prototype; verify its own subsequent release before using it as a stable route.
