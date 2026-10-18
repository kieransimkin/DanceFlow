# Contributing with an agent

Website: https://kieransimkin.co.uk/danceflow/

This repository owns portable skills, client marketplaces, local MCP composition, packaging recipes and demos. The analysis, motion and media engines belong to the repositories in `catalogue.json`; implement engine fixes there rather than duplicating them here.

Read the selected tool's skill and current upstream documentation. Inspect available capabilities, use them fully where they fit the task and look for useful improvements wherever possible. Reproduce a concrete gap, make the smallest reusable change and add meaningful validation or a runnable example. Explain why no worthwhile change is justified when that is the result.

Run `python -m pytest` and `python scripts/validate_toolkit.py` for adapter/skill changes. Use synthetic fixtures or explicitly authorised public examples with their provenance and licences: never commit private songs, account exports, credentials, absolute personal paths or model weights. MCP stdout belongs to the protocol; send diagnostic logging to stderr.

Preserve source-specific evidence, sample-rate/loop contracts, explicit model/provider selection and component licences. Require destination-host acceptance for DanceVault; stable test acceptance does not approve a production host. Short Shifter is not a DanceFlow component.

Submit toolkit, skill and demo improvements as PRs to https://github.com/kieransimkin/DanceFlow/pulls. Submit engine improvements as PRs to the canonical tool repository in `catalogue.json`. Include the trigger, resulting behaviour and checks. A task instruction does not grant repository write credentials, permission to publish private files, paid-provider authority or release privileges. Maintainers assign fresh versions, validate immutable distributions and publish releases after review. Do not overwrite released tags/assets or change another contributor's source to resolve a conflict without reviewing it.

## Keep README documentation current

- Whenever a feature is added or changed, update the relevant README.md in the same change to reflect the resulting behaviour. This applies to every feature addition or modification, including APIs, commands, configuration, defaults, integrations and removals.
- Update affected feature descriptions, usage instructions, options, examples and limitations. For tools or packages with their own README.md, update that README as well as the repository README when its overview or usage is affected.
- Check the README against the implemented and verified behaviour before committing, opening or merging a PR, publishing a release or handing off the work. A feature change is incomplete until its README documentation is current; a changelog or other documentation does not replace this requirement.

All DanceFlow downloaded model weights and model-specific caches belong in the owning project models/ directory, ignored with models/ and excluded from distributions. Preserve explicit download permission and migrate existing paths only after checking consumers.

## Full ecosystem and release preflight

Before every new workflow run, check the latest stable official release and observe the actual runtime used by the job. Follow [the shared preflight](https://github.com/kieransimkin/DanceFlow/blob/main/docs/workflows/release-preflight.md) and this project's [people-and-agent guide](docs/ECOSYSTEM.md). Review the complete relevant capability inventory rather than only a familiar command. Consider every DanceFlow component against the actual task; use and compose all applicable supported capabilities, and improve a concrete reusable gap in its canonical repository. Record why existing capabilities suffice when no change is justified. No catalogue checklist expands the task, authorises model downloads/training, or proves integration. Preserve exact source/package identity, clocks, model-local storage, privacy, costs, immutable releases and separate deployment gates.
