# RooCode Changelog


## [3.47.3] - 2026-02-06

- Remove "Enable URL context" and "Enable Grounding with Google search" checkboxes that are no longer needed (PR #11253 by @roomote)
- Revert refactor that appended environment details into existing blocks, restoring original behavior (PR #11256 by @mrubens)
- Revert removal of stripAppendedEnvironmentDetails and helpers, restoring necessary utility functions (PR #11255 by @mrubens)


## [3.47.1] - 2026-02-06

Release v3.47.1

## [cli-v0.0.51] - 2026-02-06

## What's New


### Changed

- **Default Model Update**: Changed the default model from Opus 4.5 to Opus 4.6 for improved performance and capabilities

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.0.51 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4) or Linux x64

## Usage

```bash
# Run a task
roo "What is this project?"

# See all options
roo --help
```

## Platform Support

This release includes binaries for:
- `roo-cli-darwin-arm64.tar.gz` - macOS Apple Silicon (M1/M2/M3)
- `roo-cli-linux-x64.tar.gz` - Linux x64

## Checksums

```
956cc7cfc6a95f27cafa61f64ed82f7b09c7a35daa4ef83e44024342267fe79a  roo-cli-darwin-arm64.tar.gz
ebdcac5ac73cff0a1eec47d552041401e390f11e9497fb9e15523ea0a7b81aff  roo-cli-linux-x64.tar.gz
```


## [3.47.2] - 2026-02-05

- Add support for .agents/skills directory (PR #11181 by @roomote)
- Fix: Restore Gemini thought signature round-tripping after AI SDK migration (PR #11237 by @hannesrudolph)
- Fix: Capture and round-trip thinking signature for Bedrock Claude (PR #11238 by @hannesrudolph)


## [3.47.0] - 2026-02-05

![3.47.0 Release - Claude Opus 4.6 & GPT-5.3-Codex](/releases/3.47.0-release.png)

- Add Claude Opus 4.6 support across all providers (#11223 by @hannesrudolph, PR #11224 by @hannesrudolph and @PeterDaveHello)
- Add GPT-5.3-Codex model to OpenAI - ChatGPT provider (PR #11225 by @roomote)
- Migrate Gemini and Vertex providers to AI SDK for improved reliability and consistency (PR #11180 by @daniel-lxs)
- Improve Skills and Slash Commands settings UI with multi-mode support (PR #11157 by @brunobergher)
- Add support for AGENTS.local.md personal override files (PR #11183 by @roomote)
- Add Kimi K2.5 model to Fireworks provider (PR #11177 by @daniel-lxs)
- Improve CLI dev experience and Roo provider API key support (PR #11203 by @cte)
- Fix: Preserve reasoning parts in AI SDK message conversion (#11199 by @hannesrudolph, PR #11217 by @hannesrudolph)
- Refactor: Append environment details into existing blocks for cleaner context (#11200 by @hannesrudolph, PR #11198 by @hannesrudolph)
- Fix: Resolve race condition causing provider switch during CLI mode changes (PR #11205 by @cte)
- Roo Code CLI v0.0.50 (PR #11204 by @cte)
- Chore: Remove dead toolFormat code from getEnvironmentDetails (#11206 by @hannesrudolph, PR #11207 by @roomote)
- Refactor: Simplify docs-extractor mode to focus on raw fact extraction (PR #11129 by @hannesrudolph)
- Revert then re-land AI SDK reasoning fix (PR #11216 by @mrubens, PR #11196 by @hannesrudolph)

## [cli-v0.0.50] - 2026-02-05

## What's New


### Added

- **Linux Support**: The CLI now supports Linux platforms in addition to macOS
- **Roo Provider API Key Support**: Allow `--api-key` flag and `ROO_API_KEY` environment variable for the roo provider instead of requiring cloud auth token
- **Exit on Error**: New `--exit-on-error` flag to exit immediately on API request errors instead of retrying, useful for CI/CD pipelines

### Changed

- **Improved Dev Experience**: Dev scripts now use `tsx` for running directly from source without building first
- **Path Resolution Fixes**: Fixed path resolution in [`version.ts`](src/lib/utils/version.ts), [`extension.ts`](src/lib/utils/extension.ts), and [`extension-host.ts`](src/agent/extension-host.ts) to work from both source and bundled locations
- **Debug Logging**: Debug log file (`~/.roo/cli-debug.log`) is now disabled by default unless `--debug` flag is passed
- Updated README with complete environment variable table and dev workflow documentation

### Fixed

- Corrected example in install script

### Removed

- Dropped macOS 13 support

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.0.50 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4) or Linux x64

## Usage

```bash
# Run a task
roo "What is this project?"

# See all options
roo --help
```

## Platform Support

This release includes binaries for:
- `roo-cli-darwin-arm64.tar.gz` - macOS Apple Silicon (M1/M2/M3)
- `roo-cli-linux-x64.tar.gz` - Linux x64

## Checksums

```
40e8a7c48e4dda9292b18e717c712a593b0846bf621320334b0acec0d2baa03e  roo-cli-darwin-arm64.tar.gz
223debf015deeed44276427e8e43b03900ec295f4c2a8a3532c632d3cfa1d402  roo-cli-linux-x64.tar.gz
```


## [3.46.2] - 2026-02-03

- Fix: Queue messages during command execution instead of losing them (PR #11140 by @mrubens)
- Fix: Transform tool blocks to text before condensing to prevent context corruption (PR #10975 by @daniel-lxs)
- Fix: Add image content support to MCP tool responses (PR #10874 by @roomote)
- Fix: Remove deprecated text-embedding-004 and migrate code index to gemini-embedding-001 (PR #11038 by @roomote)
- Feat: Use custom Base URL for OpenRouter model list fetch (#11150 by @sebastianlang84, PR #11154 by @roomote)
- Feat: Migrate Mistral provider to AI SDK (PR #11089 by @daniel-lxs)
- Feat: Migrate SambaNova provider to AI SDK (PR #11153 by @roomote)
- Feat: Migrate xAI provider to AI SDK (PR #11158 by @roomote)
- Chore: Remove Feature Request from issue template options (PR #11141 by @roomote)
- Fix: IPC improvements for task cancellation and queued message handling (PR #11162 by @cte)

## [cli-v0.0.49] - 2026-02-03

## What's New


### Added

- **Output Format Options**: New `--output-format` flag to control CLI output format for scripting and automation:
    - `text` (default) - Human-readable interactive output
    - `json` - Single JSON object with all events and final result at task completion
    - `stream-json` - NDJSON (newline-delimited JSON) for real-time streaming of events
    - See [`json-events.ts`](src/types/json-events.ts) for the complete event schema
    - New [`JsonEventEmitter`](src/agent/json-event-emitter.ts) for structured output generation

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.0.49 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4) or Linux x64

## Usage

```bash
# Run a task
roo "What is this project?"

# See all options
roo --help
```

## Platform Support

This release includes binaries for:
- `roo-cli-darwin-arm64.tar.gz` - macOS Apple Silicon (M1/M2/M3)
- `roo-cli-linux-x64.tar.gz` - Linux x64

## Checksums

```
19f3ad6339b2e5d1c00a11cf6552e28de9a2610bb8cfa46b9fd8ce8cb65f8a3e  roo-cli-darwin-arm64.tar.gz
9d1e75b9281180e1ff8d399a9b245228e5592afecd057e3b4687fafc7ac14eeb  roo-cli-linux-x64.tar.gz
```


## [3.46.1] - 2026-01-30

- Fix: Sanitize tool_use_id in tool_result blocks to match API history, preventing message format errors (PR #11131 by @daniel-lxs)
- Add: Mode dropdown to change skill mode dynamically, allowing more flexible skill configuration (PR #11102 by @SannidhyaSah)
- Add: Import settings option in the initial welcome screen for easier onboarding (#10992 by @emeraldcheshire, PR #10994 by @roomote)
- Chore: Treat extension .env as optional to simplify development setup (PR #11116 by @hannesrudolph)


## [3.46.0] - 2026-01-27

![3.46.0 Release - Parallel Processing Power](/releases/3.46.0-release.png)

- Parallel tool calls enabled by default for improved performance (PR #11031 by @daniel-lxs)
- Codex-inspired read_file refactor introduces indentation mode for extracting complete semantic code blocks without mid-function truncation, ideal when targeting specific lines from search results or errors (#10239 by @pwilkin, PR #10981 by @hannesrudolph)
- Lossless terminal output with new read_command_output tool allows retrieving full command output from truncated executions with pagination and regex filtering (#10941 by @hannesrudolph, PR #10944 by @hannesrudolph)
- New skill system replaces fetch_instructions with a dedicated skill tool and built-in skills for create-mcp-server and create-mode, with configurable skill locations and mandatory skill checks (#11062 by @hannesrudolph, PR #11084 by @hannesrudolph)
- Skills management UI added to settings panel for managing workspace and global skills (#10513 by @SannidhyaSah, PR #10844 by @SannidhyaSah)
- AI SDK provider migrations: Moonshot (PR #11063 by @daniel-lxs), DeepSeek (PR #11079 by @daniel-lxs), Cerebras (PR #11086 by @daniel-lxs), Groq (PR #11088 by @daniel-lxs), and Fireworks (PR #11118 by @daniel-lxs) now use the AI SDK for better streaming and tool support
- Add OpenAI-compatible base provider infrastructure for AI SDK migrations (PR #11063 by @daniel-lxs)
- Add AI SDK dependencies and message conversion utilities (PR #11047 by @daniel-lxs)
- React Compiler integration added to webview-ui for automatic memoization and performance improvements (#9916 by @In-line, PR #9565 by @In-line)
- Fix: Include reserved output tokens in task header percentage calculation (PR #11034 by @app/roomote)
- Fix: Calculate header percentage based on available input space (PR #11054 by @app/roomote)
- Fix: Prevent time-travel bug in parallel tool calling (PR #11046 by @daniel-lxs)
- Docs: Clarify read_command_output search param should be omitted when not filtering (PR #11056 by @hannesrudolph)
- Add pnpm serve command for code-server development (PR #10964 by @mrubens)
- Update Next.js to latest version (PR #11108 by @cte)
- Replace bespoke navigation menu with shadcn navigation menu on website (PR #11117 by @app/roomote)
- Add Linear integration marketing page to website (PR #11028 by @app/roomote)


## [3.45.0] - 2026-01-27

![3.45.0 Release - Smart Code Folding](/releases/3.45.0-release.png)

- Smart Code Folding: Context condensation now intelligently preserves a lightweight map of files you worked on—function signatures, class declarations, and type definitions—so Roo can continue referencing them accurately after condensing. Files are prioritized by most recent access, with a ~50k character budget ensuring your latest work is always preserved. (Idea by @shariqriazz, PR #10942 by @hannesrudolph)


## [3.44.2] - 2026-01-27

- Re-enable parallel tool calling with new_task isolation safeguards (PR #11006 by @mrubens)
- Fix worktree indexing by using relative paths in isPathInIgnoredDirectory (PR #11009 by @daniel-lxs)
- Fix local model validation error for Ollama models (PR #10893 by @roomote)
- Fix duplicate tool_call emission from Responses API providers (PR #11008 by @daniel-lxs)


## [3.44.1] - 2026-01-27

- Fix LiteLLM tool ID validation errors for Bedrock proxy (PR #10990 by @daniel-lxs)
- Add temperature=0.9 and top_p=0.95 to zai-glm-4.7 model for better generation quality (PR #10945 by @sebastiand-cerebras)
- Add quality checks to marketing site deployment workflows (PR #10959 by @mp-roocode)


## [3.44.0] - 2026-01-26

![3.44.0 Release - Worktrees](/releases/3.44.0-release.png)

- Add worktree selector and creation UX (PR #10940 by @brunobergher, thanks Cline!)
- Improve subtask visibility and navigation in history and chat views (PR #10864 by @brunobergher)
- Add wildcard support for MCP alwaysAllow configuration (PR #10948 by @app/roomote)
- Fix: Prevent nested condensing from including previously-condensed content (PR #10985 by @hannesrudolph)
- Fix: VS Code LM token counting returns 0 outside requests, breaking context condensing (#10968 by @srulyt, PR #10983 by @daniel-lxs)
- Fix: Record truncation event when condensation fails but truncation succeeds (PR #10984 by @hannesrudolph)
- Replace hyphen encoding with fuzzy matching for MCP tool names (PR #10775 by @daniel-lxs)
- Remove MCP SERVERS section from system prompt for cleaner prompts (PR #10895 by @daniel-lxs)
- new_task tool creates checkpoint the same way write_to_file does (PR #10982 by @daniel-lxs)
- Update Fireworks provider with new models (#10674 by @hannesrudolph, PR #10679 by @ThanhNguyxn)
- Fix: Truncate AWS Bedrock toolUseId to 64 characters (PR #10902 by @daniel-lxs)
- Fix: Restore opaque background to settings section headers (PR #10951 by @app/roomote)
- Fix: Remove unsupported Fireworks model tool fields (PR #10937 by @app/roomote)
- Update and improve zh-TW Traditional Chinese locale and docs (PR #10953 by @PeterDaveHello)
- Chore: Remove POWER_STEERING experiment remnants (PR #10980 by @hannesrudolph)


## [3.43.0] - 2026-01-23

![3.43.0 Release - Intelligent Context Condensation](/releases/3.43.0-release.png)

- Intelligent Context Condensation v2: New context condensation system that intelligently summarizes conversation history when approaching context limits, preserving important information while reducing token usage (PR #10873 by @hannesrudolph)
- Improved context condensation with environment details, accurate token counts, and lazy evaluation for better performance (PR #10920 by @hannesrudolph)
- Move condense prompt editor to Context Management tab for better discoverability and organization (PR #10909 by @hannesrudolph)
- Update Z.AI models with new variants and pricing (#10859 by @ErdemGKSL, PR #10860 by @ErdemGKSL)
- Add pnpm install:vsix:nightly command for easier nightly build installation (PR #10912 by @hannesrudolph)
- Fix: Convert orphaned tool_results to text blocks after condensing to prevent API errors (PR #10927 by @daniel-lxs)
- Fix: Auto-migrate v1 condensing prompt and handle invalid providers on import (PR #10931 by @hannesrudolph)
- Fix: Use json-stream-stringify for pretty-printing MCP config files to prevent memory issues with large configs (#9862 by @Michaelzag, PR #9864 by @Michaelzag)
- Fix: Correct Gemini 3 pricing for Flash and Pro models (#10432 by @rossdonald, PR #10487 by @roomote)
- Fix: Skip thoughtSignature blocks during markdown export for cleaner output (#10199 by @rossdonald, PR #10932 by @rossdonald)
- Fix: Duplicate model display for OpenAI Codex provider (PR #10930 by @roomote)
- Remove diffEnabled and fuzzyMatchThreshold settings as they are no longer needed (#10648 by @hannesrudolph, PR #10298 by @hannesrudolph)
- Remove MULTI_FILE_APPLY_DIFF experiment (PR #10925 by @hannesrudolph)
- Remove POWER_STEERING experimental feature (PR #10926 by @hannesrudolph)
- Remove legacy XML tool calling code (getToolDescription) for cleaner codebase (PR #10929 by @hannesrudolph)


## [3.42.0] - 2026-01-22

![3.42.0 Release - ChatGPT Usage Tracking](/releases/3.42.0-release.png)

- Added UI to track your ChatGPT usage limits in the OpenAI Codex provider (PR #10813 by @hannesrudolph)
- Removed deprecated Claude Code provider (PR #10883 by @daniel-lxs)
- Streamlined codebase by removing legacy XML tool calling functionality (#10848 by @hannesrudolph, PR #10841 by @hannesrudolph)
- Standardize model selectors across all providers: Improved consistency of model selection UI (#10650 by @hannesrudolph, PR #10294 by @hannesrudolph)
- Enable prompt caching for Cerebras zai-glm-4.7 model (#10601 by @jahanson, PR #10670 by @app/roomote)
- Add Kimi K2 thinking model to VertexAI provider (#9268 by @diwakar-s-maurya, PR #9269 by @app/roomote)
- Warn users when too many MCP tools are enabled (PR #10772 by @app/roomote)
- Migrate context condensing prompt to customSupportPrompts (PR #10881 by @hannesrudolph)
- Unify export path logic and default to Downloads folder (PR #10882 by @hannesrudolph)
- Performance improvements for webview state synchronization (PR #10842 by @hannesrudolph)
- Fix: Handle mode selector empty state on workspace switch (#10660 by @hannesrudolph, PR #9674 by @app/roomote)
- Fix: Resolve race condition in context condensing prompt input (PR #10876 by @hannesrudolph)
- Fix: Prevent double emission of text/reasoning in OpenAI native and codex handlers (PR #10888 by @hannesrudolph)
- Fix: Prevent task abortion when resuming via IPC/bridge (PR #10892 by @cte)
- Fix: Enforce file restrictions for all editing tools (PR #10896 by @app/roomote)
- Fix: Remove custom condensing model option (PR #10901 by @hannesrudolph)
- Unify user content tags to <user_message> for consistent prompt formatting (#10658 by @hannesrudolph, PR #10723 by @app/roomote)
- Clarify linked SKILL.md file handling in prompts (PR #10907 by @hannesrudolph)
- Fix: Padding on Roo Code Cloud teaser (PR #10889 by @app/roomote)


## [3.41.3] - 2026-01-18

- Fix: Thinking block word-breaking to prevent horizontal scroll in the chat UI (PR #10806 by @roomote)
- Add Claude-like CLI flags and authentication fixes for the Roo Code CLI (PR #10797 by @cte)
- Improve CLI authentication by using a redirect instead of a fetch (PR #10799 by @cte)
- Fix: Roo Code Router fixes for the CLI (PR #10789 by @cte)
- Release CLI v0.0.48 with latest improvements (PR #10800 by @cte)
- Release CLI v0.0.47 (PR #10798 by @cte)
- Revert E2E tests enablement to address stability issues (PR #10794 by @cte)

## [cli-v0.0.48] - 2026-01-17

## What's New


### Changed

- Simplified authentication callback flow by using HTTP redirects instead of POST requests with CORS headers for improved browser compatibility

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.0.48 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS (Intel or Apple Silicon) or Linux (x64 or ARM64)

## Usage

```bash
# Run a task
roo "What is this project?"

# See all options
roo --help
```

## Platform Support

This release includes:
- `roo-cli-darwin-arm64.tar.gz` - Built on Darwin arm64

> **Note:** Additional platforms will be added as needed. If you need a different platform, please open an issue.

## Checksum

```
c756adba40328b5bcd5f084b2356ae4aab107b4caef74e49961864bd415138be  roo-cli-darwin-arm64.tar.gz
```

## [cli-v0.0.47] - 2026-01-17

## What's New


### Added

- **Workspace flag**: New `-w, --workspace <path>` option to specify a custom workspace directory instead of using the current working directory
- **Oneshot mode**: New `--oneshot` flag to exit upon task completion, useful for scripting and automation (can also be saved in settings via [`CliSettings.oneshot`](src/types/types.ts))

### Changed

- Skip onboarding flow when a provider is explicitly specified via `--provider` flag or saved in settings
- Unified permission flags: Combined `-y`, `--yes`, and `--dangerously-skip-permissions` into a single option for Claude Code-like CLI compatibility
- Improved Roo Code Router authentication flow and error messaging

### Fixed

- Removed unnecessary timeout that could cause issues with long-running tasks
- Fixed authentication token validation for Roo Code Router provider

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.0.47 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS (Intel or Apple Silicon) or Linux (x64 or ARM64)

## Usage

```bash
# Run a task
roo "What is this project?"

# See all options
roo --help
```

## Platform Support

This release includes:
- `roo-cli-darwin-arm64.tar.gz` - Built on Darwin arm64

> **Note:** Additional platforms will be added as needed. If you need a different platform, please open an issue.

## Checksum

```
32008b2ddb6b28dc59f1176eb2f4c845b7d8be99960f2d016e7fa6a3e53375b6  roo-cli-darwin-arm64.tar.gz
```


## [3.41.2] - 2026-01-16

- Add button to open markdown in VSCode preview for easier reading of formatted content (PR #10773 by @brunobergher)
- Fix: Reset invalid model selection when using OpenAI Codex provider (PR #10777 by @hannesrudolph)
- Fix: Add openai-codex to providers that don't require an API key (PR #10786 by @roomote)
- Fix: Detect Gemini models with space-separated names for proper thought signature injection in LiteLLM (PR #10787 by @daniel-lxs)


## [3.41.1] - 2026-01-16

![3.41.1 Release - Aggregated Subtask Costs](/releases/3.41.1-release.png)

- Feat: Aggregate subtask costs in parent task (#5376 by @hannesrudolph, PR #10757 by @taltas)
- Fix: Prevent duplicate tool_use IDs causing API 400 errors (PR #10760 by @daniel-lxs)
- Fix: Handle missing tool identity in OpenAI Native streams (PR #10719 by @hannesrudolph)
- Fix: Truncate call_id to 64 chars for OpenAI Responses API (PR #10763 by @daniel-lxs)
- Fix: Gemini thought signature validation errors (PR #10694 by @daniel-lxs)
- Fix: Filter out empty text blocks from user messages for Gemini compatibility (PR #10728 by @daniel-lxs)
- Fix: Flatten top-level anyOf/oneOf/allOf in MCP tool schemas (PR #10726 by @daniel-lxs)
- Fix: Filter Ollama models without native tool support (PR #10735 by @daniel-lxs)
- Feat: Add settings tab titles to search index (PR #10761 by @roomote)
- Feat: Clarify Slack and Linear are Cloud Team only features (PR #10748 by @roomote)

