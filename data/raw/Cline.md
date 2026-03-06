# Cline Changelog


## [3.70.0] - 2026-03-04

### Added

- New Cline API docs: Getting Started, Auth, Chat Completions, Models, Errors, and SDK Examples
- Hook payloads now include `model.provider` and `model.slug` 
- Token/cost updates now happen immediately as usage chunks arrive, not after tool execution

### Fixed

- Improve subagent context compaction logic
- Subagent stream retry delay increased to reduce noise from transient failures
- State serialization errors are now caught and logged instead of crashing
- Removed incorrect `max_tokens` from OpenRouter requests

### Changed

- Windows test cleanup now retries on locked files and applies per-test timeouts
- Updated hooks docs 

**Full Changelog**: https://github.com/cline/cline/compare/v2.5.2-cli...v3.70.0


## [3.69.0] - 2026-03-03

### Added

- Add `User-Agent` header to requests sent to the Cline backend
- Add default auto-tag workflow for publish release flow
- Show Cline SDK docs on the Cline page

### Fixed

- Retry nested git restore and prevent silent `.git_disabled` leftovers in checkpoints
- Prevent Chinese filename escaping in diff view
- Trigger auto-compaction on OpenRouter context overflow errors
- Restore GPT-OSS native file editing on OpenAI-compatible models

### Changed

- Update Cline SDK docs
- Improve hooks support for Windows PowerShell

**Full Changelog**: https://github.com/cline/cline/compare/v2.5.1-cli...v3.69.0


## [3.68.0] - 2026-02-27

### Added

- Add dynamic Cline provider model fetching from Cline endpoint
- Add additional Markdown formatting in CLI
- Add focus indicator on action buttons in extension

### Fixed

- Clear all OCA secrets on auth refresh failure to prevent re-auth loops
- Resolve "Could not find the file context" error in Explain Changes
- Use `JSON_SCHEMA` for `yaml.load` to prevent unsafe deserialization
- Fetch model info from API in CLI headless auth for Cline and Vercel providers
- Generate commit message from staged changes only when staging exists
- Update stale `maxTokens` values for Claude 3.7+ models across Anthropic, Bedrock, Vertex, and SAP AI Core
- Use `model.info.maxTokens` for OpenRouter instead of hardcoded `8192`

### Changed

- Increase timeout for a flaky test to reduce short-term test instability

**Full Changelog**: https://github.com/cline/cline/compare/v2.5.0-cli...v3.68.0


## [3.67.1] - 2026-02-24

### Added

- Added Cline SDK API interface for programmatic access to Cline features and tools, enabling integration into custom applications.
- Added Codex 5.3 model support

### Fixed

- Fix OpenAI Codex by setting `store` to `false`
- Use `isLocatedInPath()` instead of string matching for path containment checks

**Full Changelog**: https://github.com/cline/cline/compare/v2.4.3-cli...v3.67.1


## [3.67.0] - 2026-02-24

### Added

- Add support for skills and optional modelId in subagent configuration
- Add AgentConfigLoader for file-based agent configs
- Add Responses API support for OpenAI native provider
- Preconnect websocket to reduce response latency
- Fetch featured models from backend with local fallback
- Add /q command to quit CLI
- Add MCP enterprise configuration details
- Pull Cline's recommended models from internal endpoint
- Add dynamic flag to adjust banner cache duration

### Fixed

- Fix reasoning delta crash on usage-only stream chunks
- Fix OpenAI tool ID transformation restricted to native provider only
- Fix auth check for ACP mode
- Fix CLI yolo mode to not persist yolo setting to disk
- Fix inline focus-chain slider within its feature row
- Fix Gemini 3.1 Pro compatibility
- Fix Cline auth with ACP flag

### Changed

- Move PR skill to .agents/skills
- SambaNova provider: update models list
- Remove changeset-converter GitHub Action and npm run changeset

**Full Changelog**: https://github.com/cline/cline/compare/v2.4.2-cli...v3.67.0


## [3.66.0] - 2026-02-19

### Added

- Gemini-3.1 Pro Preview

**Full Changelog**: https://github.com/cline/cline/compare/v2.4.1-cli...v3.66.0


## [3.65.0] - 2026-02-18

### Added

- Add /skills slash command to CLI for viewing and managing installed skills

### Fixed

- Fix aggressive context compaction caused by accidental clicks on the context window progress bar silently setting a very low auto-condense threshold
- Fix infinite retry loop when write_to_file fails with missing content parameter.
- Fixed default claude model

**Full Changelog**: https://github.com/cline/cline/compare/v2.4.0-cli...v3.65.0


## [3.64.0] - 2026-02-17

### Added

- added zai GLM 5 Free promo

### Fixed

- Restore reasoning trace visibility in chat and improve the thinking row UX so reasoning is visible, then collapsible after completion.

**Full Changelog**: https://github.com/cline/cline/compare/v2.2.3-cli...v3.64.0


## [3.63.0] - 2026-02-16

### Added

- added zai GLM 5 Free promo

### Fixed

- Restore reasoning trace visibility in chat and improve the thinking row UX so reasoning is visible, then collapsible after completion.

**Full Changelog**: https://github.com/cline/cline/compare/v3.62.0...v3.63.0


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

