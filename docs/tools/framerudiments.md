# FrameRudiments

[DanceFlow](https://kieransimkin.co.uk/danceflow/) Â· [Canonical source](https://github.com/kieransimkin/FrameRudiments) Â· [PyPI](https://pypi.org/project/framerudiments/)

FrameRudiments is the offline Python renderer for Shorts, Canvas-style clips
and full lyric visualisers. It composes Pillow layers on a frame-addressed
timeline, samples released native DanceRudiments functions and non-looping
recordings, and consumes saved StemLab beats, accepted loops and explicit
motion-match selections. No audio analysis models run in the renderer.

Install `python -m pip install framerudiments` with Python 3.11+, FFmpeg/ffprobe
and an explicit font. `framerudiments demo ./demo --font /path/font.ttf` creates
synthetic input. Then `plan demo/project.json --output plan.json`, `preflight
demo/project.json --output preflight` and `render demo/project.json --output
render`, supplying `--ffmpeg` where it is not on PATH. Every output is a new
directory. The [rendering workflow](../workflows/framerudiments.md) records handoffs.

Keep release masters, artwork and canonical timing local and hash-pinned. Use
native-rate sample bounds, preserve 64 pips versus 16 ticks per beat, and keep
BPM confirmation separate from phase evidence. Explicit match/recording source
identity and windows matter. Input changes fail validation. Transformed sprite
bounds and caption fit are checked every frame; custom scene drawing retains
its own review obligations. Legacy generators remain available for reproduction.

Outputs include H.264/AAC MP4, JSON ledger/manifest, SRT/ASS, source and encoded
QA frames, poster, phone preview and encode log. Complete decoded timestamps,
frame count, audio duration/channels and fast start are checked. `technical-QA
passed` does not imply a pleasant musical loop, attended listening, rights or
platform approval. Rendering never uploads or publishes media.

Submit improvements to [canonical pull requests](https://github.com/kieransimkin/FrameRudiments/pulls), with current README, focused regression coverage and a synthetic example. Use upstream AGENTS.md/CONTRIBUTING.md, full render CI, strict wheel/sdist validation and a clean installed-wheel smoke render.


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
