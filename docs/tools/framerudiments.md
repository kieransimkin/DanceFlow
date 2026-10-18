# FrameRudiments

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/FrameRudiments) · [PyPI](https://pypi.org/project/framerudiments/)

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

![Actual composed and processed lyric/sprite frames](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.1.4/docs/media/full-frame-comparison.png)

Actual synthetic FrameRudiments 0.1.4 candidate output, before and after both
real engines. Captions and native moving sprites/atlas share the effect path.
[Play the four-second demonstration](https://kieransimkin.github.io/DanceFlow/framerudiments.html)
with [transcript](https://github.com/kieransimkin/FrameRudiments/blob/v0.1.4/docs/media/demo-transcript.md).

![Generated processing-order illustration, not a screenshot](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.1.4/docs/media/effects-pipeline.svg)

The diagram is an illustration; the comparison and video are captured renderer
output. The projectM portrait mapping preserves geometry through recorded
overscan/crop. Review processed text for legibility and destination safe zones.


![Actual documentation player interface with native controls](https://raw.githubusercontent.com/kieransimkin/DanceFlow/v0.1.9/docs/screenshots/framerudiments-player.jpg)

Local prepublication playback QA for the documentation player: 4.00-second synthetic video reached its end with native controls and no media error. This is an interface capture, separate from the generated diagram.

## Profile visualiser input response with FrameRudiments and PrismMoves

Use FrameRudiments 0.3.0+ `presets-install` and `presets-profile`, or its maintained
`scripts/profile_visualisers.py`, to compare Butterchurn/projectM presets. Read
the canonical
[capture and synthesis workflow](https://github.com/kieransimkin/FrameRudiments/blob/v0.3.0/docs/preset-profiling.md).
The separately installed pinned catalogue has 14,680 distinct upstream entries
and 67 shared textures; membership is separate from actual GPU acceptance and
public-use rights. Preserve source notices, preset/runtime hashes and aliases.

Use explicitly authorised sample tunes, each with pinned master, cover and timed
lyrics. Keep private inputs and reports outside public packages. Cross cover/lyric composition and the three
static cards with programme/silence controls; replay every preceding feedback
frame and capture the declared output intervals. Record source offsets, sample
bounds, source/output clocks, frame rate, mix and actual cleanup. Preserve the
published source-bound beat adapter and original-time lyric/recording contracts.

Invoke a PrismMoves Python 3.13 runtime (PrismMoves 0.1.0/PixelCue 0.9.0
verified baseline); use PixelCue's actual statistics/comparison API instead of
copying analysis. Keep optional model hypotheses and unavailable states distinct,
with local weights/caches under the owning experiment models/. No automatic
downloads or expensive full sweep is implied. Benchmark an explicit batch before
extending it; retain completed, failed and untested coverage separately.

Combine measured source/output, temporal, programme/silence and shared-card/tune
comparisons into condition families and response ranges. Review palette, luminance,
edges/symmetry, texture, spatial frequency and actual text treatment before writing
a visual thesis or invariants. Near-duplicate frame grabs share a lineage; do not
invent one overall brand/quality score. Keep legibility, flash safety, musical
approval, rights and final encoded-video QA as separate evidence.

![Generated static calibration inputs, not preset-output evidence](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.3.0/docs/media/preset-test-cards.png)

Generated test-card illustrations. [Play the actual full-frame pipeline example](https://kieransimkin.github.io/DanceFlow/framerudiments.html)
with user controls and transcript; that earlier software demo is distinct from
the private real-song profiles. Keep raw PrismMoves reports, captured PNG hashes,
resume settings and failure receipts. A stored rule does not prove another chat
adopted it or that every catalogue entry has been profiled.

## Full feature workflow

[Read the released feature references](../capabilities/framerudiments.md) and [check current releases before every new run](../workflows/release-preflight.md). Consider the whole ecosystem, use and improve applicable shared capabilities, and keep actual runtime/output evidence separate from availability.
