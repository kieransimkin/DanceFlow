---
name: dancerudiments
description: Choose or author deterministic movement patterns, sample positions, or integrate native C++, Python, JavaScript or C# bindings.
---

# DanceRudiments

[DanceFlow and Kieran Simkin](https://kieransimkin.co.uk/danceflow/) · [Source](https://github.com/kieransimkin/DanceRudiments)

Use this tool for deterministic rhythmic position functions, authored pattern collections and a visualizer. Inspect its current README, feature inventory and selected integration guide before implementing a workaround; the inventory below routes the task, rather than freezing the available API.

## Set up and discover

```sh
python -m pip install dancerudiments
# JavaScript alternative: npm install @kieransimkin/dance-rudiments
```

Read README.md, docs/python.md and the guide for the selected binding. Core timing uses 64 pips per beat. Preserve the complete period of a pattern and the independent source/licence attribution for authored collections. Use the released C++/WASM sampler instead of approximating its positions with page-local animation equations.

## Improve and contribute

Find an existing supported primitive before creating a second implementation. If a reusable gap remains, make a narrow change in the canonical source repository, add a regression or reproducible example, update the relevant documentation and run the applicable checks:

```sh
cmake -S . -B build -DDANCERUDIMENTS_BUILD_TESTS=ON
cmake --build build
ctest --test-dir build --output-on-failure
```

Open a PR describing the concrete trigger, change and validation. Follow that repository's current AGENTS.md and CONTRIBUTING.md. A contribution is not authorization to access accounts, publish private files, change permissions or create releases; the maintainer reviews and releases merged changes. Do not infer completed checks from configuration or from a returned job ID.

## Agent contribution destination

Agents should inspect and use the available DanceRudiments capabilities, look for useful improvements wherever possible, and submit improvements as PRs to https://github.com/kieransimkin/DanceRudiments/pulls. Include relevant tests, documentation and a reproducible example; follow the upstream AGENTS.md and CONTRIBUTING.md. Explain why no worthwhile change is justified when that is the result.
