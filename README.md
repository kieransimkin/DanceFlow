# DanceFlow for people and agents

[Kieran Simkin's website](https://kieransimkin.co.uk/) · [DanceFlow ecosystem](https://kieransimkin.co.uk/danceflow/) · [Source and contributions](https://github.com/kieransimkin/DanceFlow)

Portable instructions for twelve independently useful music, motion and media tools, plus a local MCP adapter that composes the published KeywordMoves and PixelCue interfaces. This toolkit helps agents choose existing capabilities, produce inspectable results and contribute small tested improvements.

<!-- mcp-name: io.github.kieransimkin/danceflow -->

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
uvx --python 3.13 --from danceflow-agent-tools==0.1.5 danceflow-mcp --workspace ./my-workspace
```

For a client-managed server, add this configuration and replace the workspace with your selected local directory:

```json
{
  "mcpServers": {
    "danceflow": {
      "command": "uvx",
      "args": ["--python", "3.13", "--from", "danceflow-agent-tools==0.1.5", "danceflow-mcp"],
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
| [ThumbMoves](docs/tools/thumbmoves.md) | Cache-only OS thumbnails with explicit misses |
| [React Timeline Sequence](docs/tools/react-timeline-sequence.md) | Audio timeline, transport and sample-frame loops |
| [EPK Social Metadata](docs/tools/epk-social-metadata.md) | WordPress Open Graph, X cards and Schema.org |
| [DanceVault](docs/tools/dancevault.md) | Experimental encrypted WordPress delivery; hosting acceptance pending |

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
