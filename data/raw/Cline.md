# Cline Changelog


## [3.62.0] - 2026-02-13

### Fixed
- Banners now display immediately when opening the extension instead of requiring user interaction first
- Resolved 17 security vulnerabilities including high-severity DoS issues in dependencies (body-parser, axios, qs, tar, and others)

**Full Changelog**: https://github.com/cline/cline/compare/v3.61.0...v3.62.0


## [3.61.0] - 2026-02-13

- UI/UX fixes with minimax model family

**Full Changelog**: https://github.com/cline/cline/compare/v2.2.2-cli...v3.61.0


## [3.60.0] - 2026-02-13

- Fixes for Minimax model family

**Full Changelog**: https://github.com/cline/cline/compare/v2.2.1-cli...v3.60.0


## [3.59.0] - 2026-02-12

- Added Minimax 2.5 Free Promo
- Fixed Response chaining for OpenAI's Responses API 

**Full Changelog**: https://github.com/cline/cline/compare/cli-build-024bb65...v3.59.0


## [3.58.0] - 2026-02-12

### Added
- Subagent: replace legacy subagents with the native `use_subagents` tool
- Bundle `endpoints.json` support so packaged distributions can ship required endpoints out-of-the-box
- Amazon Bedrock: support parallel tool calling
- New "double-check completion" experimental feature to verify work before marking tasks complete
- CLI: new task controls/flags including custom `--thinking` token budget and `--max-consecutive-mistakes` for yolo runs
- Remote config: new UI/options (including connection/test buttons) and support for syncing deletion of remotely configured MCP servers
- Vertex / Claude Code: add 1M context model options for Claude Opus 4.6
- ZAI/GLM: add GLM-5

### Fixed
- CLI: handle stdin redirection correctly in CI/headless environments
- CLI: preserve OAuth callback paths during auth redirects
- VS Code Web: generate auth callback URLs via `vscode.env.asExternalUri` (OAuth callback reliability)
- Terminal: surface command exit codes in results and improve long-running `execute_command` timeout behavior
- UI: add loading indicator and fix `api_req_started` rendering
- Task streaming: prevent duplicate streamed text rows after completion
- API: preserve selected Vercel model when model metadata is missing
- Telemetry: route PostHog networking through proxy-aware shared fetch and ensure telemetry flushes on shutdown
- CI: increase Windows E2E test timeout to reduce flakiness

### Changed
- Settings/model UX: move "reasoning effort" into model configuration and expose it in settings
- CLI provider selection: limit provider list to those remotely configured
- UI: consolidate ViewHeader component/styling across views
- Tools: add auto-approval support for `attempt_completion` commands
- Remotely configured MCP server schema now supports custom headers

**Full Changelog**: https://github.com/cline/cline/compare/cli-build-6278382...v3.58.0


## [3.57.1] - 2026-02-05

### Fixed

- Fixed Opus 4.6 for bedrock provider

**Full Changelog**: https://github.com/cline/cline/compare/v3.57.0...v3.57.1


## [3.57.0] - 2026-02-05

### Added

- Cline CLI 2.0 now available. Install with `npm install -g cline`
- Anthopic Opus 4.6 
- Minimax-2.1 and Kimi-k2.5 now available for free for a limited time promo
- Codex-5.3 through ChatGPT subscription

### Fixed

