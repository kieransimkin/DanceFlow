# DanceFlow ecosystem through one MCP server

Version 0.1.20 packages the catalogue-backed MCP hub, seventeen components and eight workflow guides. The prior 0.1.16 five-tool bridge does not acquire these features automatically; verify the actual installed wheel and resource readback. Potbot and Unity discovery does not implement their native host execution.

## Discover before execution

Start with `danceflow_search` to find a feature using words from a task, or `danceflow_list_workflows` with no arguments to browse procedures. These tools do not require prior knowledge of component names, workflow IDs or resource URIs. The server's initialization instructions point new clients to both entry points.

| Tool | Inputs | Result |
| --- | --- | --- |
| `danceflow_search` | Optional `query`, `kind` (`all`, `component`, `tool`, `workflow`, `skill`, `reference`), `component`, `limit`, `offset` | Ranked matches with summaries, actual tool schemas where applicable, runtime/effect information, references and explicit `next_call` values |
| `danceflow_list_workflows` | Optional `query`, `component`, `limit`, `offset` | Workflow titles, summaries, related components, source identity and the call to read each procedure |
| `danceflow_get_workflow` | `name` returned by search/listing | Full workflow instructions or linked source reference with source identity; it does not execute the workflow |

For example, call `danceflow_search` with `{"query":"render video"}`, `{"query":"WordPress","kind":"tool"}`, or `{"query":"thumbnail"}`. An empty query browses every entry in the selected kind. Listing/search responses include total counts, coverage and a `next_offset` when more results exist. Follow the returned calls rather than constructing IDs or file paths. Tool schemas come from the server's actual `tools/list`, including federated native StemLab tools; there is no separately maintained list of callable tools.

The searchable documentation includes all seventeen component skills, capability references and guides, shared overviews, and eight bundled DanceFlow workflow guides. When the operator configures `components.workflowmoves.source_root`, discovery also reads that checkout's Markdown workflow guides, portable skill recipes and supporting references. These records use namespaced IDs such as `workflowmoves/workflows/wordpress-blog-rest-api`. Source paths are confined to the configured checkout, reads are bounded, and malformed, unreadable or skipped documents appear in coverage information. Without that source, discovery explicitly reports the missing WorkflowMoves coverage and provides a setup/reference call. The eight packaged guides are not described as the complete WorkflowMoves workflow library. Search does not fetch remote documentation, run engine operations or install models.

Call `danceflow_capabilities` for all seventeen components and observed runtime availability. Call `danceflow_component` with a discovered catalogue ID for exact operation schemas, conditional effects, native-host routes, source references and requirements. Missing optional packages do not stop unrelated components. A related component mentioned in a document is not a verified runtime dependency.

Every component has three MCP resources:

- `danceflow://components/{name}/capabilities`
- `danceflow://components/{name}/skill`
- `danceflow://components/{name}/guide`

`danceflow://catalogue`, `danceflow://overview/{name}` and `danceflow://workflows/{name}` expose the shared references. `danceflow_read_reference` provides the same text for clients without resource support. The `danceflow_workflow` MCP prompt loads a selected portable skill; it does not execute that procedure.

Read `danceflow://overview/mcp` for this guide. References retain their dated upstream baselines. The operation descriptor's `source` identifies the exact released CLI used to validate an adapter; a newer feature in a capability reference is not automatically callable.

## Coverage

