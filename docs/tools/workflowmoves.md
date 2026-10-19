# WorkflowMoves

[DanceFlow](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/WorkflowMoves) · [Releases](https://github.com/kieransimkin/WorkflowMoves/releases)

WorkflowMoves is the guarded workflow layer for the ecosystem. It packages versioned rules, task guides, portable agent skills, validators and an additive installer. Use it to bring a reviewed DanceFlow capability into project instructions without replacing project-owned text.

Before every run, check the latest stable release and the actual installed source. Download the matching archive and checksum manifest, then preview the exact route set:

```powershell
python install.py --root "Z:\My Songs" --routes tool-adoption-routes.json --check
python install.py --root "Z:\My Songs" --routes tool-adoption-routes.json
```

The preview validates anchors, known predecessors and conflicts before any write. Read back every changed target after applying. A clean preview is not evidence of installation, and a saved instruction is not evidence that another running agent adopted it.

Use the complete component references and compose supported file/API contracts. Keep FrameRudiments, StemLab, DanceRudiments, DanceMoves, PixelCue, PrismMoves and every other package in its own area of responsibility. Put weights and model caches under the owning project's ignored `models/`.

![Generated WorkflowMoves guarded-installation overview](https://raw.githubusercontent.com/kieransimkin/WorkflowMoves/v0.1.34/docs/media/workflowmoves-overview.svg)

Generated architecture illustration for WorkflowMoves 0.1.34. It explains the contract; the installed destination and its evidence must be verified separately.

## Full feature workflow

[Read the released feature references](../capabilities/workflowmoves.md) and [check current releases before every new run](../workflows/release-preflight.md). Improve a concrete shared gap in its canonical owner, with tests and a reproducible public-safe example.