- Fix read file tool to support reading large files
- Fix decimal input crash in OpenAI Compatible price fields (#8129)
- Fix build complete handlers when updating the api config
- Fixed missing provider from list
- Fixed Favorite Icon / Star from getting clipped in the task history view

### Changed

- Make skills always enabled and remove feature toggle setting

**Full Changelog**: https://github.com/cline/cline/compare/v2.0.5-cli...v3.57.0


## [3.56.2] - 2026-01-30

### Added

- __CLI authentication:__ Added Vercel AI Gateway and Cline API key provider support for headless CI/automation workflows
- __New model:__ Added Kimi-K2.5 model to Moonshot provider (262K context, image support, prompt caching)
- __Prompt variant:__ Added Trinity Large prompt variant for improved tool-calling support
- __OpenTelemetry:__ Added support for custom headers on metrics and logs endpoints
- __Social links:__ Added community icons (X, Discord, GitHub, Reddit, LinkedIn) to the What's New modal

### Fixed

- __LiteLLM:__ Fixed thinking configuration not appearing for reasoning-capable models
- __OpenTelemetry:__ Fixed endpoint path handling (no longer incorrectly appends `/v1/logs` or `/v1/metrics`) and ensured logs are sent regardless of VSCode telemetry settings
- __CLI auth:__ Fixed `cline auth` displaying incorrect provider information after configuration

### Changed

- __Hooks:__ Hook scripts now run from the workspace repository root instead of filesystem root
- __Default settings:__ Enabled multi-root workspaces, parallel tool calling, and skills by default; disabled strict plan mode by default
- __Settings UI:__ Refreshed feature settings section with collapsible design

**Full Changelog**: https://github.com/cline/cline/compare/v3.56.1...v3.56.2


## [3.56.1] - 2026-01-30

### Added

- __CLI authentication:__ Added Vercel AI Gateway and Cline API key provider support for headless CI/automation workflows
- __New model:__ Added Kimi-K2.5 model to Moonshot provider (262K context, image support, prompt caching)
- __Prompt variant:__ Added Trinity Large prompt variant for improved tool-calling support
- __OpenTelemetry:__ Added support for custom headers on metrics and logs endpoints
- __Social links:__ Added community icons (X, Discord, GitHub, Reddit, LinkedIn) to the What's New modal

### Fixed

- __LiteLLM:__ Fixed thinking configuration not appearing for reasoning-capable models
- __OpenTelemetry:__ Fixed endpoint path handling (no longer incorrectly appends `/v1/logs` or `/v1/metrics`) and ensured logs are sent regardless of VSCode telemetry settings
- __CLI auth:__ Fixed `cline auth` displaying incorrect provider information after configuration

### Changed

- __Hooks:__ Hook scripts now run from the workspace repository root instead of filesystem root
- __Default settings:__ Enabled multi-root workspaces, parallel tool calling, and skills by default; disabled strict plan mode by default
- __Settings UI:__ Refreshed feature settings section with collapsible design

**Full Changelog**: https://github.com/cline/cline/compare/v3.56.0...v3.56.1


## [3.56.0] - 2026-01-30

### Added

- __CLI authentication:__ Added Vercel AI Gateway and Cline API key provider support for headless CI/automation workflows
- __New model:__ Added Kimi-K2.5 model to Moonshot provider (262K context, image support, prompt caching)
- __Prompt variant:__ Added Trinity Large prompt variant for improved tool-calling support
- __OpenTelemetry:__ Added support for custom headers on metrics and logs endpoints
- __Social links:__ Added community icons (X, Discord, GitHub, Reddit, LinkedIn) to the What's New modal

### Fixed

- __LiteLLM:__ Fixed thinking configuration not appearing for reasoning-capable models
- __OpenTelemetry:__ Fixed endpoint path handling (no longer incorrectly appends `/v1/logs` or `/v1/metrics`) and ensured logs are sent regardless of VSCode telemetry settings
- __CLI auth:__ Fixed `cline auth` displaying incorrect provider information after configuration

### Changed

- __Hooks:__ Hook scripts now run from the workspace repository root instead of filesystem root
- __Default settings:__ Enabled multi-root workspaces, parallel tool calling, and skills by default; disabled strict plan mode by default
- __Settings UI:__ Refreshed feature settings section with collapsible design

**Full Changelog**: https://github.com/cline/cline/compare/v3.55.0...v3.56.0


## [3.55.0] - 2026-01-28

- Add new model: Arcee Trinity Large Preview
- Add new model: Moonshot Kimi K2.5
- Add MCP prompts support - prompts from connected MCP servers now appear in slash command autocomplete as `/mcp:<server>:<prompt>`

**Full Changelog**: https://github.com/cline/cline/compare/v3.54.0...v3.55.0


## [3.54.0] - 2026-01-27

### Added

- Native tool calls support for Ollama provider
- Sonnet 4.5 is now the default Amazon Bedrock model id

### Fixed

- Prevent infinite retry loops when replace_in_file fails repeatedly. The system now detects repeated failures and provides better guidance to break out of retry cycles.
- Skip diff error UI handling during streaming to prevent flickering. Error handling is deferred until streaming completes.
- Strip notebook cell outputs when extracting text content from Jupyter notebooks, significantly reducing context size sent to the LLM.
- Throttle diff view updates during streaming to reduce UI flickering and improve performance.

### Changed

- Removed Mistral's Devstral-2512 free from the free models list
- Removed deprecated zai-glm-4.6 model from Cerebras provider

**Full Changelog**: https://github.com/cline/cline/compare/v3.53.1...v3.54.0


## [3.53.1] - 2026-01-24

### Fixed
 - Bug in responses API

**Full Changelog**: https://github.com/cline/cline/compare/v3.53.0...v3.53.1


## [3.53.0] - 2026-01-23

### Fixed
 - Removed grok model from free tier

**Full Changelog**: https://github.com/cline/cline/compare/v3.52.0...v3.53.0

