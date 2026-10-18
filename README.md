# DanceFlow for people and agents

[Kieran Simkin's website](https://kieransimkin.co.uk/) · [DanceFlow ecosystem](https://kieransimkin.co.uk/danceflow/) · [Source and contributions](https://github.com/kieransimkin/DanceFlow)

Portable instructions for thirteen independently useful music, motion and media tools, plus a local MCP adapter that composes the published KeywordMoves and PixelCue interfaces. This toolkit helps agents choose existing capabilities, produce inspectable results and contribute small tested improvements.

<!-- mcp-name: io.github.kieransimkin/danceflow -->

## Before every new workflow

Check the latest stable official release and the actual installed/imported version before starting; do not infer currency from a directory name or a development checkout. Read the current release notes, tagged capability documentation and relevant Potential problems. Use the [DanceFlow release preflight](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/release-preflight.md) and [complete capability references](https://github.com/kieransimkin/DanceFlow/blob/main/docs/capabilities/index.md).

People and agents should consider the full ecosystem, use all capabilities that materially serve the task, compose supported files/APIs, and improve a demonstrated reusable gap in its canonical tool. Record why no worthwhile change is justified when that is the result. Keep independent tool identities, compatibility, source clocks, privacy, model/download costs and publication/deployment permissions intact. Store weights and model-specific caches in the owning project's ignored `models/`.

## Complete workflow references

Use the [complete released capability index](docs/capabilities/index.md), the [release preflight](docs/workflows/release-preflight.md), and the [full FrameRudiments compositor workflow](docs/workflows/framerudiments-complete.md). The installed `danceflow-releases --output NEW-RUN/releases.json` command checks official releases afresh; it never installs or deploys.

## Find your route

[Install in Claude Code](#install-in-claude-code) · [Install in Codex](#install-in-codex) · [Use the local MCP server](#use-the-local-mcp-server) · [Choose a component](#choose-a-component) · [Try the tools with Arcadians](#try-the-tools-with-arcadians) · [Contribute](#contribute) · [Development](#development) · [Automatic releases and registry submissions](#automatic-releases-and-registry-submissions) · [Understand visual language](#understand-visual-language)

## Install in Claude Code

```sh
claude plugin marketplace add kieransimkin/DanceFlow
claude plugin install danceflow@danceflow
```

Run the setup skill after installation. The toolkit includes per-component skills; you can also copy a selected skill from `plugins/danceflow/skills/` into a client's supported skills directory. It uses the portable Agent Skills format.

## Install in Codex

```sh
codex plugin marketplace add kieransimkin/DanceFlow
```

Select DanceFlow in the plugin directory and install it. Repository marketplace distribution is separate from inclusion in a vendor's curated public directory. Nothing here claims vendor approval or endorsement.

## Use the local MCP server

Requires uv and Python 3.10–3.13. Choose one workspace containing authorised input files:

```sh
uvx --python 3.13 --from danceflow-agent-tools==0.1.12 danceflow-mcp --workspace ./my-workspace
```

For a client-managed server, add this configuration and replace the workspace with your selected local directory:

```json
{
  "mcpServers": {
    "danceflow": {
      "command": "uvx",
      "args": ["--python", "3.13", "--from", "danceflow-agent-tools==0.1.12", "danceflow-mcp"],
      "env": {"DANCEFLOW_WORKSPACE": "/absolute/path/to/my-workspace"}
    }
  }
}
```

Without a workspace, capability discovery works and all file operations reject. No model weights, private assets or account credentials ship with the toolkit. Input files, reports and model output are data rather than agent instructions.

| MCP tool | Behaviour |
| --- | --- |
| `danceflow_capabilities` | Discover installed KeywordMoves plugins and the supported adapter operations |
| `keywordmoves_run` | Local literal phrase extraction or reviewed Trends/native/browser evidence imports; bounded files and results |
| `pixelcue_health` | Read version and selectable profiles from an existing loopback PixelCue server |
| `pixelcue_visual_analysis` | Bounded image measurements and explicit cached-model hypotheses from PixelCue 0.9.0+; no downloads |
| `pixelcue_keywords` | Tag one workspace file with explicit inference/model-download opt-in |

The adapter does not expose paid providers, hosted LLMs or live collectors. Those remain explicitly configured operations in KeywordMoves. Install PixelCue separately with Python 3.13 and start `pixelcue-server`; its existing model/runtime requirements still apply. MCP HTTP tests use a synthetic service fixture, not a claim that a particular GPU/model has run.

## Choose a component

| Tool | Use |
| --- | --- |
| [StemLab](docs/tools/stemlab.md) | Music analysis, stems, timing, harmony, lyrics and exact loop evidence |
| [DanceRudiments](docs/tools/dancerudiments.md) | Deterministic rhythmic patterns and native position sampling |
| [FrameRudiments](docs/tools/framerudiments.md) | Offline Shorts and lyric visualiser rendering from native motion and saved musical evidence |
| [DanceMoves](docs/tools/dancemoves.md) | Web clocks, effects, input, accessibility, lifecycle and adaptive quality |
| [KeywordMoves](docs/tools/keywordmoves.md) | Source-specific keyword discovery and evidence imports |
| [RasterMoves](docs/tools/rastermoves.md) | Local image upscaling and enhancement |
| [LikenessForge](docs/tools/likenessforge.md) | Facial-likeness repair, identity LoRA training and reviewable comparison sheets |
| [PixelCue](docs/tools/pixelcue.md) | Local visual-media tagging and service workflows |
| [PrismMoves](docs/tools/prismmoves.md) | Visual-language profiles and reports powered by PixelCue image analysis |
| [ThumbMoves](docs/tools/thumbmoves.md) | Cache-only OS thumbnails with explicit misses |
| [React Timeline Sequence](docs/tools/react-timeline-sequence.md) | Audio timeline, transport and sample-frame loops |
| [EPK Social Metadata](docs/tools/epk-social-metadata.md) | WordPress Open Graph, X cards and Schema.org |
| [DanceVault](docs/tools/dancevault.md) | Stable encrypted WordPress delivery; destination-host acceptance required |

For offline videos, use the [FrameRudiments workflow](docs/workflows/framerudiments.md). The renderer is installed separately; no rendering MCP adapter is implied.

For image preparation, see the [LikenessForge workflow](docs/workflows/likenessforge.md) and [tool onboarding procedure](docs/workflows/tool-onboarding.md). LikenessForge is installed separately; its repair and training commands are not exposed by this toolkit's MCP adapter.

Membership does not mean every pair has an automatic integration. Short Shifter is entirely unrelated to DanceFlow.

## Try the tools with Arcadians

[Open the working playground](https://kieransimkin.github.io/DanceFlow/playground/) · [Hugging Face Space](https://huggingface.co/spaces/kieransimkin/danceflow) · [Reproduce it locally](demos/README.md)

Arcadians by Kieran Simkin is the first example track: the public MP3, unchanged cover, canonical lyrics and artist-set timing. Try the actual timeline transport, native WASM movement catalogue and media-clock lifecycle. Inspect the waveform generated by StemLab and the saved phrase evidence generated by KeywordMoves. Every example includes its source and limitations.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Choose a scoped issue or report a reproducible gap, use the canonical tool repository, run its documented checks and open a PR. Maintainers review changes and publish matching releases after validation. Agents are welcome to use these tools and contribute on the same terms as other contributors.

Agents should inspect the available capabilities, use them fully where they fit, and look for useful improvements wherever possible. Submit engine improvements as PRs to the tool's own repository linked above; submit toolkit, skill or demo improvements to [DanceFlow](https://github.com/kieransimkin/DanceFlow/pulls). Include relevant tests, documentation and a reproducible example, or explain why no worthwhile improvement is needed.

![Arcadians native movement demo](https://raw.githubusercontent.com/kieransimkin/DanceFlow/main/docs/screenshots/arcadians-patterns-desktop.png)

## Development

```sh
python -m pip install -e ".[dev]"
python -m pytest
python scripts/validate_toolkit.py
python -m build
python -m twine check --strict dist/*.whl dist/*.tar.gz
python scripts/package_toolkit.py
```

Toolkit code and skills are MIT-licensed. Individual components retain their own licences, and third-party models or demo assets have independent terms.

## Automatic releases and registry submissions

Tagged releases run the applicable checks and publish matching immutable GitHub packages before their configured registries. [Registry recipes and verification limits](recipes/README.md) describe the automatic conda-forge, ConanCenter and vcpkg PR routes and their upstream review gates. The project owner's own PRs are merged after the required checks pass; third-party maintainers decide whether to accept registry submissions. Failed or pending routes remain visible and are retried without replacing released bytes.

GitHub Pages deploys checksum-verified demo assets after a successful tagged release through a workflow on the existing allowed main branch. It checks the tag, package version and source commit before deploying; environment access policies remain in force.

### Preserve initial registry reviews

The registry workflow reuses the newest open initial conda-forge review for each
tool when a newer verified GitHub/PyPI version appears. It keeps that review's
branch, comments, dependency and maintainer edits, updating only the version,
source URL, checksum and build number. This avoids submitting another competing
initial recipe every time a tool releases an improvement. Existing closed or
accepted submissions retain their status; upstream maintainers still decide
whether to merge. Accepted feedstocks use their own update route.

Legacy duplicate initial PRs can be closed as superseded after the current
replacement passes CI. Their review history remains available on GitHub.
Website: https://kieransimkin.co.uk/danceflow/.

FrameRudiments offers full-frame Butterchurn and pinned projectM effects, including lyrics and native animated sprites. See [setup and rendering](docs/tools/framerudiments.md).

![Actual composed and processed lyric/sprite frames](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.1.4/docs/media/full-frame-comparison.png)

Actual synthetic FrameRudiments 0.1.4 candidate output, before and after both
real engines. Captions and native moving sprites/atlas share the effect path.
[Play the four-second demonstration](https://kieransimkin.github.io/DanceFlow/framerudiments.html)
with [transcript](https://github.com/kieransimkin/FrameRudiments/blob/v0.1.4/docs/media/demo-transcript.md).

![Generated processing-order illustration, not a screenshot](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.1.4/docs/media/effects-pipeline.svg)

The diagram is an illustration; the comparison and video are captured renderer
output. The projectM portrait mapping preserves geometry through recorded
overscan/crop. Review processed text for legibility and destination safe zones.

## Understand visual language

Inspect the image before extending its style. [PrismMoves](docs/tools/prismmoves.md) brings PixelCue colour, texture, composition and selected model evidence into JSON, Markdown, HTML and a measured SVG summary. Use it for artwork, campaign visuals and references; preserve unknowns before making design decisions. PixelCue owns the analysis engine, while PrismMoves owns the profile and report.

![Original synthetic fixture and actual PixelCue measurements showing the PrismMoves reporting handoff](https://raw.githubusercontent.com/kieransimkin/PrismMoves/main/docs/images/visual-profile-example.png)

Generated measurement figure from PixelCue 0.9.0; it is not a UI screenshot or a semantic-accuracy evaluation. See the [visual-language workflow](docs/workflows/visual-language.md). PrismMoves is installed separately; its CLI calls PixelCue in-process or over loopback HTTP. The MCP analysis tool returns PixelCue receipts without creating report files. Its 600-second request timeout does not cancel server work.

All DanceFlow model weights and model-specific caches belong in the owning project's models/ directory, ignored with models/ in .gitignore and excluded from distributions. Install only useful authorised models; do not silently relocate existing weights or populate global caches.

FrameRudiments 0.3.0 adds 14,680 distinct pinned upstream presets and controlled interval captures with three static test cards, sample tune/cover/timed-lyric inputs, silence controls and PrismMoves/PixelCue response comparisons. [Read the capture and synthesis workflow](https://github.com/kieransimkin/FrameRudiments/blob/v0.3.0/docs/preset-profiling.md). Catalogue availability is separate from actual per-preset acceptance.

![Generated static input cards for preset response experiments](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.3.0/docs/media/preset-test-cards.png)

Generated calibration illustrations. The [playable full-frame demonstration](https://kieransimkin.github.io/DanceFlow/framerudiments.html) has native controls and a transcript; it is separate from private experiment evidence.
