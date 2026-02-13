# Claude Changelog

最后更新: 2026-02-13 09:53:21


## [2.1.39] - 2026-02-10

## What's changed

- Improved terminal rendering performance
- Fixed fatal errors being swallowed instead of displayed
- Fixed process hanging after session close
- Fixed character loss at terminal screen boundary
- Fixed blank lines in verbose transcript view


## [2.1.38] - 2026-02-10

## What's changed

- Fixed VS Code terminal scroll-to-top regression introduced in 2.1.37
- Fixed Tab key queueing slash commands instead of autocompleting
- Fixed bash permission matching for commands using environment variable wrappers
- Fixed text between tool uses disappearing when not using streaming
- Fixed duplicate sessions when resuming in VS Code extension
- Improved heredoc delimiter parsing to prevent command smuggling
- Blocked writes to `.claude/skills` directory in sandbox mode


## [2.1.37] - 2026-02-07

## What's changed

- Fixed an issue where /fast was not immediately available after enabling /extra-usage


## [2.1.36] - 2026-02-07

## What's changed

- Fast mode is now available for Opus 4.6. Learn more at https://code.claude.com/docs/en/fast-mode


## [2.1.34] - 2026-02-06

## What's changed

- Fixed a crash when agent teams setting changed between renders
- Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled


## [2.1.33] - 2026-02-06

## What's changed

- Fixed agent teammate sessions in tmux to send and receive messages
- Fixed warnings about agent teams not being available on your current plan
- Added `TeammateIdle` and `TaskCompleted` hook events for multi-agent workflows
- Added support for restricting which sub-agents can be spawned via `Task(agent_type)` syntax in agent "tools" frontmatter
- Added `memory` frontmatter field support for agents, enabling persistent memory with `user`, `project`, or `local` scope
- Added plugin name to skill descriptions and `/skills` menu for better discoverability
- Fixed an issue where submitting a new message while the model was in extended thinking would interrupt the thinking phase
- Fixed an API error that could occur when aborting mid-stream, where whitespace text combined with a thinking block would bypass normalization and produce an invalid request
- Fixed API proxy compatibility issue where 404 errors on streaming endpoints no longer triggered non-streaming fallback
- Fixed an issue where proxy settings configured via `settings.json` environment variables were not applied to WebFetch and other HTTP requests on the Node.js build
- Fixed `/resume` session picker showing raw XML markup instead of clean titles for sessions started with slash commands
- Improved error messages for API connection failures — now shows specific cause (e.g., ECONNREFUSED, SSL errors) instead of generic "Connection error"
- Errors from invalid managed settings are now surfaced
- VSCode: Added support for remote sessions, allowing OAuth users to browse and resume sessions from claude.ai
- VSCode: Added git branch and message count to the session picker, with support for searching by branch name
- VSCode: Fixed scroll-to-bottom under-scrolling on initial session load and session switch


## [2.1.32] - 2026-02-05

## What's changed

- Claude Opus 4.6 is now available!
- Added research preview agent teams feature for multi-agent collaboration (token-intensive feature, requires setting CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)
- Claude now automatically records and recalls memories as it works
- Added "Summarize from here" to the message selector, allowing partial conversation summarization.
- Skills defined in `.claude/skills/` within additional directories (`--add-dir`) are now loaded automatically.
- Fixed `@` file completion showing incorrect relative paths when running from a subdirectory
- Updated --resume to re-use --agent value specified in previous conversation by default.
- Fixed: Bash tool no longer throws "Bad substitution" errors when heredocs contain JavaScript template literals like `${index + 1}`, which previously interrupted tool execution
- Skill character budget now scales with context window (2% of context), so users with larger context windows can see more skill descriptions without truncation
- Fixed Thai/Lao spacing vowels (สระ า, ำ) not rendering correctly in the input field
- VSCode: Fixed slash commands incorrectly being executed when pressing Enter with preceding text in the input field
- VSCode: Added spinner when loading past conversations list


## [2.1.31] - 2026-02-04

## What's changed

