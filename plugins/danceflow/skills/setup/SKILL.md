---
name: setup
description: Set up the DanceFlow agent toolkit, choose a local workspace and discover installed tool capabilities.
---

# Set up DanceFlow

[Website](https://kieransimkin.co.uk/danceflow/) · [Toolkit source](https://github.com/kieransimkin/DanceFlow)

Choose the component that fits the user's task from catalogue.json or the per-tool skills. These are independently useful tools; installing the toolkit does not install every model or WordPress plugin. Short Shifter is unrelated to DanceFlow.

For the local MCP adapter, require uv and Python 3.10–3.13. Set DANCEFLOW_WORKSPACE in the host's MCP environment to one explicitly selected local directory, then restart that MCP server and call danceflow_capabilities. With no workspace configured, capability discovery works but all file operations reject. Do not default the workspace to the entire disk or user home.

KeywordMoves offline extraction and reviewed imports are available directly. Other live/paid/provider operations stay in KeywordMoves' explicitly configured CLI and require their own user-selected access and budget. PixelCue is optional: install it separately with Python 3.13, start pixelcue-server on loopback and call pixelcue_health before inference. Ask the user to select a model and accept any first-run download before allow_inference=true. Install StemLab's separately maintained plugin when music analysis is required; this bridge does not replace its analysis engine or React timeline.

Verify a small synthetic input before using real files. Return actual versions, supported operations and any unavailable dependencies. Installation, discovery, a queued job and a completed result are separate states.
