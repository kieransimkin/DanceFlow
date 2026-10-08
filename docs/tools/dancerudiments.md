# DanceRudiments

[Website](https://kieransimkin.co.uk/danceflow/) · [Canonical source](https://github.com/kieransimkin/DanceRudiments)

Deterministic rhythmic position functions, authored pattern collections and a visualizer.

Read README.md, docs/python.md and the guide for the selected binding. Core timing uses 64 pips per beat. Preserve the complete period of a pattern and the independent source/licence attribution for authored collections. Use the released C++/WASM sampler instead of approximating its positions with page-local animation equations.

## Development checks

```sh
cmake -S . -B build -DDANCERUDIMENTS_BUILD_TESTS=ON
cmake --build build
ctest --test-dir build --output-on-failure
```

Submit contributions to https://github.com/kieransimkin/DanceRudiments/pulls. See the repository's current instructions before editing.