- Added session resume hint on exit, showing how to continue your conversation later
- Added support for full-width (zenkaku) space input from Japanese IME in checkbox selection
- Fixed PDF too large errors permanently locking up sessions, requiring users to start a new conversation
- Fixed bash commands incorrectly reporting failure with "Read-only file system" errors when sandbox mode was enabled
- Fixed a crash that made sessions unusable after entering plan mode when project config in `~/.claude.json` was missing default fields
- Fixed `temperatureOverride` being silently ignored in the streaming API path, causing all streaming requests to use the default temperature (1) regardless of the configured override
- Fixed LSP shutdown/exit compatibility with strict language servers that reject null params
- Improved system prompts to more clearly guide the model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents (`cat`, `sed`, `grep`, `find`), reducing unnecessary bash command usage
- Improved PDF and request size error messages to show actual limits (100 pages, 20MB)
- Reduced layout jitter in the terminal when the spinner appears and disappears during streaming
- Removed misleading Anthropic API pricing from model selector for third-party provider (Bedrock, Vertex, Foundry) users


## [2.1.30] - 2026-02-03

## What's changed

- Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return a lightweight reference when `@` mentioned instead of being inlined into context.
- Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.
- Added `/debug` for Claude to help troubleshoot the current session
- Added support for additional `git log` and `git show` flags in read-only mode (e.g., `--topo-order`, `--cherry-pick`, `--format`, `--raw`)
- Added token count, tool uses, and duration metrics to Task tool results
- Added reduced motion mode to the config
- Fixed phantom "(no content)" text blocks appearing in API conversation history, reducing token waste and potential model confusion
- Fixed prompt cache not correctly invalidating when tool descriptions or input schemas changed, only when tool names changed
- Fixed 400 errors that could occur after running `/login` when the conversation contained thinking blocks
- Fixed a hang when resuming sessions with corrupted transcript files containing `parentUuid` cycles
- Fixed rate limit message showing incorrect "/upgrade" suggestion for Max 20x users when extra-usage is unavailable
- Fixed permission dialogs stealing focus while actively typing
- Fixed subagents not being able to access SDK-provided MCP tools because they were not synced to the shared application state
- Fixed a regression where Windows users with a `.bashrc` file could not run bash commands
- Improved memory usage for `--resume` (68% reduction for users with many sessions) by replacing the session index with lightweight stat-based loading and progressive enrichment
- Improved `TaskStop` tool to display the stopped command/task description in the result line instead of a generic "Task stopped" message
- Changed `/model` to execute immediately instead of being queued
- [VSCode] Added multiline input support to the "Other" text input in question dialogs (use Shift+Enter for new lines)
- [VSCode] Fixed duplicate sessions appearing in the session list when starting a new conversation


## [2.1.29] - 2026-01-31

## What's changed

- Fixed startup performance issues when resuming sessions that have `saved_hook_context`


## [2.1.27] - 2026-01-30

## What's changed

- Added tool call failures and denials to debug logs
- Fixed context management validation error for gateway users, ensuring `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` avoids the error
- Added `--from-pr` flag to resume sessions linked to a specific GitHub PR number or URL
- Sessions are now automatically linked to PRs when created via `gh pr create`
- Fixed /context command not displaying colored output
- Fixed status bar duplicating background task indicator when PR status was shown
- VSCode: Enabled Claude in Chrome integration
- Permissions now respect content-level `ask` over tool-level `allow`. Previously `allow: ["Bash"], ask: ["Bash(rm *)"]` allowed all bash commands, but will now permission prompt for `rm`.
- Windows: Fixed bash command execution failing for users with `.bashrc` files
- Windows: Fixed console windows flashing when spawning child processes
- VSCode: Fixed OAuth token expiration causing 401 errors after extended sessions


## [2.1.25] - 2026-01-29

## What's changed

- Fixed beta header validation error for gateway users on Bedrock and Vertex, ensuring `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` avoids the error


## [2.1.23] - 2026-01-29

## What's changed

- Added customizable spinner verbs setting (`spinnerVerbs`)
- Fixed mTLS and proxy connectivity for users behind corporate proxies or using client certificates
- Fixed per-user temp directory isolation to prevent permission conflicts on shared systems
- Fixed a race condition that could cause 400 errors when prompt caching scope was enabled
- Fixed pending async hooks not being cancelled when headless streaming sessions ended
- Fixed tab completion not updating the input field when accepting a suggestion
- Fixed ripgrep search timeouts silently returning empty results instead of reporting errors
- Improved terminal rendering performance with optimized screen data layout
- Changed Bash commands to show timeout duration alongside elapsed time
- Changed merged pull requests to show a purple status indicator in the prompt footer
- [IDE] Fixed model options displaying incorrect region strings for Bedrock users in headless mode


