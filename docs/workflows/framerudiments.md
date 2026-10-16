# Render with FrameRudiments

Use [FrameRudiments](https://github.com/kieransimkin/FrameRudiments) for reusable
offline Shorts and lyric-visualiser rendering. Keep analysis in StemLab,
movement/recording playback in DanceRudiments and live web/WordPress motion in
DanceMoves. Preserve a historical generator when reproducing an approved film.

1. Identify and hash the exact authorised programme, canonical timing, artwork
   and font. Retain privacy, source rights, BPM/phase status, source sample rate
   and start-inclusive/end-exclusive bounds. Never infer canonicity from presence.
2. Reuse saved StemLab evidence. `stemlab.loops.v1` accepted-loop IDs can supply
   exact bounds; exploratory phrase candidates remain separate artist-reviewed
   explicit sample intervals. Pin any beat report, match report or N-D recording.
   Choose the exact source/match/window/projection; no automatic creative approval.
3. Build `framerudiments.project.v1` with release-specific appearance. Use native
   named/table/composite/matched routes or recording files; keep original source
   offsets and recording capture limits. One beat is 64 native pips or 16 ticks.
   Pin scene-hook inputs too. New reusable mechanics belong in the package.
4. Run `plan`, then `preflight`, then `render` into distinct new directories.
   Read the single caption/cue frame ledger and signed quantisation errors.
   Check `audio.fade_seconds`: short derivatives default to .12 qsin; an approved
   raw seam uses 0, and visualisers/Canvas default to 0. The master stays unchanged.
5. Inspect encoded frame zero, every distinct lyric/scene state, adjacent cue
   frames, representative motion and the ending at native and phone sizes.
   Check official destination overlays/actual upload preview separately; a text
   rectangle does not establish platform safety. Listen to the encoded programme
   and repeated seam. Keep technical, creative and listening states distinct.
6. Retain exact source/render/manifest hashes, software identity, command/log,
   caption ledger, alpha bounds, full decode and CFR evidence. Publication and
   EPK reconciliation remain later actions under their own authorised workflows.

Portable CLI examples (replace paths with pinned authorised inputs):

```sh
framerudiments plan release/project.json --output release/plan.json
framerudiments preflight release/project.json --output release/preflight --ffmpeg /path/ffmpeg
framerudiments render release/project.json --output release/render --ffmpeg /path/ffmpeg
```

Use a trusted Python scene hook only for release-owned drawing. It receives the
shared frame/source/output/beat/lyric/cue context; do not add another scheduler,
native sampler or encoder. Validate its custom bounds, occlusion and collisions.
Update the README/tests and submit a canonical PR for a demonstrated shared gap.


Modular rudiment layers use `type: "rudiment"` with `renderer: "particles"`,
`"bars"`, `"waveform"`, `"path"` or `"spectrum"`. The views share named, table,
matched, composite and recording motion adapters; a trusted Python registry
adds renderers without another clock or encoder. History is frame-addressed
and viewports are bounded. `framerudiments renderers` lists the built-ins;
`demo --rudiments` shows the four general views.

Spectrum views consume calibrated saved StemLab Fourier recordings, recover
RMS/dBFS from gain/normalization metadata, respect silent bands and export
dominant/local peaks and peak holds to a hashed per-frame JSONL sidecar. Peak
frequencies are band ranges, and hold uses bounded observed-frame history;
neither is an exact-pitch or audio true-peak claim. The optional `demo --spectrum`
uses StemLab 1.6+ to analyse a synthetic sweep; ordinary saved-recording rendering
does not import StemLab. See the canonical
[renderer API](https://github.com/kieransimkin/FrameRudiments/blob/main/docs/rudiment-renderers.md)
and [spectrum contract](https://github.com/kieransimkin/FrameRudiments/blob/main/docs/spectrum.md).

Optional ordered `effects` stages use Butterchurn 2.6.7 and projectM 4.2-dev
at exact source `349b7cc2db312d47cef6be24c6856ced6643a385`. Both process the
complete composed frame, including captions, lyric art, DanceRudiments-moving
sprites and beat-animated atlases, before encoding. Choose either engine or a
chain with original feedback, kaleidoscope and Julia-distortion presets.
Read the canonical [visualiser setup and contract](https://github.com/kieransimkin/FrameRudiments/blob/main/docs/visualisers.md).
Use `visualisers` to inspect pins and explicit `effects-setup` to provision a
runtime. Preserve exact output clocks and PCM from the same trim/repeat/fade
chain as the soundtrack. Retain preset/runtime/bridge hashes and cleanup
receipts. Feedback is sequential; recreate/replay to seek. GPU pixels vary by
driver, and pre-effect text bounds do not prove final legibility or safe zones.
Verify real shader/glyph/sprite feedback and encoded output; keep optional
engine setup, licences and trusted executable presets explicit.