| Component | Callable MCP interface | Separate runtime or host |
| --- | --- | --- |
| StemLab | Its native `stemlab_*` tools, including analysis/MIDI/evidence/loop jobs, logs, artifacts and timeline viewer; 15 additional bounded CLI routes | Install StemLab with its `codex` extra in the selected Python environment; models remain separately provisioned |
| DanceRudiments | Native catalogue and integer-pip sampling | Native Python extension |
| FrameRudiments | Ten CLI routes, including plan, preflight, render, demonstrations and preset profiling | Renderer, FFmpeg and selected effects runtimes |
| DanceMoves | Page, timing-file and motion-capture validation through actual public exports | Workspace npm package; browser host for live clocks, motion and sensors |
| KeywordMoves | Existing bounded offline extraction and reviewed evidence imports | Other collectors, paid providers and hosted LLMs use the owner's configured native routes |
| RasterMoves | Eleven CLI routes for discovery, plans, selected derivatives, model provisioning and analysis | Optional canonical backends; offline processing and explicit downloads are distinct |
| LikenessForge | Nine CLI routes, including inspection, repair, comparisons, preparation and training | Canonical package/backends; explicit inference, download/network and training acknowledgements |
| PixelCue | Existing loopback health, keyword tagging and visual-analysis APIs | An already-running local PixelCue service |
| PrismMoves | Four CLI routes for discovery, profiles, preset analysis and gallery compilation | Canonical PrismMoves and PixelCue package/service; conditional model/download effects |
| ThumbMoves | Backend inspection and cache-only thumbnails | Native OS cache; a cache miss is a normal result |
| React Timeline Sequence | Five pure clock/lyric operations through the released library | Workspace npm package and React peers; actual playback/editing needs a browser |
| WorkflowMoves | Twenty audited script routes: evidence checks, HTML preparation, outreach claims and six guarded WordPress modes | Operator-selected trusted checkout; WordPress needs its separate PowerShell/site/credential binding |
| MediaSlide | Complete skill, capability/API references and integration requirements | React browser host; no standalone renderer is invented |
| EPK Social Metadata | Complete skill, registered WordPress metadata contract and host requirements | Authorized WordPress REST/editor context with the plugin installed |
| DanceVault | Complete skill, actual WordPress action contract and acceptance requirements | Selected WordPress host; destination-host acceptance remains mandatory |

There are 97 toolkit tools with this source version: the original five, eleven discovery/job/reference helpers, 69 CLI adapters and 12 native-library operations. Installed StemLab contributes its own tools at `tools/list`, with its original input/output schemas and annotations. It is a persistent official-SDK MCP connection, not a new analysis implementation. A tool's presence proves its interface is available; it does not prove that its optional engine or model is installed.

Object-valued local tools return MCP `structuredContent` alongside their JSON text content. Native StemLab results preserve their original structured data, images and error status. Workflows remain portable skill/reference instructions; the hub's job receipts and runtime configuration are DanceFlow-specific contracts, not a separate workflow-language standard.

No operation accepts an arbitrary shell command, executable, Python plugin directory or JavaScript expression. Browser mounting, source installation, plugin deployment and unrestricted native CLI escape hatches remain explicit host operations. This hub does not claim every desktop/UI interaction can execute headlessly.

## Configure runtimes

Develop/test this branch in an isolated environment:

```sh
python -m pip install -e ".[dev]"
danceflow-mcp --workspace /selected/workspace --runtime-config /selected/config/danceflow-runtimes.json
```

`DANCEFLOW_RUNTIME_CONFIG` is the equivalent startup environment variable. Only the server operator can bind runtimes and trusted source code. The JSON file contains paths and site bindings, not inline secrets:

```json
{
  "schema": "danceflow.runtimes.v1",
  "max_jobs": 1,
  "node": "node",
  "powershell": "pwsh",
  "components": {
    "stemlab": {"python": "/runtimes/stemlab/bin/python"},
    "framerudiments": {"python": "/runtimes/framerudiments/bin/python"},
    "workflowmoves": {"source_root": "/trusted/WorkflowMoves"}
  }
}
```

Use the corresponding absolute Windows executable/checkout paths on Windows. Without overrides, Python CLI adapters use the server's interpreter. Install DanceRudiments and ThumbMoves in that interpreter. Install the fixed `@kieransimkin/dancemoves` and `react-timeline-sequence` npm packages and their peers in the selected workspace. The server never runs `pip`, `npm install`, `uvx` or model bootstrap on the caller's behalf.