## [2.1.22] - 2026-01-28

## What's changed

- Fixed structured outputs for non-interactive (-p) mode


## [2.1.21] - 2026-01-28

## What's changed

- Added support for full-width (zenkaku) number input from Japanese IME in option selection prompts
- Fixed shell completion cache files being truncated on exit
- Fixed API errors when resuming sessions that were interrupted during tool execution
- Fixed auto-compact triggering too early on models with large output token limits
- Fixed task IDs potentially being reused after deletion
- Fixed file search not working in VS Code extension on Windows
- Improved read/search progress indicators to show "Reading…" while in progress and "Read" when complete
- Improved Claude to prefer file operation tools (Read, Edit, Write) over bash equivalents (cat, sed, awk)
- [VSCode] Added automatic Python virtual environment activation, ensuring `python` and `pip` commands use the correct interpreter (configurable via `claudeCode.usePythonEnvironment` setting)
- [VSCode] Fixed message action buttons having incorrect background colors


## [2.1.20] - 2026-01-27

## What's changed

- Added arrow key history navigation in vim normal mode when cursor cannot move further
- Added external editor shortcut (Ctrl+G) to the help menu for better discoverability
- Added PR review status indicator to the prompt footer, showing the current branch's PR state (approved, changes requested, pending, or draft) as a colored dot with a clickable link
- Added support for loading `CLAUDE.md` files from additional directories specified via `--add-dir` flag (requires setting `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`)
- Added ability to delete tasks via the `TaskUpdate` tool
- Fixed session compaction issues that could cause resume to load full history instead of the compact summary
- Fixed agents sometimes ignoring user messages sent while actively working on a task
- Fixed wide character (emoji, CJK) rendering artifacts where trailing columns were not cleared when replaced by narrower characters
- Fixed JSON parsing errors when MCP tool responses contain special Unicode characters
- Fixed up/down arrow keys in multi-line and wrapped text input to prioritize cursor movement over history navigation
- Fixed draft prompt being lost when pressing UP arrow to navigate command history
- Fixed ghost text flickering when typing slash commands mid-input
- Fixed marketplace source removal not properly deleting settings
- Fixed duplicate output in some commands like `/context`
- Fixed task list sometimes showing outside the main conversation view
- Fixed syntax highlighting for diffs occurring within multiline constructs like Python docstrings
- Fixed crashes when cancelling tool use
- Improved `/sandbox` command UI to show dependency status with installation instructions when dependencies are missing
- Improved thinking status text with a subtle shimmer animation
- Improved task list to dynamically adjust visible items based on terminal height
- Improved fork conversation hint to show how to resume the original session
- Changed collapsed read/search groups to show present tense ("Reading", "Searching for") while in progress, and past tense ("Read", "Searched for") when complete
- Changed teammate messages to render with rich Markdown formatting (bold, code blocks, lists, etc.) instead of plain text
- Changed `ToolSearch` results to appear as a brief notification instead of inline in the conversation
- Changed the `/commit-push-pr` skill to automatically post PR URLs to Slack channels when configured via MCP tools
- Changed the `/copy` command to be available to all users
- Changed background agents to prompt for tool permissions before launching
- Changed permission rules like `Bash(*)` to be accepted and treated as equivalent to `Bash`
- Changed config backups to be timestamped and rotated (keeping 5 most recent) to prevent data loss


## [2.1.19] - 2026-01-23

## What's changed

