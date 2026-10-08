# Contribute to DanceFlow

[Website](https://kieransimkin.co.uk/danceflow/) · [Issues](https://github.com/kieransimkin/DanceFlow/issues)

People and agents are welcome. Start with an issue labelled `good first issue` or provide a minimal reproduction of a missing capability, failed integration or unclear setup step. Report the component, version, operating system, exact command, expected behaviour and actual result. Use synthetic or publicly licensed inputs; redact secrets and personal file paths.

For this toolkit, install `.[dev]`, run `python -m pytest` and `python scripts/validate_toolkit.py`, and include a small example when the behaviour changes. For engine changes, follow the current contribution instructions in the canonical repository linked from `catalogue.json` and the per-tool guides.

Keep changes focused. Preserve working interfaces, evidence units, local-path boundaries, accessibility/lifecycle behaviour and component licences. Explain which checks ran and which did not. Configuration, job submission and mocked contracts are not evidence of live model results or deployment.

PRs should describe the concrete problem, changed behaviour and validation. Maintainers review and assign versions. Every accepted improvement is pushed to its established repository and receives a matching tested GitHub release; configured registries are verified separately. Published tags and asset bytes are immutable.

Contribution discussion belongs in the relevant issue or PR. Automatic agents should avoid duplicate issues, unsolicited mentions, repeated comments and unreviewed releases. Please keep discussion practical and respectful.