For the WorkflowMoves WordPress transport, add an operator-owned `wordpress` object with `site_url` (HTTPS) and an absolute `credential_path` for its existing encrypted credential file. PowerShell 7.5+ and the credential's supported host/account are required. MCP inputs cannot replace those bindings. Publication modes still require the original manifest SHA-256, reviewed-source fields, authority fields and a new receipt. A permission flag is an acknowledgment from the caller, not a grant of authority or proof of rights.

Optional `models_dir` localizes generic Hugging Face/Torch/cache environment variables for a CLI/native provider. Tool-specific model-store selection remains owned by each engine; see its documented project-root rules and model-directory parameters. Inspect the actual model store before an authorized download. Never infer that setting a cache environment variable migrates existing weights or overrides every backend.

## Start and inspect a job

Each CLI adapter exposes an `arguments` object with its exact JSON Schema and a `permissions` object. Schema validation rejects unknown parameters and literal strings beginning with command-line option prefixes. Use `./-name` or an absolute path for a filename beginning with a dash; supply negative numeric values as JSON numbers. Paths are normalized against the selected workspace; symlink escapes and overwriting immutable output paths are rejected. Documented state/resume directories are explicit exceptions in their operation metadata.

For example, call `framerudiments_plan` with:

```json
{
  "arguments": {
    "project": "render/project.json",
    "output": "runs/render-plan-001.json"
  },
  "permissions": {"write": true}
}
```

The result is a retained job receipt. Poll `danceflow_job_status`, read `danceflow_job_logs` and inspect reports with `danceflow_read_artifact`. Run preflight and render as separate dependent operations with their own new output directories. A completed process is not visual, audio or creative review.

Possible effect acknowledgements are `write`, `inference`, `download`, `network`, `publication` and `training`. Exact requirements are returned by component discovery. Prism's statistics-only profile requires a local write; selecting optional models or `allow_download` adds the corresponding effects. LikenessForge's CLI can provision models during computation, so its compute routes conservatively require explicit download/network acknowledgement. StemLab retains its own independent consent controls.

Job states distinguish `running`, `completed`, `needs_review`, `failed`, `timed_out`, `cancelled`, `unavailable` and `unknown_after_restart`. An expected nonzero exit becomes `needs_review`: some tools reuse the same exit code for usable partial evidence and invalid inputs, so inspect the actual report and log. Exit zero alone does not establish that every optional backend succeeded.

Receipts and bounded logs live under `.danceflow/jobs/` inside the selected workspace. Writes use atomic receipt replacement; active overlapping output paths are reserved within the server. Logs are capped at eight MiB. There are no automatic retries. A timed-out or failed external mutation has an uncertain remote outcome until independently reconciled. Only an owned process from the current session can be cancelled; a stale receipt never authorizes killing a reused PID.

The host checks temporary-directory create/read/rename/cleanup before jobs. Work happens in trusted installed engines. **This is not an OS sandbox:** a native renderer project, manifest or receipt may reference further assets or configuration. Review that transitive configuration using the owning tool's rules. Use OS isolation when executing untrusted native projects.

## Verification and limits

The test suite exercises real MCP stdio discovery/calls/resources, task-word search, workflow listing and retrieval, optional source coverage and path boundaries, persistent native-provider sessions, schema/result/image passthrough, job lifecycle, consent flags, output ownership and installed-wheel reference discovery. Library adapters also have synthetic error/deadline tests. Canonical engines remain independently tested in their own repositories.

Integration checks for this change exercised published DanceRudiments 0.3.0, ThumbMoves 0.1.2, DanceMoves 3.4.0 and React Timeline Sequence 0.8.0 against synthetic inputs. The CLI registry was checked against the tagged argument parsers linked in its descriptors. These checks do not establish GPU inference, real-song render quality, Windows/macOS thumbnail behavior, physical motion, live WordPress publication or production DanceVault acceptance.
