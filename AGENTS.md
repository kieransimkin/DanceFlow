# Contributing with an agent

Website: https://kieransimkin.co.uk/danceflow/

This repository owns portable skills, client marketplaces, local MCP composition, packaging recipes and demos. The analysis, motion and media engines belong to the repositories in `catalogue.json`; implement engine fixes there rather than duplicating them here.

Read the selected tool's skill and current upstream documentation. Inspect available capabilities before proposing a new feature. Reproduce a concrete gap, make the smallest reusable change and add meaningful validation or a runnable example.

Run `python -m pytest` and `python scripts/validate_toolkit.py` for adapter/skill changes. Use synthetic fixtures: never commit private songs, account exports, credentials, absolute personal paths or model weights. MCP stdout belongs to the protocol; send diagnostic logging to stderr.

Preserve source-specific evidence, sample-rate/loop contracts, explicit model/provider selection and component licences. Do not represent DanceVault as production-ready or Short Shifter as a DanceFlow component.

Open a PR with the trigger, resulting behaviour and checks. A task instruction does not grant repository write credentials, permission to publish private files, paid-provider authority or release privileges. Maintainers assign fresh versions, validate immutable distributions and publish releases after review. Do not overwrite released tags/assets or change another contributor's source to resolve a conflict without reviewing it.
