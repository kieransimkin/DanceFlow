# KeywordMoves: capability and package reference

Audited 23 October 2026: **v0.5.8**, exact source [`e07db45c506d1b31a9a6d8703130c150723fd5b1`](https://github.com/kieransimkin/keywordmoves/tree/e07db45c506d1b31a9a6d8703130c150723fd5b1). This is a dated source/documentation audit, not installed-runtime or end-to-end acceptance. [Check current releases before use](../workflows/release-preflight.md).

## Current README feature routes

- [Agents and contributors](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#agents-and-contributors)
- [Current plugins](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#current-plugins)
- [Credentials](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#credentials)
- [Install](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#install)
- [Use](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#use)
- [Extract proper nouns and noun chunks with spaCy](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#extract-proper-nouns-and-noun-chunks-with-spacy)
- [Extract with NLTK](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#extract-with-nltk)
- [Rank reference-text phrases with KeyBERT](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#rank-reference-text-phrases-with-keybert)
- [Use OpenAI models](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#use-openai-models)
- [Online keyword sources](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#online-keyword-sources)
- [Write a keyword plugin](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#write-a-keyword-plugin)
- [Write an LLM plugin](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#write-an-llm-plugin)
- [Development](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#development)
- [Bundled skill](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#bundled-skill)
- [Monitor keyword evidence over time](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#monitor-keyword-evidence-over-time)
- [Current limitations and integration notes](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md#current-limitations-and-integration-notes)

## Source documentation and examples

- [`README.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md)
- [`docs/authenticated-access.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/authenticated-access.md)
- [`docs/automatic-free-collection.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/automatic-free-collection.md)
- [`docs/bing-search.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/bing-search.md)
- [`docs/branding/README.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/branding/README.md)
- [`docs/browser-observations.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/browser-observations.md)
- [`docs/candidate-context.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/candidate-context.md)
- [`docs/candidate-shortlist.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/candidate-shortlist.md)
- [`docs/credentials.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/credentials.md)
- [`docs/free-public-source-modules.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/free-public-source-modules.md)
- [`docs/free-youtube-volume-sources.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/free-youtube-volume-sources.md)
- [`docs/google-search.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/google-search.md)
- [`docs/instagram.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/instagram.md)
- [`docs/keybert.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/keybert.md)
- [`docs/keywordmoves-local-privacy.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/keywordmoves-local-privacy.md)
- [`docs/keywordmoves-local-terms.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/keywordmoves-local-terms.md)
- [`docs/literal-text.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/literal-text.md)
- [`docs/monitoring.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/monitoring.md)
- [`docs/multi-source-research.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/multi-source-research.md)
- [`docs/native-export.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/native-export.md)
- [`docs/nltk.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/nltk.md)
- [`docs/online-sources.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/online-sources.md)
- [`docs/openai.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/openai.md)
- [`docs/platform-client-notices.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/platform-client-notices.md)
- [`docs/plugin-opportunities.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/plugin-opportunities.md)
- [`docs/pypi-publication.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/pypi-publication.md)
- [`docs/reddit.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/reddit.md)
- [`docs/spacy.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/spacy.md)
- [`docs/tiktok.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/tiktok.md)
- [`docs/trends-demand-assessment.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/trends-demand-assessment.md)
- [`docs/vidiq-benchmark.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/vidiq-benchmark.md)
- [`docs/youtube-demand-sources.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/youtube-demand-sources.md)
- [`docs/youtube.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/docs/youtube.md)

## Package evidence

- [`README.md`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/README.md) — SHA-256 `32f5c3a7556bcb0e8812fff1c10cfcc47b0a72a02792550bca965870473f5c19`.
- [`pyproject.toml`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/pyproject.toml) — SHA-256 `862a40206c6738be8d8041932518fbea08a9b42d11af90583261d8aa72020f71`.
- [`MANIFEST.in`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/MANIFEST.in) — SHA-256 `ccec2f38fd33c38e3ea2c0a9b85805c6fe3c42b0aea4ada6fbd289c8aa73d0d6`.
- [`LICENSE`](https://github.com/kieransimkin/keywordmoves/blob/e07db45c506d1b31a9a6d8703130c150723fd5b1/LICENSE) — SHA-256 `7f353aca65f8e26252d5785218c8c8329f819172e8c35b5dd62b4ebb981abf34`.

Package files were read at the pinned source. Published distributions, installed identity, working host examples, rights and reviewed output require their own verification.

## Historical detailed reference

The following older index is retained for detailed routes. Its earlier version is historical; the audited source links above identify current documented availability.

# keywordmoves: complete capability reference

Inspected stable source: [v0.5.8](https://github.com/kieransimkin/keywordmoves/releases/tag/v0.5.8), commit `e07db45c506d1b31a9a6d8703130c150723fd5b1`. This is a dated baseline; [check current releases before every new workflow](../workflows/release-preflight.md).

## Choose and use a route

| Goal | Supported route and evidence |
|---|---|
| Discover available sources | Inspect keyword/LLM plugin discovery, source-native workbenches and the module operation help. Literal extraction, NLP salience and semantic proposals have different evidence meaning. |
| Collect or import | Choose permitted first-party/provider reads, native CSV/HTML exports or dated reviewed observations. Use source-specific Google/Bing/Trends/social routes; no unsupported scraper is implied. |
| Compare evidence | Use compatible source/geography/period/unit snapshots, monitors, focus/shortlist and research batches. Relative interest, local phrase frequency, paid estimates and actual native demand remain distinct. |
| Extend a genuine gap | Implement a plugin or provider in the canonical registry with permitted fixtures; preserve explicit credentials, costs and source limits. Live and paid routes are not exposed by the hub MCP bridge. |

## Released reference coverage

Each entry links to the exact released explanation, options, example or limitation. These are documented capabilities, not a claim that every option was run on this computer. Review the relevant source before configuring it.

- [Agents and contributors](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#agents-and-contributors) — `README.md`.
- [Current plugins](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#current-plugins) — `README.md`.
- [Credentials](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#credentials) — `README.md`.
- [Install](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#install) — `README.md`.
- [Use](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#use) — `README.md`.
- [Extract proper nouns and noun chunks with spaCy](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#extract-proper-nouns-and-noun-chunks-with-spacy) — `README.md`.
- [Extract with NLTK](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#extract-with-nltk) — `README.md`.
- [Rank reference-text phrases with KeyBERT](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#rank-reference-text-phrases-with-keybert) — `README.md`.
- [Use OpenAI models](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#use-openai-models) — `README.md`.
- [Online keyword sources](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#online-keyword-sources) — `README.md`.
- [Write a keyword plugin](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#write-a-keyword-plugin) — `README.md`.
- [Write an LLM plugin](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#write-an-llm-plugin) — `README.md`.
- [Development](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#development) — `README.md`.
- [Bundled skill](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#bundled-skill) — `README.md`.
- [Monitor keyword evidence over time](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#monitor-keyword-evidence-over-time) — `README.md`.
- [Current limitations and integration notes](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/README.md#current-limitations-and-integration-notes) — `README.md`.
- [Authenticated platform access](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/authenticated-access.md#authenticated-platform-access) — `docs/authenticated-access.md`.
- [App notices and consent](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/authenticated-access.md#app-notices-and-consent) — `docs/authenticated-access.md`.
- [First-party credentials and scope](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/authenticated-access.md#first-party-credentials-and-scope) — `docs/authenticated-access.md`.
- [Cross-platform secret storage](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/authenticated-access.md#cross-platform-secret-storage) — `docs/authenticated-access.md`.
- [Bounded verification and evidence](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/authenticated-access.md#bounded-verification-and-evidence) — `docs/authenticated-access.md`.
- [Primary references](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/authenticated-access.md#primary-references) — `docs/authenticated-access.md`.
- [Automatic free-source collection](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/automatic-free-collection.md#automatic-free-source-collection) — `docs/automatic-free-collection.md`.
- [Direct collection](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/automatic-free-collection.md#direct-collection) — `docs/automatic-free-collection.md`.
- [Connected-browser collection](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/automatic-free-collection.md#connected-browser-collection) — `docs/automatic-free-collection.md`.
- [Composition and verification](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/automatic-free-collection.md#composition-and-verification) — `docs/automatic-free-collection.md`.
- [Google Trends native downloads (0.5.6)](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/automatic-free-collection.md#google-trends-native-downloads-056) — `docs/automatic-free-collection.md`.
- [Bing Search discovery and analysis](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#bing-search-discovery-and-analysis) — `docs/bing-search.md`.
- [API access status matters](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#api-access-status-matters) — `docs/bing-search.md`.
- [Installation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#installation) — `docs/bing-search.md`.
- [Credentials and secret handling](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#credentials-and-secret-handling) — `docs/bing-search.md`.
- [Bing Webmaster module](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#bing-webmaster-module) — `docs/bing-search.md`.
- [Native operation matrix](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#native-operation-matrix) — `docs/bing-search.md`.
- [Native market keyword research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#native-market-keyword-research) — `docs/bing-search.md`.
- [Query opportunities and query/page overlap](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#query-opportunities-and-querypage-overlap) — `docs/bing-search.md`.
- [Bing search results and organic competition](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#bing-search-results-and-organic-competition) — `docs/bing-search.md`.
- [Competition output](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#competition-output) — `docs/bing-search.md`.
- [Autocomplete and provider suggestions](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#autocomplete-and-provider-suggestions) — `docs/bing-search.md`.
- [Documented Keyword Tool route](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#documented-keyword-tool-route) — `docs/bing-search.md`.
- [Experimental browser autocomplete](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#experimental-browser-autocomplete) — `docs/bing-search.md`.
- [Popularity estimates and competitor keywords](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#popularity-estimates-and-competitor-keywords) — `docs/bing-search.md`.
- [DataForSEO routes](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#dataforseo-routes) — `docs/bing-search.md`.
- [Keyword Tool volume route](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#keyword-tool-volume-route) — `docs/bing-search.md`.
- [Local schemas and analysis operations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#local-schemas-and-analysis-operations) — `docs/bing-search.md`.
- [Webmaster interchange](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#webmaster-interchange) — `docs/bing-search.md`.
- [Search-result interchange](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#search-result-interchange) — `docs/bing-search.md`.
- [Other dated observations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#other-dated-observations) — `docs/bing-search.md`.
- [Transport limits and operational controls](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#transport-limits-and-operational-controls) — `docs/bing-search.md`.
- [Coverage boundaries](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#coverage-boundaries) — `docs/bing-search.md`.
- [Offline demonstration and tests](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#offline-demonstration-and-tests) — `docs/bing-search.md`.
- [Primary references](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/bing-search.md#primary-references) — `docs/bing-search.md`.
- [Reviewed browser observations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/browser-observations.md#reviewed-browser-observations) — `docs/browser-observations.md`.
- [Require listening intent and topic together](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/candidate-context.md#require-listening-intent-and-topic-together) — `docs/candidate-context.md`.
- [Explicit shortlist review](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/candidate-shortlist.md#explicit-shortlist-review) — `docs/candidate-shortlist.md`.
- [Credential configuration](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/credentials.md#credential-configuration) — `docs/credentials.md`.
- [Install and select an OS store](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/credentials.md#install-and-select-an-os-store) — `docs/credentials.md`.
- [Account profiles and environment configuration](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/credentials.md#account-profiles-and-environment-configuration) — `docs/credentials.md`.
- [Existing environment and CLI routes](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/credentials.md#existing-environment-and-cli-routes) — `docs/credentials.md`.
- [Library composition and token renewal](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/credentials.md#library-composition-and-token-renewal) — `docs/credentials.md`.
- [Verification](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/credentials.md#verification) — `docs/credentials.md`.
- [Reviewed free public-source modules](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-public-source-modules.md#reviewed-free-public-source-modules) — `docs/free-public-source-modules.md`.
- [Working routes](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-public-source-modules.md#working-routes) — `docs/free-public-source-modules.md`.
- [Capture and run](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-public-source-modules.md#capture-and-run) — `docs/free-public-source-modules.md`.
- [Metric semantics](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-public-source-modules.md#metric-semantics) — `docs/free-public-source-modules.md`.
- [Composition and example](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-public-source-modules.md#composition-and-example) — `docs/free-public-source-modules.md`.
- [Reviewed routes not integrated](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-public-source-modules.md#reviewed-routes-not-integrated) — `docs/free-public-source-modules.md`.
- [Free YouTube search-volume source audit](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-youtube-volume-sources.md#free-youtube-search-volume-source-audit) — `docs/free-youtube-volume-sources.md`.
- [Working public feed](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-youtube-volume-sources.md#working-public-feed) — `docs/free-youtube-volume-sources.md`.
- [Other candidates](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-youtube-volume-sources.md#other-candidates) — `docs/free-youtube-volume-sources.md`.
- [Admission checks for a new source](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/free-youtube-volume-sources.md#admission-checks-for-a-new-source) — `docs/free-youtube-volume-sources.md`.
- [Google Search keyword discovery and analysis](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#google-search-keyword-discovery-and-analysis) — `docs/google-search.md`.
- [The three questions that must stay separate](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#the-three-questions-that-must-stay-separate) — `docs/google-search.md`.
- [Installation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#installation) — `docs/google-search.md`.
- [Operation matrix: 35 implemented operations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#operation-matrix-35-implemented-operations) — `docs/google-search.md`.
- [Shared controls, credentials and preservation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#shared-controls-credentials-and-preservation) — `docs/google-search.md`.
- [Geography is intentionally not one interchangeable code](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#geography-is-intentionally-not-one-interchangeable-code) — `docs/google-search.md`.
- [Search Console: setup and query workflows](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#search-console-setup-and-query-workflows) — `docs/google-search.md`.
- [Opportunities and query/page overlap](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#opportunities-and-querypage-overlap) — `docs/google-search.md`.
- [Inventory, inspections and bulk export](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#inventory-inspections-and-bulk-export) — `docs/google-search.md`.
- [Search Console import contracts](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#search-console-import-contracts) — `docs/google-search.md`.
- [Search-result competition and rank checking](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#search-result-competition-and-rank-checking) — `docs/google-search.md`.
- [Organic difficulty and backlink context](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#organic-difficulty-and-backlink-context) — `docs/google-search.md`.
- [Autocomplete, People Also Ask and related searches](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#autocomplete-people-also-ask-and-related-searches) — `docs/google-search.md`.
- [Planning estimates and keyword expansion](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#planning-estimates-and-keyword-expansion) — `docs/google-search.md`.
- [Trends, technical review and legacy search](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#trends-technical-review-and-legacy-search) — `docs/google-search.md`.
- [Offline evidence, schemas and workflow composition](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#offline-evidence-schemas-and-workflow-composition) — `docs/google-search.md`.
- [Offline demonstration](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#offline-demonstration) — `docs/google-search.md`.
- [Other avenues and explicit limits](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#other-avenues-and-explicit-limits) — `docs/google-search.md`.
- [Tests and failure handling](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#tests-and-failure-handling) — `docs/google-search.md`.
- [Primary references](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#primary-references) — `docs/google-search.md`.
- [Related Trends CSV exports](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/google-search.md#related-trends-csv-exports) — `docs/google-search.md`.
- [Instagram hashtag and keyword research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#instagram-hashtag-and-keyword-research) — `docs/instagram.md`.
- [The important distinction: what “popular” means](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#the-important-distinction-what-popular-means) — `docs/instagram.md`.
- [Install and list operations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#install-and-list-operations) — `docs/instagram.md`.
- [1. Find literal tags in reference text](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#1-find-literal-tags-in-reference-text) — `docs/instagram.md`.
- [2. Discover related hashtags and estimated demand](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#2-discover-related-hashtags-and-estimated-demand) — `docs/instagram.md`.
- [3. Resolve known hashtags and inspect their media with Meta](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#3-resolve-known-hashtags-and-inspect-their-media-with-meta) — `docs/instagram.md`.
- [Check rolling hashtag usage](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#check-rolling-hashtag-usage) — `docs/instagram.md`.
- [Resolve and analyse a tag](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#resolve-and-analyse-a-tag) — `docs/instagram.md`.
- [Professional account, competitor, profile and caption research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#professional-account-competitor-profile-and-caption-research) — `docs/instagram.md`.
- [Owned-media insights and comments](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#owned-media-insights-and-comments) — `docs/instagram.md`.
- [4. Broader hashtag, keyword and Reel discovery through Apify](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#4-broader-hashtag-keyword-and-reel-discovery-through-apify) — `docs/instagram.md`.
- [Start explicitly, then fetch separately](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#start-explicitly-then-fetch-separately) — `docs/instagram.md`.
- [5. Browser observations and exports](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#5-browser-observations-and-exports) — `docs/instagram.md`.
- [JSON and CSV](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#json-and-csv) — `docs/instagram.md`.
- [Explicit saved-HTML selectors](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#explicit-saved-html-selectors) — `docs/instagram.md`.
- [Direct public hashtag page: deliberately experimental](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#direct-public-hashtag-page-deliberately-experimental) — `docs/instagram.md`.
- [6. Measure change between comparable snapshots](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#6-measure-change-between-comparable-snapshots) — `docs/instagram.md`.
- [Coverage of other possible research avenues](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#coverage-of-other-possible-research-avenues) — `docs/instagram.md`.
- [Processing limits, provenance and privacy](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#processing-limits-provenance-and-privacy) — `docs/instagram.md`.
- [Tests and verification](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#tests-and-verification) — `docs/instagram.md`.
- [Sources and contract references](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/instagram.md#sources-and-contract-references) — `docs/instagram.md`.
- [KeyBERT keyword plugin](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#keybert-keyword-plugin) — `docs/keybert.md`.
- [Install](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#install) — `docs/keybert.md`.
- [Basic extraction](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#basic-extraction) — `docs/keybert.md`.
- [Selection methods](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#selection-methods) — `docs/keybert.md`.
- [Literal candidates and provenance](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#literal-candidates-and-provenance) — `docs/keybert.md`.
- [Rank a restricted vocabulary](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#rank-a-restricted-vocabulary) — `docs/keybert.md`.
- [Models, cache and offline use](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#models-cache-and-offline-use) — `docs/keybert.md`.
- [Long text and resource limits](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#long-text-and-resource-limits) — `docs/keybert.md`.
- [Options](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#options) — `docs/keybert.md`.
- [Tests](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#tests) — `docs/keybert.md`.
- [Sources](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keybert.md#sources) — `docs/keybert.md`.
- [KeywordMoves Local privacy notice](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keywordmoves-local-privacy.md#keywordmoves-local-privacy-notice) — `docs/keywordmoves-local-privacy.md`.
- [Purpose and information accessed](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keywordmoves-local-privacy.md#purpose-and-information-accessed) — `docs/keywordmoves-local-privacy.md`.
- [Local storage, use and sharing](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keywordmoves-local-privacy.md#local-storage-use-and-sharing) — `docs/keywordmoves-local-privacy.md`.
- [Consent, control and deletion](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keywordmoves-local-privacy.md#consent-control-and-deletion) — `docs/keywordmoves-local-privacy.md`.
- [KeywordMoves Local terms of use](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/keywordmoves-local-terms.md#keywordmoves-local-terms-of-use) — `docs/keywordmoves-local-terms.md`.
- [Literal source phrase extraction](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/literal-text.md#literal-source-phrase-extraction) — `docs/literal-text.md`.
- [Keyword demand monitoring](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#keyword-demand-monitoring) — `docs/monitoring.md`.
- [Quick start without accounts or network access](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#quick-start-without-accounts-or-network-access) — `docs/monitoring.md`.
- [Watchlist](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#watchlist) — `docs/monitoring.md`.
- [Observations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#observations) — `docs/monitoring.md`.
- [Existing evidence and native exports](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#existing-evidence-and-native-exports) — `docs/monitoring.md`.
- [History and provenance](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#history-and-provenance) — `docs/monitoring.md`.
- [Coverage and alerts](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#coverage-and-alerts) — `docs/monitoring.md`.
- [Due plans and collection](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#due-plans-and-collection) — `docs/monitoring.md`.
- [Scheduling and retention](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#scheduling-and-retention) — `docs/monitoring.md`.
- [Verifying retained captures](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#verifying-retained-captures) — `docs/monitoring.md`.
- [Compatibility with reviewed browser observations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/monitoring.md#compatibility-with-reviewed-browser-observations) — `docs/monitoring.md`.
- [Multi-source research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#multi-source-research) — `docs/multi-source-research.md`.
- [Access and useful evidence](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#access-and-useful-evidence) — `docs/multi-source-research.md`.
- [Explicit research batches](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#explicit-research-batches) — `docs/multi-source-research.md`.
- [Added source contracts](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#added-source-contracts) — `docs/multi-source-research.md`.
- [SE Ranking](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#se-ranking) — `docs/multi-source-research.md`.
- [Wikimedia Pageviews](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#wikimedia-pageviews) — `docs/multi-source-research.md`.
- [Apple iTunes catalogue](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#apple-itunes-catalogue) — `docs/multi-source-research.md`.
- [Datamuse context](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#datamuse-context) — `docs/multi-source-research.md`.
- [Target review](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#target-review) — `docs/multi-source-research.md`.
- [Potential problems](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#potential-problems) — `docs/multi-source-research.md`.
- [Primary sources](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/multi-source-research.md#primary-sources) — `docs/multi-source-research.md`.
- [Reviewed native CSV exports](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/native-export.md#reviewed-native-csv-exports) — `docs/native-export.md`.
- [Platform coverage](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/native-export.md#platform-coverage) — `docs/native-export.md`.
- [NLTK keyword extraction](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#nltk-keyword-extraction) — `docs/nltk.md`.
- [Installation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#installation) — `docs/nltk.md`.
- [Custom data directory or offline use](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#custom-data-directory-or-offline-use) — `docs/nltk.md`.
- [Use](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#use) — `docs/nltk.md`.
- [Detectors and normalisation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#detectors-and-normalisation) — `docs/nltk.md`.
- [Options](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#options) — `docs/nltk.md`.
- [Evidence, offsets and ranking](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#evidence-offsets-and-ranking) — `docs/nltk.md`.
- [Input boundaries and limitations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#input-boundaries-and-limitations) — `docs/nltk.md`.
- [Tests](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#tests) — `docs/nltk.md`.
- [References checked](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/nltk.md#references-checked) — `docs/nltk.md`.
- [Online keyword discovery and analysis](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#online-keyword-discovery-and-analysis) — `docs/online-sources.md`.
- [Installation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#installation) — `docs/online-sources.md`.
- [Provider and access matrix](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#provider-and-access-matrix) — `docs/online-sources.md`.
- [Credentials](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#credentials) — `docs/online-sources.md`.
- [Common limits and result semantics](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#common-limits-and-result-semantics) — `docs/online-sources.md`.
- [Google Ads: planning ideas and historical metrics](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#google-ads-planning-ideas-and-historical-metrics) — `docs/online-sources.md`.
- [Search Console: observed queries for your own property](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#search-console-observed-queries-for-your-own-property) — `docs/online-sources.md`.
- [DataForSEO Labs](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#dataforseo-labs) — `docs/online-sources.md`.
- [Semrush](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#semrush) — `docs/online-sources.md`.
- [Ahrefs](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#ahrefs) — `docs/online-sources.md`.
- [Keyword Tool: multi-platform suggestions and volume](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#keyword-tool-multi-platform-suggestions-and-volume) — `docs/online-sources.md`.
- [Keywords Everywhere](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#keywords-everywhere) — `docs/online-sources.md`.
- [AlsoAsked](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#alsoasked) — `docs/online-sources.md`.
- [SerpApi](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#serpapi) — `docs/online-sources.md`.
- [Brave Suggest](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#brave-suggest) — `docs/online-sources.md`.
- [Datamuse and Wikipedia](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#datamuse-and-wikipedia) — `docs/online-sources.md`.
- [Direct website access](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#direct-website-access) — `docs/online-sources.md`.
- [Browser autocomplete endpoints: experimental and opt-in](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#browser-autocomplete-endpoints-experimental-and-opt-in) — `docs/online-sources.md`.
- [Public static HTML: `website-keywords`](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#public-static-html-website-keywords) — `docs/online-sources.md`.
- [Saved rendered HTML](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#saved-rendered-html) — `docs/online-sources.md`.
- [Ubersuggest and AnswerThePublic: report import, not invented scrapers](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#ubersuggest-and-answerthepublic-report-import-not-invented-scrapers) — `docs/online-sources.md`.
- [Reusing local candidates](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#reusing-local-candidates) — `docs/online-sources.md`.
- [Tests and implementation limits](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#tests-and-implementation-limits) — `docs/online-sources.md`.
- [Primary sources and verification trail](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#primary-sources-and-verification-trail) — `docs/online-sources.md`.
- [TikTok-specific discovery and analysis](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#tiktok-specific-discovery-and-analysis) — `docs/online-sources.md`.
- [YouTube-specific research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#youtube-specific-research) — `docs/online-sources.md`.
- [Google Search workbench](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#google-search-workbench) — `docs/online-sources.md`.
- [Bing Search workbench](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/online-sources.md#bing-search-workbench) — `docs/online-sources.md`.
- [OpenAI LLM plugin](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#openai-llm-plugin) — `docs/openai.md`.
- [Installation and selection](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#installation-and-selection) — `docs/openai.md`.
- [API keys](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#api-keys) — `docs/openai.md`.
- [PowerShell](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#powershell) — `docs/openai.md`.
- [Bash / zsh](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#bash--zsh) — `docs/openai.md`.
- [Command-line key](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#command-line-key) — `docs/openai.md`.
- [Options](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#options) — `docs/openai.md`.
- [Python](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#python) — `docs/openai.md`.
- [Hosted data, usage and output](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#hosted-data-usage-and-output) — `docs/openai.md`.
- [Troubleshooting](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#troubleshooting) — `docs/openai.md`.
- [Tests and sources](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/openai.md#tests-and-sources) — `docs/openai.md`.
- [Notices for an authenticated platform client](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/platform-client-notices.md#notices-for-an-authenticated-platform-client) — `docs/platform-client-notices.md`.
- [Plugin opportunities](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/plugin-opportunities.md#plugin-opportunities) — `docs/plugin-opportunities.md`.
- [Source notes](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/plugin-opportunities.md#source-notes) — `docs/plugin-opportunities.md`.
- [Recommended build order](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/plugin-opportunities.md#recommended-build-order) — `docs/plugin-opportunities.md`.
- [PyPI publication](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/pypi-publication.md#pypi-publication) — `docs/pypi-publication.md`.
- [Reddit keyword, community and conversation research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#reddit-keyword-community-and-conversation-research) — `docs/reddit.md`.
- [Access status: read this before configuring a live source](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#access-status-read-this-before-configuring-a-live-source) — `docs/reddit.md`.
- [Installation and registration](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#installation-and-registration) — `docs/reddit.md`.
- [Operation inventory](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#operation-inventory) — `docs/reddit.md`.
- [Approved native OAuth reads](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#approved-native-oauth-reads) — `docs/reddit.md`.
- [Providers and analysis](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#providers-and-analysis) — `docs/reddit.md`.
- [Native setup and examples](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#native-setup-and-examples) — `docs/reddit.md`.
- [Pagination and comments](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#pagination-and-comments) — `docs/reddit.md`.
- [What the analyser measures](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#what-the-analyser-measures) — `docs/reddit.md`.
- [Analysis options](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#analysis-options) — `docs/reddit.md`.
- [Provider suggestions and estimated demand](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#provider-suggestions-and-estimated-demand) — `docs/reddit.md`.
- [Explicit third-party collection through Apify](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#explicit-third-party-collection-through-apify) — `docs/reddit.md`.
- [Imports, comparison, and data lifecycle](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#imports-comparison-and-data-lifecycle) — `docs/reddit.md`.
- [Explicit source observations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#explicit-source-observations) — `docs/reddit.md`.
- [Refresh and remove source data](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#refresh-and-remove-source-data) — `docs/reddit.md`.
- [Further avenues: researched, not silently implied as integrations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#further-avenues-researched-not-silently-implied-as-integrations) — `docs/reddit.md`.
- [Testing and a reproducible offline demonstration](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#testing-and-a-reproducible-offline-demonstration) — `docs/reddit.md`.
- [Primary references checked](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/reddit.md#primary-references-checked) — `docs/reddit.md`.
- [spaCy keyword extraction](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#spacy-keyword-extraction) — `docs/spacy.md`.
- [Install](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#install) — `docs/spacy.md`.
- [Reference text](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#reference-text) — `docs/spacy.md`.
- [What is extracted](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#what-is-extracted) — `docs/spacy.md`.
- [Filtering and normalisation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#filtering-and-normalisation) — `docs/spacy.md`.
- [Options](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#options) — `docs/spacy.md`.
- [Evidence, scores and source positions](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#evidence-scores-and-source-positions) — `docs/spacy.md`.
- [Python API](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#python-api) — `docs/spacy.md`.
- [Tests](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#tests) — `docs/spacy.md`.
- [Primary references](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/spacy.md#primary-references) — `docs/spacy.md`.
- [TikTok keyword discovery and evidence analysis](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#tiktok-keyword-discovery-and-evidence-analysis) — `docs/tiktok.md`.
- [Scope and the important distinctions](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#scope-and-the-important-distinctions) — `docs/tiktok.md`.
- [Installation](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#installation) — `docs/tiktok.md`.
- [Operations and access requirements](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#operations-and-access-requirements) — `docs/tiktok.md`.
- [Known hashtags and reported popularity](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#known-hashtags-and-reported-popularity) — `docs/tiktok.md`.
- [Submit a hashtag-analytics collection](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#submit-a-hashtag-analytics-collection) — `docs/tiktok.md`.
- [Other collection presets](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#other-collection-presets) — `docs/tiktok.md`.
- [TikTok keyword suggestions and search estimates](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#tiktok-keyword-suggestions-and-search-estimates) — `docs/tiktok.md`.
- [Own-account analysis through the Display API](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#own-account-analysis-through-the-display-api) — `docs/tiktok.md`.
- [Approved Research API operations](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#approved-research-api-operations) — `docs/tiktok.md`.
- [Advertising-language research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#advertising-language-research) — `docs/tiktok.md`.
- [Native website and in-app routes](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#native-website-and-in-app-routes) — `docs/tiktok.md`.
- [Public hashtag page and oEmbed](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#public-hashtag-page-and-oembed) — `docs/tiktok.md`.
- [Creative Center, Search Insights, Studio and other providers](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#creative-center-search-insights-studio-and-other-providers) — `docs/tiktok.md`.
- [Local imports and cross-provider provenance](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#local-imports-and-cross-provider-provenance) — `docs/tiktok.md`.
- [Saved HTML](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#saved-html) — `docs/tiktok.md`.
- [What the analyser calculates](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#what-the-analyser-calculates) — `docs/tiktok.md`.
- [Snapshot comparisons](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#snapshot-comparisons) — `docs/tiktok.md`.
- [Configuration and limits](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#configuration-and-limits) — `docs/tiktok.md`.
- [Tests and offline demonstration](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#tests-and-offline-demonstration) — `docs/tiktok.md`.
- [Research references](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/tiktok.md#research-references) — `docs/tiktok.md`.
- [Native relative-demand assessment](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/trends-demand-assessment.md#native-relative-demand-assessment) — `docs/trends-demand-assessment.md`.
- [Visible source display failure](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/trends-demand-assessment.md#visible-source-display-failure) — `docs/trends-demand-assessment.md`.
- [Importing vidIQ and reviewing phrase fit](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/vidiq-benchmark.md#importing-vidiq-and-reviewing-phrase-fit) — `docs/vidiq-benchmark.md`.
- [A fair comparison](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/vidiq-benchmark.md#a-fair-comparison) — `docs/vidiq-benchmark.md`.
- [YouTube demand sources](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube-demand-sources.md#youtube-demand-sources) — `docs/youtube-demand-sources.md`.
- [Free YouTube relative interest](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube-demand-sources.md#free-youtube-relative-interest) — `docs/youtube-demand-sources.md`.
- [Independent provider imports, when authorised data exist](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube-demand-sources.md#independent-provider-imports-when-authorised-data-exist) — `docs/youtube-demand-sources.md`.
- [YouTube keyword, hashtag and audience-language research](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#youtube-keyword-hashtag-and-audience-language-research) — `docs/youtube.md`.
- [Install and list](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#install-and-list) — `docs/youtube.md`.
- [Evidence: what "popular" can mean](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#evidence-what-popular-can-mean) — `docs/youtube.md`.
- [Sample analysis](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#sample-analysis) — `docs/youtube.md`.
- [API-derived statistics and retention](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#api-derived-statistics-and-retention) — `docs/youtube.md`.
- [Operation reference](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#operation-reference) — `docs/youtube.md`.
- [Official YouTube Data API](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#official-youtube-data-api) — `docs/youtube.md`.
- [Authorised Analytics API](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#authorised-analytics-api) — `docs/youtube.md`.
- [Provider APIs and experimental web routes](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#provider-apis-and-experimental-web-routes) — `docs/youtube.md`.
- [Apify collection: submit, then fetch](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#apify-collection-submit-then-fetch) — `docs/youtube.md`.
- [Local analysis, exports and browser evidence](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#local-analysis-exports-and-browser-evidence) — `docs/youtube.md`.
- [Snapshot comparison](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#snapshot-comparison) — `docs/youtube.md`.
- [Other discovery avenues and actual coverage](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#other-discovery-avenues-and-actual-coverage) — `docs/youtube.md`.
- [Limits, failures and privacy](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#limits-failures-and-privacy) — `docs/youtube.md`.
- [Tests and offline demonstration](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#tests-and-offline-demonstration) — `docs/youtube.md`.
- [Sources checked](https://github.com/kieransimkin/keywordmoves/blob/v0.5.8/docs/youtube.md#sources-checked) — `docs/youtube.md`.

## Examples and media

Use the runnable examples and actual screenshots/videos linked from the released references. Keep their documented version/context and distinguish synthetic fixtures, model hypotheses and real captured output. Do not represent a guide link as proof that a model, GPU, physical phone or production host was tested. New decorative generated imagery adds no feature evidence to this reference index.

## Default-branch availability

The official default branch was also inspected at [`46100c92ef88032537982a0eeb5413920b8072ac`](https://github.com/kieransimkin/keywordmoves/tree/46100c92ef88032537982a0eeb5413920b8072ac). It differs from the audited stable tag. [Read that exact README](https://github.com/kieransimkin/keywordmoves/blob/46100c92ef88032537982a0eeb5413920b8072ac/README.md) for later source/documentation work; this does not establish a newer release, registry version or installed runtime.