- Added env var `CLAUDE_CODE_ENABLE_TASKS`, set to `false` to keep the old system temporarily
- Added shorthand `$0`, `$1`, etc. for accessing individual arguments in custom commands
- Fixed crashes on processors without AVX instruction support
- Fixed dangling Claude Code processes when terminal is closed by catching EIO errors from `process.exit()` and using SIGKILL as fallback
- Fixed `/rename` and `/tag` not updating the correct session when resuming from a different directory (e.g., git worktrees)
- Fixed resuming sessions by custom title not working when run from a different directory
- Fixed pasted text content being lost when using prompt stash (Ctrl+S) and restore
- Fixed agent list displaying "Sonnet (default)" instead of "Inherit (default)" for agents without an explicit model setting
- Fixed backgrounded hook commands not returning early, potentially causing the session to wait on a process that was intentionally backgrounded
- Fixed file write preview omitting empty lines
- Changed skills without additional permissions or hooks to be allowed without requiring approval
- Changed indexed argument syntax from `$ARGUMENTS.0` to `$ARGUMENTS[0]` (bracket syntax)
- [SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageReplay` events when `replayUserMessages` is enabled
- [VSCode] Enabled session forking and rewind functionality for all users


## [2.1.17] - 2026-01-22

## What's changed

- Fixed crashes on processors without AVX instruction support


## [2.1.16] - 2026-01-22

## What's changed

- Added new task management system, including new capabilities like dependency tracking
- [VSCode] Added native plugin management support
- [VSCode] Added ability for OAuth users to browse and resume remote Claude sessions from the Sessions dialog
- Fixed out-of-memory crashes when resuming sessions with heavy subagent usage
- Fixed an issue where the "context remaining" warning was not hidden after running `/compact`
- Fixed session titles on the resume screen not respecting the user's language setting
- [IDE] Fixed a race condition on Windows where the Claude Code sidebar view container would not appear on start


## [2.1.15] - 2026-01-21

## What's changed

- Added deprecation notification for npm installations - run `claude install` or see https://docs.anthropic.com/en/docs/claude-code/getting-started for more options
- Improved UI rendering performance with React Compiler
- Fixed the "Context left until auto-compact" warning not disappearing after running `/compact`
- Fixed MCP stdio server timeout not killing child process, which could cause UI freezes


## [2.1.14] - 2026-01-20

## What's changed

- Added history-based autocomplete in bash mode (`!`) - type a partial command and press Tab to complete from your bash command history
- Added search to installed plugins list - type to filter by name or description
- Added support for pinning plugins to specific git commit SHAs, allowing marketplace entries to install exact versions
- Fixed a regression where the context window blocking limit was calculated too aggressively, blocking users at ~65% context usage instead of the intended ~98%
- Fixed memory issues that could cause crashes when running parallel subagents
- Fixed memory leak in long-running sessions where stream resources were not cleaned up after shell commands completed
- Fixed `@` symbol incorrectly triggering file autocomplete suggestions in bash mode
- Fixed `@`-mention menu folder click behavior to navigate into directories instead of selecting them
- Fixed `/feedback` command generating invalid GitHub issue URLs when description is very long
- Fixed `/context` command to show the same token count and percentage as the status line in verbose mode
- Fixed an issue where `/config`, `/context`, `/model`, and `/todos` command overlays could close unexpectedly
- Fixed slash command autocomplete selecting wrong command when typing similar commands (e.g., `/context` vs `/compact`)
- Fixed inconsistent back navigation in plugin marketplace when only one marketplace is configured
- Fixed iTerm2 progress bar not clearing properly on exit, preventing lingering indicators and bell sounds
- Improved backspace to delete pasted text as a single token instead of one character at a time
- [VSCode] Added `/usage` command to display current plan usage


## [2.1.12] - 2026-01-17

## What's changed

- Fixed message rendering bug


## [2.1.11] - 2026-01-17

## What's changed

- Fixed excessive MCP connection requests for HTTP/SSE transports


## [2.1.9] - 2026-01-16

## What's changed

- Added `auto:N` syntax for configuring the MCP tool search auto-enable threshold, where N is the context window percentage (0-100)
- Added `plansDirectory` setting to customize where plan files are stored
- Added external editor support (Ctrl+G) in AskUserQuestion "Other" input field
- Added session URL attribution to commits and PRs created from web sessions
- Added support for `PreToolUse` hooks to return `additionalContext` to the model
- Added `${CLAUDE_SESSION_ID}` string substitution for skills to access the current session ID
- Fixed long sessions with parallel tool calls failing with an API error about orphan tool_result blocks
- Fixed MCP server reconnection hanging when cached connection promise never resolves
- Fixed Ctrl+Z suspend not working in terminals using Kitty keyboard protocol (Ghostty, iTerm2, kitty, WezTerm)

