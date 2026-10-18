---
name: framerudiments
description: Render offline Shorts, Canvas-style videos and lyric visualisers from native DanceRudiments motion and saved StemLab timing or recordings.
---

# FrameRudiments

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/FrameRudiments)

Use the shared Python renderer for new or materially revised offline videos.
Read its current README and project-format guide; use the existing historical
generator when reproducing an approved old film. Keep release artwork/layouts
in declarative projects or scene hooks. Improve a reusable missing mechanism
in FrameRudiments instead of copying another clock, caption or encoder loop.

Install `framerudiments` from PyPI in a dedicated Python 3.11+ environment and
provide FFmpeg/ffprobe and an explicitly selected font. Inspect `framerudiments
--help`; `demo` creates synthetic fixtures, `plan` validates pins and exports
the frame ledger, `preflight` checks every composed frame and `render` encodes
and verifies a new output directory. No command publishes or schedules media.

Pin the exact authorised master, canonical LRC/CUE/font/artwork and source
sample bounds. Reuse StemLab beat/loop/matcher/recording files, retaining report
hashes, source offsets, BPM and phase status. Explicitly select a match window;
scores do not approve motion. Native recordings stop at capture bounds and
keep all axes and their own 64-pip clock. One DanceMoves tick is four pips.

Use one frame ledger for caption state, clears and subtitle sidecars. Keep
structural cues separate from lyrics and optional canonical-text comparison
exact. Short derivatives default to 120 ms quarter-sine endpoint fades; retain
an approved raw seam with `audio.fade_seconds: 0`. Canvas/full visualisers
default to no fades. Never change the source master or stretch audio for frames.

Inspect the encoded poster, caption/scene boundaries and final frames, all
transformed alpha bounds and the destination's current safe areas. Technical
QA and a clean decode do not establish listening approval, musical seams,
rights, platform preview acceptance or public eligibility. Custom scene hooks
must pin their own assets and verify their own painted bounds/collisions.

Contribute focused fixes with current README, synthetic tests and a reproducible
example to https://github.com/kieransimkin/FrameRudiments/pulls. Run the full
FFmpeg/font-enabled suite, ruff, build, strict package checks and an installed
wheel render. Preserve immutable versions and automatic software publication after checks; media schedules and site deployment retain their own requirements.


For rudiment-driven particles, bars, waveform traces, XY paths or spectra, use
the modular `type: "rudiment"` layer and the canonical renderer/spectrum guides.
Select original recording dimensions, bounded history and viewports; keep
waveform traces distinct from PCM. Spectrum requires recoverable StemLab Fourier
calibration, exact frequency ranges and silent-band handling. Retain the hashed
`rudiment-analysis.jsonl` peak/hold reports and verify encoded representative
states. Extend the trusted Python registry for a reusable view rather than
copying sampling, analysis or frame loops. Optional demo generation uses
StemLab 1.6+; saved-recording rendering requires no new model run.

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

## Current releases and full feature routing

Before every new workflow, follow the [release preflight](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/release-preflight.md) and [complete capability reference](https://github.com/kieransimkin/DanceFlow/blob/main/docs/capabilities/framerudiments.md). Observe the real installed runtime, review every relevant feature and compose supported ecosystem tools. Improve a demonstrated reusable gap in its canonical repository, or record why the tool already meets the need. This guidance does not trigger unrelated processing or downloads.

For the full compositor, authoring and profiling routes, read [the detailed workflow](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/framerudiments-complete.md). The source helpers and native GPU runtimes are separate from the universal wheel.
