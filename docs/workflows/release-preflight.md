# Start a DanceFlow workflow with current releases

People and agents use the same preflight. Review the [component catalogue](../../catalogue.json), choose the capabilities that serve the requested result, and read their released guides. Each tool remains independently useful; membership alone does not create an integration.

1. Run `danceflow-releases --output runs/NEW-RUN/releases.json` before every new workflow. This queries official GitHub releases afresh. It ignores documentation-only tags, drafts and prereleases, and resolves ThumbMoves' separate tag stream inside PixelCue. GitHub CLI authentication is used when available; otherwise it uses the public API. Network/rate-limit failures remain `unavailable` and require resolution before claiming a tool is current.
2. Observe the actual runtimes used by the job. The checker sees only its own Python environment. For other Python environments, run their package/version commands; for npm inspect the installed package manifest; for WordPress read the active plugin version. Pass a JSON mapping of component names to observed versions with `--installed installed.json`. A directory name, checkout version or loaded script is insufficient.
3. Compare the release notes, exact tagged docs, package manifests and compatibility constraints. Preserve a receipt containing date, release/tag, source commit, selected distribution and SHA-256 at installation. Resolve source commits and verify registry acceptance separately; the release checker does not infer them from a mutable branch name or from GitHub publication.
4. Update compatible local runtimes through official distributions. Keep the old package/lock for rollback, preserve models and data, then verify actual imports, dependency health and a relevant small example. An upstream `main` feature is developmental until its matching stable release is verified. Do not silently downgrade or replace a required feature when compatibility fails.
5. Select from the [complete capability references](../capabilities/index.md). Use every relevant capability, compose supported files/APIs, and improve a demonstrated reusable gap in its canonical project. Record why an existing capability meets the need when no change is justified. Do not create expensive inference, media scans, training or unrelated work just to exercise the catalogue.
6. Keep release, installed, invoked, produced, reviewed and deployed states separate. Software updates do not authorise a website save, plugin deployment, account/access change, spending, model download or rights commitment. Apply the destination's actual approval requirements.

```sh
python -m pip install danceflow-agent-tools
danceflow-releases --output runs/new-workflow/releases.json
# After observing runtimes outside this Python environment:
danceflow-releases --installed runs/new-workflow/installed.json --output runs/new-workflow/verified-releases.json
```

An example observation file is `{"StemLab":"1.8.0","DanceMoves":"3.4.0"}`. These are dated example values, not future authority. The command returns 2 if any official release query is unavailable. `not_observed` means this environment has no observation; it does not establish that a tool is absent from the computer. `ahead_of_release` and `unverified_identity` require inspection, not a claim of currency. Exit 0 means the queries completed; inspect individual rows before deciding what to update.

## Read the ecosystem by task

| Result | Supported composition |
|---|---|
| Understand a master or select a clip | StemLab analysis, saved evidence, native matching and source-frame loops; React Timeline Sequence for actual transport/editing |
| Render video offline | FrameRudiments compositor, native DanceRudiments, saved StemLab evidence; PixelCue/PrismMoves for scoped visual analysis |
| Build web motion | DanceMoves shared clocks, effects, input, playback, accessibility, quality and cleanup; native DanceRudiments; metadata-derived EPK timing |
| Prepare and find visual assets | PixelCue discovery/history/service, ThumbMoves cache previews, RasterMoves derivatives; LikenessForge only for an authorised identity task |
| Research language and publication facts | KeywordMoves source-native evidence and imports; EPK Social Metadata for verified page facts |
| Deliver private files | DanceVault encrypted delivery only with destination-host acceptance and the relevant recipient/access authority |

![Actual encoded synthetic FrameRudiments clock-composition example](https://raw.githubusercontent.com/kieransimkin/FrameRudiments/v0.4.1/docs/media/beat-alignment.png)

Actual synthetic renderer output retained in FrameRudiments 0.4.1. [Play the controlled clock example](https://github.com/kieransimkin/FrameRudiments/blob/v0.4.1/docs/media/beat-alignment.mp4). This demonstrates composition, not song-analysis accuracy. The linked reference includes frame/hash evidence; playback remains user controlled.

## Potential problems

- **The repository's newest release is a documentation tag.** Filter for the component's stable semantic runtime prefix, inspect real distributions and read its source version. ThumbMoves uses `thumbmoves-v`; other current components use `v`. Never install a policy tag as software.
- **A checkout contains features beyond its latest release.** Keep those in a development section with the exact source commit. Inspect the tagged source before suggesting the feature in a production run. A README on `main` is not evidence that its contents ship in the installed wheel.
- **The checker runs in a different environment.** Inspect that runtime directly and provide explicit observations; never label unobserved WordPress or npm installations current.
- **A query fails.** Preserve `unavailable`, use the documented network/authentication recovery, and retry once the cause is resolved. Do not replace fresh verification with an old successful receipt.
- **An old environment has an incomplete unrelated distribution.** Preserve its evidence and models. Verify the selected integration in a healthy project environment or repair the actual missing package; do not describe a version-only install as a repaired environment.

Screenshots and recordings belong beside the feature they demonstrate. A generated diagram may explain a contract but cannot establish installation, operation or publication. This preflight needs no new decorative generated bitmap; the actual encoded example explains the timing handoff directly.
