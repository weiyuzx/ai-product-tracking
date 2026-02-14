# Oh My OpenCode Changelog

最后更新: 2026-02-14 09:20:34


## [3.5.3] - 2026-02-12

## v3.5.3 — Bug Fixes & Stability

### Background Agent
- Handle `session.error` events — zombie tasks that held concurrency slots forever are now properly cleaned up with error status, concurrency release, and full timer/queue cleanup
- Error-status tasks are now skipped during queue processing, preventing attempts to start dead tasks
- Stale pending tasks are now removed from `queuesByKey` when pruned, eliminating orphan queue entries
- Extracted `session.idle` handling and shared cleanup logic into dedicated modules for maintainability

### Auth
- Multi-layer auth injection for desktop app compatibility — tries 5 strategies in order (setConfig → interceptors → fetch wrapper → mutable config → top-level fetch) instead of single `setConfig` approach that broke on some SDK versions

### CLI Run
- Session-scoped event subscription — `event.subscribe()` now passes `directory` to prevent cross-session interference
- Added 10s stabilization period after first meaningful work before checking completion, preventing premature exits

### Prometheus
- Case-insensitive agent name matching — display names like "Prometheus (Plan Builder)" and "PROMETHEUS" are now correctly detected

### Slash Commands
- Better error messages for marketplace plugin commands (`:` prefix) — directs users to `.claude/commands/`

---

## What's Changed

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.5.2...v3.5.3


## [3.5.2] - 2026-02-11

v3.5.2 is a stability patch with targeted fixes for auto-update reliability, subagent lifecycle, and MCP tool safety.

### Highlights

**Auto-Update Safety**
- Pinned plugin versions are now respected — auto-update skips when you've explicitly locked a version
- If an update install fails, the config pin reverts to prevent version mismatch between config and disk

**Subagent Lifecycle**
- Fixed zombie sessions caused by `permission.question=deny` override in subagent spawning
- Added optional chaining guard on `session_ids` to prevent crashes in boulder state reads

**MCP Tool Guard**
- Tool after-hooks now safely guard `output.output` for MCP tools that return non-standard shapes (#1720)

**Atlas Intelligence**
- Boulder verification reminders now include a notepad reading step — Atlas checks its own notes before prompting

**Category Control**
- New `disable` field in CategoryConfigSchema — turn off entire categories without removing their config

---

## What's Changed

### Features

- **categories**: add disable field to CategoryConfigSchema
- **atlas**: add notepad reading step to boulder verification reminders

### Bug Fixes

- guard output.output in tool after-hooks for MCP tools (#1720)
- respect user-pinned plugin version, skip auto-update when explicitly pinned
- **auto-update**: revert config pin on install failure to prevent version mismatch
- **subagent**: remove permission.question=deny override that caused zombie sessions
- guard session_ids with optional chaining to prevent crash
- **ci**: add web-flow to CLA allowlist

### Other Changes

- Merge pull request #1754 from code-yeongyu/fix/issue-1745-auto-update-pin
- Merge pull request #1756 from code-yeongyu/fix/mcp-tool-output-guard
- @ojh102 has signed the CLA in code-yeongyu/oh-my-opencode#1750
- Merge pull request #1683 from code-yeongyu/fix/issue-1672
- @danpung2 has signed the CLA in code-yeongyu/oh-my-opencode#1741

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.5.1...v3.5.2


## [3.5.1] - 2026-02-11

## Bug Fixes

- `13d960f3` fix(look-at): revert to sync prompt to fix race condition with async polling
  - The `look_at` tool was not waiting for the multimodal-looker agent response before returning results. This was caused by `df0b9f76` switching from synchronous `session.prompt` to async `session.promptAsync` + polling, which introduced a race condition where the poller would fire before the server registered the session as busy.

---

## What's Changed

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.5.0...v3.5.1


## [3.5.0] - 2026-02-10

# v3.5.0 — Atlas Trusts No One

Atlas was naive. A subagent said "done" — Atlas moved on. Tests failing, code half-baked, requirements missing entirely. Didn't matter. "Done" meant done.

**Not anymore.**

Atlas now enforces mandatory manual code review. You `Read` every file the subagent touched. You cross-check claims against reality. You verify imports, logic, edge cases — or you don't proceed. No rubber-stamping. No skipping Step 2.

But that wasn't the only thing Atlas got wrong.

---

## What Changed in Atlas

Boulder continuation fired on any idle session. Yours wasn't even part of the boulder — didn't matter. Atlas injected continuation prompts into random sessions. Phantom continuations everywhere.

**Now Atlas checks `session_ids` first.** Not in the list? You don't get continued. Period.

`injectBoulderContinuation` wasn't being awaited. Fire-and-forget. When it failed — and it failed — errors were swallowed silently. Your boulder stalled. You stared at a frozen session wondering what went wrong. The answer: Atlas threw the error into the void.

**Now it's awaited.** Failures are tracked. Prompt failure count increments. Two strikes, continuation stops. No more hammering broken sessions.

Plan paths pointed to the wrong place. `.sisyphus/tasks/*.yaml` — a path that doesn't exist anymore. Atlas looked where there were no plans. **Fixed to `.sisyphus/plans/*.md`.**

Sisyphus sessions were blocked from boulder continuation. Atlas-agent only. But Sisyphus runs when the boulder defaults to Atlas — same intent, different name. **Now Sisyphus gets through.**

The continuation prompt itself improved. Before: just "continue working." Now: **"Read the plan file FIRST."** Check exact progress. Count the remaining `- [ ]` tasks. No more guessing where you left off.

---

## Also Shipped

### 🔴 Background Task Interrupts
Background tasks that fail during `promptAsync` are now marked `"interrupt"` instead of generic `"error"`. Notifications show **INTERRUPTED** — you know exactly what happened without digging into logs.

### 🧭 Session Idle Dedup
OpenCode fires both `session.status {type:"idle"}` and `session.idle` for the same event. Your hooks fired twice. Now there's a 500ms dedup window — one idle, one dispatch, zero duplicates.

### 📝 Comment Checker: `apply_patch`
AI slop detection now catches `apply_patch` edits. Previously only Write/Edit tools were checked — patches slipped through. Not anymore.

### 📂 Skill @path Auto-Resolution
`@scripts/search.py` in skill templates → `/home/user/.config/opencode/skills/frontend/scripts/search.py`. No more broken relative references when skills load from unexpected directories.

### 🐚 Prometheus: Bash Access
The planner agent can now execute bash commands. Previously restricted to read-only tools — now it actually inspects the environment it's planning for.

---

## Fixes

### Delegation System (Wave 1 + 2)
The entire sync delegation pipeline was overhauled:
- **Polling**: Native finish-based completion detection. No more fragile message-count stability polling.
- **Resource cleanup**: Subagent sessions cleaned up on ALL exit paths.
- **Tool restrictions**: Sync tasks get their tools back.
- **CLI runner**: Fixed hang caused by event processor promise missing `.catch()`.
- **JSONC**: Config writes use proper `jsonc-parser` — no more corruption from comments or trailing commas.

### CLI & Config
- `run` command: timeout 2min → 10min, handles "retry" status, error check before idle gates.
- Config migration applies in-memory even if backup fails.
- Auth-plugins: crash recovery restores previous config on write failure.
- Sensitive query params redacted from skill-mcp error messages.

### Agent System
- `useTaskSystem` config flag actually wired into Sisyphus/Hephaestus now.
- EXA websearch `x-api-key` header restored (accidentally removed).
- `promptAsync` gets 120s timeout (was infinite).
- Comment checker CLI spawn gets 30s hard timeout.
- Session recovery returns `success=false` for unsupported prefill.
- Sisyphus-Junior can use TaskCreate/Update/List without delegation tool block.
- Todo continuation enforcer requires active boulder session.

---

## The Great Split

645 files. 25+ god-files decomposed. 200 LOC hard limit enforced.

| Module | Before | After |
|--------|--------|-------|
| `src/index.ts` | 1,004 lines | 88 lines + 4 orchestration files |
| `delegate-task/executor.ts` | 998 lines | 16 lines + 15 modules |
| `background-agent/manager.ts` | 1,646 lines | Core manager + 20 modules |
| `hooks/atlas/index.ts` | 700 lines | 25 lines + 15 modules |
| `hooks/todo-continuation-enforcer.ts` | 517 lines | 58 lines + 11 modules |
| `hooks/ralph-loop/index.ts` | 456 lines | 53 lines + 9 modules |
| `hooks/session-recovery/index.ts` | 451 lines | 145 lines + 12 modules |
| `hooks/claude-code-hooks/index.ts` | 422 lines | 22 lines + 6 handlers |
| `tools/lsp/client.ts` | 854 lines | 129 lines + 12 modules |
| `config/schema.ts` | 483 lines | 21 schema component files |
| `cli/install.ts` | 540 lines | 189 lines + validators/prompts |
| `cli/config-manager.ts` | 680 lines | 82 lines + 18 modules |

New architecture layer: `src/plugin/` — 21 files composing the plugin interface.

Every `utils.ts` renamed to what it actually does: `result-formatter.ts`, `session-formatter.ts`, `tmux-path-resolver.ts`, `source-detector.ts`.

Not a single public API changed.

---

## Stats

**645 files changed**
**+34,507 additions**
**-21,492 deletions**

---

## Breaking Changes

None. Internal module boundaries only. All public APIs unchanged.

---

## Upgrade

```bash
npm install -g oh-my-opencode@3.5.0
# or
bun install -g oh-my-opencode@3.5.0
```

---

**Thank you to our community contributors:**
- @nianyi778: Add ELESTYLE to "Loved by professionals at" section
- New CLA signers: @RobertWsp, @materializerx, @cyberprophet, @lxia1220, @mrm007, @aliozdenisik, @JunyeongChoi0

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.4.0...v3.5.0

LFG ulw ulw!


## [3.4.0] - 2026-02-08

# v3.4.0 — Context Continuity

## What's New

### 🎯 Context Preservation: `/handoff`

The headline feature. Your subagent is deep in work. Compaction is coming. Context is about to vanish.

**`/handoff` solves this.** Synthetically transfer session context—programmatically—to a new session before compaction strikes. Preemptively preserve what matters. Continue where you left off.

```typescript
// Preserve context before compaction
await handoff({
  targetSession: 'new-session-id',
  context: synthesizeContext(currentSession)
})
```

No more losing critical state mid-work.

---

## Features

### Claude Tasks Integration
- `CLAUDE_CODE_TASK_LIST_ID` environment variable support
- Direct integration with Claude Code task lists
- Seamless workflow between oh-my-opencode and Claude Tasks

### Anthropic Prefill Auto-Recovery
- Automatically detects Anthropic assistant message prefill deprecation
- Auto-bypasses the restriction
- Zero manual intervention needed

### Background Task Visibility
- Background output now shows task titles
- Know exactly which task just completed
- Better multi-task workflow monitoring

### Session Permission Management
- CLI `run` command properly propagates permissions
- Background agents receive correct session permissions
- Consistent permission model across execution contexts

### Git Diff Stats Utility
- Infrastructure for collecting worktree changes
- Foundation for better change tracking and reporting

---

## Fixes

### Critical Behavior Fixes
- **#1428**: Prometheus now banned from bash execution (security)
- **#1295**: Category delegation respects user model settings
- **#1357**: Subagent type path respects user agent model settings
- **#1366**: LSP safety blocks no longer persist after server restart
- **#1582**: Background task parallel completion race condition eliminated
- **#1623**: Custom agents visible to orchestrator + init deadlock resolved

### Integration Fixes
- **#1627**: Exa MCP API key config fixed (removed duplicate headers + proper URL encoding)
- **#1493**: `load_skills` parameter now has proper defaults

### Agent System Fixes
- **#1233**: Ralph/ULW loop `<promise>DONE</promise>` tag detection restored
- Prometheus/Plan mutual exclusion — prevents cross-delegation loops
- Sync continuation preserves variant (thinking budget) correctly
- Plan agent inherits Prometheus model settings properly

---

## Refactoring

### Module Size Reduction
Split 6 massive modules into <200 LOC each for maintainability:
- `background-task`
- `call-omo-agent`
- `interactive-bash-session`
- `tmux-subagent`
- `delegate-task`
- `atlas`

### Code Organization
- `skill-resolver` extracted as standalone module
- `config-handler` type safety improvements
- Better separation of concerns across codebase

---

## Stats

**102 files changed**  
**+5,919 additions**  
**-2,263 deletions**

---

## Breaking Changes

None. This release is backward-compatible.

---

## Upgrade

```bash
npm install -g oh-my-opencode@3.4.0
# or
bun install -g oh-my-opencode@3.4.0
```

---

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.3.2...v3.4.0

LFG ulw ulw!
---

## What's Changed

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.4.0...v3.4.0


## [3.3.2] - 2026-02-08

## What's Changed

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.3.2...v3.3.2


## [3.3.1] - 2026-02-07

## What's Changed

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.3.1...v3.3.1


## [3.3.0] - 2026-02-07

# Hi Subagents! 👋

**The headline:** Subagents are no longer black boxes. Click on a `task` tool call in the UI and see exactly what you delegated — prompt, description, model, session ID, the whole story.

## `delegate_task` → `task`: From Mystery to Transparency

Before v3.3.0, spawning a subagent meant sending it off into the void. You gave it a prompt, crossed your fingers, and waited. Want to know what instructions you actually sent? Tough luck — `delegate_task` kept its secrets.

**Now with `task`:**
- **Click to inspect**: Every `task` tool call is clickable in the UI. One click reveals the full context.
- **ctx.metadata()**: Subagent tasks now store title, description, prompt, category, model — everything you need.
- **storeToolMetadata()**: Tool calls aren't just executed; they're documented.

Delegation isn't a leap of faith anymore — it's observable, debuggable, transparent.

## Also Shipped

**CLI**: `--port`, `--attach`, `--session-id`, `--on-complete`, `--json` flags for `run`
**Opus 4.6**: Auto `effort=max` via anthropic-effort hook
**Plugin safety**: `plugin_load_timeout_ms`, `safe_hook_creation`, `safeCreateHook()`
**ACP (Zed)**: 18x `session.prompt` → `promptAsync` fix
**MCP config**: Reads both `~/.claude.json` and `~/.claude/.mcp.json`
**UserPromptSubmitHooks**: Now fires on every prompt
**Compaction**: TODO preservation improved
**Cascade cancel**: Parent deletion cancels child subagents
**Windows**: Multiple crash fixes
**Desktop app**: Cross-platform path support
**Migration**: System modularization

LFG ulw ulw! 🔥

---

## What's Changed

### Features

- **cli**: extend run command with port, attach, session-id, on-complete, and json options
- **config**: add plugin_load_timeout_ms and safe_hook_creation experimental flags
- **shared**: add safeCreateHook utility for error-safe hook creation
- register anthropic-effort hook in plugin lifecycle
- add anthropic-effort hook to inject effort=max for Opus 4.6

### Bug Fixes

- **mcp-loader**: also read ~/.claude/.mcp.json for CLI-managed user MCP config
- **look-at**: remove isJsonParseError band-aid (root cause fixed)
- **tools**: switch session.prompt to promptAsync in delegate-task and call-omo-agent
- **hooks**: switch session.prompt to promptAsync in all hooks
- **background-agent**: switch session.prompt to promptAsync
- **core**: switch compatibility shim to promptAsync
- **shared**: switch promptWithModelSuggestionRetry to use promptAsync
- **hooks**: fire UserPromptSubmitHooks on every prompt, not just first (#594)
- **mcp-loader**: read user-level MCP config from ~/.claude.json (#814)
- **skill-loader**: filter discovered skills by browserProvider (#1563)
- skip ultrawork injection for plan-like agents (#1501)
- **migration**: stop task_system backup writes (#1561)
- rewrite dedup recovery test to mock module instead of filesystem
- use lazy storage dir resolution to fix CI test flakiness
- wire deduplication into compaction recovery for prompt-too-long errors (#96)
- register compaction todo preserver
- add compaction todo preserver hook
- avoid invented compaction constraints
- ensure truncated result stays within maxLength limit
- cascade cancel descendant tasks when parent session is deleted (#114)
- update session-manager tests to use factory pattern
- use character limit instead of sentence split for skill description (#358)
- allow string values for commit_footer config (#919)
- use ctx.directory instead of process.cwd() in tools for Desktop app support
- normalize resolvedPath before startsWith check
- expand ALLOWED_AGENTS to include all subagent-capable agents
- boulder continuation now respects /stop-continuation guard
- anchor .sisyphus path check to ctx.directory to prevent false positives
- use platform-aware binary detection (where on Windows, which on Unix)
- allow dash-prefixed arguments in CLI run command
- don't fallback to system 'sg' command for ast-grep
- allow dash-prefixed arguments in CLI run command
- make model migration run only once by storing history in _migrations field
- explicitly pass encoding/callback args through stdout.write wrapper
- **test**: remove shadowed consoleErrorSpy declarations in on-complete-hook tests
- address cubic 4/5 review issues
- **test**: mock SDK and port-utils in integration test to prevent CI failure
- clear race timeout after plugin loading settles
- **index**: wrap hook creation with safeCreateHook + add defensive optional chaining (#1559)
- **config-handler**: add timeout + error boundary around loadAllPluginComponents (#1559)
- trim whitespace from tool names to prevent invalid tool calls
- allow Prometheus to overwrite .sisyphus/*.md plan files
- **hooks**: add defensive null check for matcher.hooks to prevent Windows crash (#441)
- respect user-configured agent models over system defaults
- respect user-configured agent models over system defaults
- guard against undefined modelID in anthropic-effort hook

### Refactoring

- **migration**: split model and category helpers (#1561)
- **migration**: extract agent and hook maps (#1561)
- extract context window recovery hook
- migrate delegate_task to task tool with metadata fixes

### Documentation

- add comprehensive local testing guide for acp-json-error branch

### Other Changes

- Merge pull request #1620 from potb/acp-json-error
- Merge pull request #1621 from code-yeongyu/fix/814-mcp-config-both-paths
- Merge pull request #1616 from code-yeongyu/fix/814-user-mcp-config
- Merge pull request #1618 from code-yeongyu/fix/594-user-prompt-submit-fires-once
- Merge pull request #1615 from code-yeongyu/fix/1563-browser-provider-gating
- Merge pull request #1584 from code-yeongyu/fix/441-matcher-hooks-undefined
- Merge pull request #1614 from code-yeongyu/fix/1501-ulw-plan-loop
- Merge pull request #1613 from code-yeongyu/fix/1561-dead-migration
- Merge pull request #1610 from code-yeongyu/fix/96-compaction-dedup-recovery
- Merge pull request #1611 from code-yeongyu/fix/1481-1483-compaction
- Merge pull request #1607 from code-yeongyu/fix/358-skill-description-truncation
- Merge pull request #1608 from code-yeongyu/fix/114-cascade-cancel
- Merge pull request #1606 from code-yeongyu/fix/658-tools-ctx-directory
- Merge pull request #1605 from code-yeongyu/fix/919-commit-footer-v2
- Merge pull request #1593 from code-yeongyu/fix/prometheus-plan-overwrite
- Merge pull request #1604 from code-yeongyu/fix/957-allowed-agents-dynamic
- Merge pull request #1594 from code-yeongyu/fix/boulder-stop-continuation
- Merge pull request #1603 from code-yeongyu/fix/1269-windows-which-detection
- Merge pull request #1601 from code-yeongyu/fix/899-cli-run-dash-args
- Merge pull request #1602 from code-yeongyu/fix/1365-sg-cli-path-fallback
- Merge pull request #1597 from code-yeongyu/fix/899-cli-run-dash-args
- Merge pull request #1595 from code-yeongyu/fix/tool-name-whitespace
- Merge pull request #1592 from code-yeongyu/fix/issue-1570-onetime-migration
- Merge pull request #1590 from code-yeongyu/feat/run-cli-extensions
- Merge pull request #1585 from code-yeongyu/fix/1559-crash-boundary
- Revert "Merge pull request #1578 from code-yeongyu/fix/user-configured-model-override"
- Merge pull request #1578 from code-yeongyu/fix/user-configured-model-override
- Merge pull request #1564 from code-yeongyu/feat/anthropic-effort-hook
- Merge pull request #1543 from code-yeongyu/feat/task-tool-refactor

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.2.4...v3.3.0


## [3.2.4] - 2026-02-06

# What a wild day.

GPT 5.3 Codex and Claude Opus 4.6 dropped on the same day. That's not a coincidence — that's the universe telling us we're living through something historic. Two frontier model providers, shipping simultaneously. Monumental.

And we adopted both **the same day they shipped**. 

**108 files changed. +4,666/-4,625 lines.** A same-day sweep from one end of the codebase to the other. When the frontier moves, we move with it.

---

### **Hephaestus: The Legitimate Craftsman Evolves** 🔨

New mindset: **"KEEP GOING. SOLVE PROBLEMS."**

Autonomous recovery got smarter. Hephaestus now tries **3 different approaches** before bothering you. Stuck on a bug? He'll pivot, retry, adapt — all on his own. This is what autonomous execution should feel like.

Plus: provider-based activation. Got OpenAI, Copilot, or OpenCode connected? Hephaestus is ready. No exact model matching gymnastics required.

### **Custom Skills: First-Class Citizens**

User-installed skills now get **HIGH PRIORITY** treatment in prompts. No more blending in with builtins — they're clearly separated, emphasized, and respected. Your custom workflows matter.

### **Safety First: Write Guard**

New hook blocks agents from silently overwriting existing files. The write tool now checks before clobbering. Peace of mind.

---

## **What's New**

**Models**
- Claude Opus 4.5 → 4.6, GPT 5.2 Codex → 5.3 Codex across 108 files
- Auto-migration: `MODEL_VERSION_MAP` upgrades your configs on load automatically
- Claude Opus 4.6 prioritized in anthropic fallback chains

**Hephaestus**
- "KEEP GOING. SOLVE PROBLEMS." mindset upgrade
- 3-approach-first recovery rule before escalating to user
- Provider-based gating: activates by connectivity, not exact model match

**Skills**
- Dynamic skill priority: user-installed skills emphasized with HIGH PRIORITY
- `formatCustomSkillsBlock()` extracted as shared DRY function

**Safety & UX**
- Write existing file guard: blocks overwrite of existing files
- Auto port selection: finds next available when 4096 is busy
- `look_at` image_data support: paste/clipboard images now work

**Task System**
- Task global storage with `ULTRAWORK_TASK_LIST_ID` support

---

## **Fixes**

- Atlas continuation guard: stops infinite retry loops
- Compaction model-agnostic: removed hardcoded Claude model prefix
- Sisyphus-Junior: uses category model instead of UI-selected model
- Plan agent: dynamic categories/skills (not hardcoded)
- Schema sync: Zod schemas aligned
- Regex special chars escaped in pattern matcher
- Disabled tools actually enforced now
- Glob/Grep uses `process.cwd()` correctly
- Background agent abort handled gracefully
- Custom skills env var restoration fixed
- Provider cache handles both `string[]` and `object[]` formats
- LSP Windows: uses Node.js child_process (avoid Bun segfault)
- Boulder state agent tracking fixed
- Model availability honors connected providers
- Auto-update uses correct config dir
- Duplicate fallback entries cleaned

---

## **Refactoring**

- Dead code removal: `ollama-ndjson-parser.ts`, `plugin-state.ts`, unused types
- Schema build: `z.toJSONSchema` → `zodToJsonSchema`
- `formatCustomSkillsBlock` DRY extraction

## **Docs**

- `AGENTS.md` regenerated across all directories
- Config/feature docs updated

---

This is what shipping looks like when the frontier moves. Two models, one day, immediate adoption.

LFG 🔥 ulw ulw

---

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.2.3...v3.2.4


## [3.2.3] - 2026-02-04

## What's Changed

### ✨ Features

- **Multi-provider websearch support** - Choose between Exa (default) and Tavily for web search (#1371 by @YanzheL)
- **Nested skill directories** - Skills can now be organized in subdirectories for better organization (#1254 by @LeekJay)
- **Disabled skills support** - Add `disabledSkills` config to selectively disable skills

### 🐛 Bug Fixes

#### Authentication & Server
- Fix OpenCode Desktop server unauthorized error on subagent spawn (#1399 by @ualtinok, @boguan)
- Add graceful fallback for server auth injection

#### Model & Provider
- Prefer exact model ID match in fuzzyMatchModel - fixes wrong model selection (#1460)
- Use supported variant for gemini-3-pro (#1463)
- Avoid `propertyNames` in skill-mcp for Gemini compatibility (#1465)
- Honor explicit category model over sisyphus-junior default

#### Skill Loader
- Respect `disabledSkills` in async skill resolution (caching bug)
- Deterministic collision handling for duplicate skill names (#1370 by @misyuari)

#### LSP & Tools
- Prevent stale diagnostics by syncing `didChange` before fetching (#1280 by @Zacks-Zhang)
- Fix overridden tools (glob, grep) path resolution for OpenCode Desktop

#### Agents & Hooks
- Deduplicate settings paths to prevent double hook execution (#1297 by @khduy)
- Honor tools overrides via permission migration (#1289 by @KonaEspresso94)
- Block bash commands in Prometheus mode to respect permission config (#1449 by @kaizen403)
- Abort session on model suggestion retry failure
- Add read-only restrictions for Metis and Momus agents

#### Shell & Environment
- Use `detectShellType()` instead of hardcoded 'unix' for cross-platform support (#1459)
- Force unix export syntax for bash env prefix in non-interactive environments

#### CI/CD
- Use regex variables for bash 5.2+ compatibility in changelog generation

### 🎨 Style
- Update Hephaestus and Prometheus agent colors

### 📚 Documentation
- Clarify Prometheus invocation workflow (#1466)
- Instruct curl over WebFetch for installation (#1461)
- Document websearch provider configuration
- Fix broken TOC links in translated READMEs (#1384 by @devxoul)

### 🔧 Other
- Respect user-configured agent variant in doctor command (#1464)
- Lazy evaluation prevents crash when websearch disabled

---

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.2.2...v3.2.3


## [3.2.2] - 2026-02-03

## v3.2.2

### 🚀 GPT-5.2 Prompt Optimization
- **Atlas, Sisyphus-Junior, Oracle**: Model-based prompt routing with GPT-5.2 optimized prompts (XML structure, verbosity constraints, explicit decision criteria)

### 🧪 Experimental: Claude Code-style Task System
- **New Tools**: `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate` for structured task management
- **File-based Storage**: Tasks stored in `.sisyphus/tasks/` with Claude Code compatible schema
- ⚠️ **Important Limitation**: This is **experimental** and does **NOT sync with OpenCode's Todo UI**. Enabling this will disable `TodoWrite` - todos won't appear in TUI. This is a known UX downgrade. We're exploring SDK integration solutions.
- **Enable**: Set `experimental.task_system: true` in config

### ✨ Agent & Hook Improvements
- **Faster Exploration**: `grok-code-fast-1` as default explore agent model
- **Preemptive Compaction**: Auto-summarizes session at 78% context usage (Anthropic models)
- **Agent Fallback**: First-run without cache now works properly
- **CLI**: Added `default_run_agent` config and `OPENCODE_DEFAULT_AGENT` env var

### 🐞 Bug Fixes
- **config**: Plan agent no longer inherits Prometheus prompt on demote
- **background-cancel**: Skip notification when user explicitly cancels tasks
- **delegate-task**: Fixed sisyphus-junior model override precedence
- **prompts**: Added missing `run_in_background`, `load_skills` params in examples

### 🛠 New Skills
- **github-pr-triage**: Streaming PR analysis with background tasks
- **github-issue-triage**: Streaming issue analysis

---

## What's Changed

### Features
- **delegate-task**: add actionable TODO list template to plan agent prompt
- **auto-slash-command**: add builtin commands support and improve part extraction
- **agents**: add GPT-5.2 optimized prompt for sisyphus-junior
- **tasks-todowrite-disabler**: improve error message with actionable workflow guidance
- **agents**: add useTaskSystem flag for conditional todo/task discipline prompts
- **agents**: add Todo Discipline section to Hephaestus prompt
- **task-system**: add experimental task system with Claude Code spec alignment
- **agents**: respect uiSelectedModel in Atlas model resolution
- add agent fallback and preemptive-compaction restoration
- **agents**: add grok-code-fast-1 as primary model for explore agent
- **skills**: add streaming mode and todo tracking to triage skills
- **agents**: restructure atlas agent into modular directory with model-based routing
- **task**: add real-time single-task todo sync via OpenCode API
- **task**: refactor to Claude Code style individual tools
- **cli**: implement default agent priority in run command
- **config**: add default_run_agent schema option
- **skills**: add github-pr-triage skill and update github-issue-triage
- **config**: disable todowrite/todoread tools when new_task_system_enabled

### Bug Fixes
- **config**: prevent plan agent from inheriting prometheus prompt on demote
- **background-cancel**: skip notification when user explicitly cancels tasks
- **config-handler**: preserve plan prompt when demoted
- **prometheus**: enforce path constraints and atomic write protocol
- **prompts**: add missing run_in_background and load_skills params to examples
- **delegate-task**: honor sisyphus-junior model override precedence
- honor agent variant overrides
- **task-tool**: add task ID validation and improve lock acquisition safety

### Refactoring
- **ultrawork**: simplify workflow and apply parallel context gathering
- **config-handler**: separate plan prompt into dedicated configuration
- **background-agent**: optimize lifecycle and simplify tools
- **oracle**: optimize prompt for GPT-5.2 with XML structure and verbosity constraints
- **prometheus**: replace binary verification with layered agent-executed QA
- **task**: update schema to Claude Code field names

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.2.1...v3.2.2


## [3.2.1] - 2026-02-01

## Bug Fixes

- **background-agent**: prevent concurrency slot leaks on task startup failures
- **cli**: add -preview suffix for GitHub Copilot Gemini model names
- **ci**: add shell: bash to retry action for Windows compatibility


## [3.2.0] - 2026-02-01

# 3.2.0 — Meet Hephaestus 🔨

## Highlights

### 🔥 Hephaestus: The Legitimate Craftsman Agent

![Meet Hephaestus](https://github.com/code-yeongyu/oh-my-opencode/raw/dev/.github/assets/hephaestus.png)

In Greek mythology, Hephaestus was the god of forge, fire, metalworking, and craftsmanship—the divine blacksmith who crafted weapons for the gods.

**Meet our new autonomous deep worker: Hephaestus (GPT 5.2 Codex Medium).**

*Why "Legitimate"? When Anthropic blocked third-party access citing ToS violations, the community started joking about "legitimate" usage. Hephaestus embraces this irony—he's the craftsman who builds things the right way.*

**Key Characteristics:**
- **Goal-Oriented**: Give him an objective, not a recipe. He determines the steps himself.
- **Explores Before Acting**: Fires 2-5 parallel explore/librarian agents before writing a single line of code.
- **End-to-End Completion**: Doesn't stop until the task is 100% done with evidence of verification.
- **Pattern Matching**: Searches existing codebase to match your project's style—no AI slop.
- **Legitimate Precision**: Crafts code like a master blacksmith—surgical, minimal, exactly what's needed.

Inspired by [AmpCode's deep mode](https://ampcode.com)—autonomous problem-solving with thorough research before decisive action.

---

## What's New

### Features
- **agents**: Add Hephaestus - autonomous deep worker agent (#1287)
- **babysitting**: Make unstable-agent-babysitter always-on by default
- **todo-continuation**: Show remaining tasks list in continuation prompt
- **doctor**: Detect OpenCode desktop GUI installations on all platforms (#1352)
- **skill-mcp-manager**: Enhance manager with improved test coverage
- **hooks**: Add unstable-agent-babysitter hook for monitoring unstable background agents
- **background-agent**: Add isUnstableAgent flag for unstable model detection
- **background_output**: Add thinking_max_chars option
- **ci**: Auto-generate structured release notes from conventional commits

### Bug Fixes
- **Windows**: Improve compatibility and fix event listener issues (#1102)
- **config**: Properly handle prompt_append for Prometheus agent (#1271)
- **tmux**: Send Ctrl+C before kill-pane and respawn-pane to prevent orphaned processes (#1329)
- **tests**: Properly stub notifyParentSession and fix timer-based tests
- **non-interactive-env**: Always inject env vars for git commands
- **background-agent**: Abort session on task completion to prevent zombie attach processes
- **ci**: Add retry logic for platform binary builds

### Refactoring
- **background-agent**: Show category in task completion notification
- **delegate-task**: Improve session title format and add task_metadata block
- **background-agent**: Optimize task timing and constants management
- **agents**: Improve explore/librarian prompt examples with 4-part context structure
- Major codebase cleanup - BDD comments, file splitting, bug fixes (#1350)

### Documentation
- **background-task**: Enhance background_output tool description with full_session parameter

---

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.1.11...v3.2.0


## [3.1.11] - 2026-02-01

## What's Changed

### Features
- **Oracle Safety Review**: Added Oracle deployment safety review to `/get-unpublished-changes` command for pre-release analysis
- **Stop Continuation Command**: New `/stop-continuation` command to halt all continuation mechanisms (ralph loop, todo continuation, boulder)
- **GLM-4.7 Thinking Mode**: Added thinking mode support for GLM-4.7 model

### Bug Fixes
- **Memory Leak Prevention**: Track and cancel completion timers in background-agent to prevent memory leaks
- **Zombie Process Prevention**: Proper process lifecycle management to prevent zombie processes
- **Windows LSP Fix**: Added Bun version check for Windows LSP segfault bug
- **Session Recovery**: Fixed `/stop-continuation` to be one-time only and respect session recovery
- **Start Work Fix**: Always switch to atlas in `/start-work` to fix Prometheus sessions
- **Test Stability**: Added missing ToolContext fields to test mocks and consistent `_resetForTesting()` usage
- **Dependencies**: Regenerated bun.lock to restore vscode-jsonrpc dependency

### Refactoring
- Removed orphaned `compaction-context-injector` hook
- Consolidated duplicate patterns and simplified codebase (binary-downloader, model-resolution-pipeline, session-injected-paths)

### Documentation
- Added `github-issue-triage` skill with exhaustive pagination enforcement

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.1.10...v3.1.11


## [3.1.10] - 2026-01-31

No notable changes


## [3.1.9] - 2026-01-30

# Hi Kimi! 👋

This release welcomes **Kimi K2.5** to the oh-my-opencode family!

> **Personal Note**: I've been testing Kimi K2.5 as an Atlas orchestrator, and it's been performing **better than Claude Sonnet 4.5** in my workflows. Seriously impressive for a free model.

---

## What's New in 3.1.9

### Features
- **Kimi For Coding provider**: New provider option in installer for Sisyphus/Prometheus/Atlas fallback
- **kimi-k2.5 fallback chains**: Added to sisyphus, atlas, prometheus, metis, multimodal-looker agents
- **deep category**: Goal-oriented autonomous problem-solving with thorough research before action
- **artistry category**: Creative, unconventional approaches beyond standard patterns
- **requiresModel field**: Conditional category activation based on model availability
- **model-suggestion-retry**: Auto-retry with provider-suggested model on not found errors
- **isModelAvailable helper**: Fuzzy match model availability checking

### Fixes
- Model resolution now falls back to client API when cache is empty/unknown
- Atlas properly respects fallbackChain and refreshes provider-models cache
- Fixed gh api command for starring repo
- Subagents no longer affected by UI model selection override
- npm OIDC publish fixes

### Improvements
- ultrabrain category revamped with deep work mindset and code style requirements
- Replaced console.log/warn/error with file-based log() for silent logging
- Replaced big-pickle with glm-4.7-free for librarian fallback
- Oracle fallback prioritizes gemini-3-pro over opus
- momus opus fallback now includes variant max

### Test Improvements
- Optimized test suite with FakeTimers and race condition fixes


## [3.1.8] - 2026-01-30

## Bug Fixes

- 30f893b7 fix(cli/run): fix [undefine] tag and add text preview to verbose log
- c905e1cb fix(delegate-task): restore resolved.model to category userModel chain (#1227)
- 5f0b6d49 fix(run): prevent premature exit on idle before meaningful work (#1263)

## Refactoring

- d3e2b36e refactor(tmux-subagent): introduce dependency injection for testability (#1267)

---

No notable changes


## [3.1.7] - 2026-01-29

## What's New in v3.1.7

### 🔐 MCP OAuth 2.1 Authentication (#1169)
Full OAuth 2.1 support for MCP servers — RFC 7591 (Dynamic Client Registration), RFC 9728 (Protected Resource Metadata), RFC 8414 (Authorization Server Discovery), RFC 8707 (Resource Indicators). Includes secure token storage, step-up authorization, and CLI commands (`opencode mcp oauth login/logout/status`).

### 🔧 LSP Client Migration to vscode-jsonrpc (#1095)
Replaced custom JSON-RPC implementation with `vscode-jsonrpc` library for improved protocol stability. Bun↔Node stream bridges for compatibility. ~60 line net reduction.

### Bug Fixes
- **background-agent**: Prevent zombie processes by aborting all child sessions on shutdown (#1240)
- **model-resolver**: Respect UI model selection in agent initialization (#1158)
- **model-resolver**: Use connected providers cache when model cache is empty (#1227)
- **delegate-task**: Pass registered agent model explicitly for subagent_type (#1225)
- **start-work**: Prevent overwriting session agent if already set; inherit parent model (#1201)
- **config**: Expand override.category and explicit reasoningEffort priority (#1219)
- **test**: Migrate config-handler tests from mock.module to spyOn to prevent cross-file cache pollution

### Documentation
- Add missing configuration options to configurations.md (#1186)
- Add OAuth 2.1 feature documentation and CLI guide

---

## Commits

- dcda8769 feat(mcp-oauth): add full OAuth 2.1 authentication for MCP servers (#1169)
- a94fbadd Migrate LSP client to vscode-jsonrpc for improved stability (#1095)
- 23b49c4a fix: expand override.category and explicit reasoningEffort priority (#1219) (#1235)
- b4973954 fix(background-agent): prevent zombie processes by aborting sessions on shutdown (#1240) (#1243)
- 34aaef22 fix(delegate-task): pass registered agent model explicitly for subagent_type (#1225)
- faca80ca fix(start-work): prevent overwriting session agent if already set; inherit parent model for subagent types (#1201)
- 0c3fbd72 fix(model-resolver): respect UI model selection in agent initialization (#1158)
- bffa1ad4 fix(model-resolver): use connected providers cache when model cache is empty (#1227)
- c7455708 docs: Add missing configuration options to configurations.md (#1186)
- cd4da93b fix(test): migrate config-handler tests from mock.module to spyOn
- 71b2f151 chore(agents): unify agent description format with OhMyOpenCode attribution


## [3.1.6] - 2026-01-28

No notable changes


## [3.1.5] - 2026-01-28

## Changes

- 03f6e72c refactor(ultrawork): replace prometheus with plan agent, add parallel task graph output
- 4fd9f0fd refactor(agents): enforce zero user intervention in QA/acceptance criteria
- 895f366a docs: add Ollama streaming NDJSON issue guide and workaround (#1197)
- acc19fcd feat(hooks): auto-disable directory-agents-injector for OpenCode 1.1.37+ native support (#1204)
- dee89c15 feat(delegate-task): add prometheus self-delegation block and delegate_task permission
- 3dd80889 fix(tools): add permission field to session.create() for consistency (#1199)
- 8f6ed5b2 fix(hooks): add null guard for tool.execute.after output (#1054)
- 01500f1e fix: prevent system-reminder tags from triggering mode keywords (#1155)
- 48f6c5e0 fix(skill): support YAML array format for allowed-tools field (#1163)
- 3e32afe6 fix(agent-variant): resolve variant based on current model, not static config (#1179)
- d11c4a1f fix: guard JSON.parse(result.stdout) with || "{}" fallback in hook handlers (#1191)

---

No notable changes


## [3.1.4] - 2026-01-28

## What's Changed

### New Features
- **Provider Cache Warning Toast**: Show toast notification when provider cache is missing, helping users understand model resolution issues (#1da0adcb)

### Bug Fixes
- **Version Detection for npm Global Installations**: Fixed version detection to work correctly with npm global installs (#1194)
- **Model Resolver**: Skip fallback chain when no provider cache exists to prevent errors (#8a9d966a)
- **Config Schema**: Added 'dev-browser' to BrowserAutomationProviderSchema (#76f8c500)

### CI & Testing Improvements
- Improved test isolation for parallel execution stability
- Fixed CI test timeouts with configurable timing
- Enhanced mock handling in delegate-task tests

### Contributors
Thanks to @agno01 and @zycaskevin for signing the CLA!

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.1.3...v3.1.4


## [3.1.3] - 2026-01-27

## What's Changed in v3.1.3

### 🔧 Bug Fixes
- **delegate-task**: Pass variant as top-level field in prompt body
- **background-agent**: Pass variant as top-level field in prompt body  
- **keyword-detector**: Skip ultrawork injection for planner agents
- **prometheus**: Set mode to 'all' and restore plan demote logic
- **plan-agent**: Only inherit model from prometheus as fallback
- **mcp**: Add optional Context7 `Authorization` header (#1133)
- **mcp**: Prevent builtin MCPs from overwriting user MCP configs (#956)
- **compaction**: Preserve agent verification state (#1144)
- **notification**: Prevent false positive plugin detection (#1148)
- **cli**: Add baseline builds for non-AVX2 CPUs (#1154)
- **delegate-task**: Add clear error when model not configured (#1139)

### ✨ Features
- **sisyphus**: Add foundation schemas for tasks and swarm (Wave 1)
- **subagent**: Block question tool at both SDK and hook level
- **workflow**: Add ZAI Coding + OpenAI provider for sisyphus-agent
- **prompts**: Enhance plan output with TL;DR, agent profiles, and parallelization
- **server**: Support `OPENCODE_SERVER_PORT` and `OPENCODE_SERVER_HOSTNAME` env vars (#1157)

### 📝 Documentation
- Clarify category model resolution priority and fallback behavior (#1074)

### 🧪 Tests & CI
- Fix flaky tests caused by `mock.module` pollution across parallel test files
- Isolate mock-heavy test files to prevent parallel pollution in CI
- Skip flaky sync variant test (CI timeout)
- Add tests for plan demote and prometheus mode

### 🔄 Reverts
- Revert "Add oh-my-opencode-slim (#1100)"
- Revert "docs: add v2.x to v3.x migration guide (#1057)"

### 👥 New Contributors
- @moha-abdi signed the CLA
- @MoerAI signed the CLA

**Full Changelog**: https://github.com/code-yeongyu/oh-my-opencode/compare/v3.1.2...v3.1.3


## [3.1.2] - 2026-01-27

No notable changes


## [3.1.1] - 2026-01-26

## Patch Release v3.1.1

### Features
- **plan-agent**: Apply prometheus config with fallback chain
- **plan-agent**: Enforce dependency/parallel graphs and category+skill recommendations
- **ultrawork**: Enforce plan agent invocation and parallel delegation
- **delegate-task**: Prepend system prompt for plan agent invocations
- **config**: Add thinking/reasoningEffort/providerOptions to AgentOverrideConfigSchema
- Make systemDefaultModel optional for OpenCode fallback

### Bug Fixes
- **background-agent**: Disable question tool for background tasks

### Tests & Docs
- Add version display test to verify package.json reading
- Add tmux integration and interactive terminal documentation
- Add server mode and shell function examples for tmux integration

---

No notable changes


## [3.1.0] - 2026-01-26

## New Features

### Tmux Pane Management for Background Agents
- **2D Grid Layout**: Background agent sessions now support 2D grid layout with intelligent divider-aware calculations
- **Replace Action**: New replace action prevents mass eviction when managing tmux panes
- **State-First Architecture**: Complete refactor with decision engine for reliable pane state management

<img width="1909" height="982" alt="image" src="https://github.com/user-attachments/assets/8968e0da-636f-4344-b82e-1f0db32a036e" />


### Browser Automation Skills
- **agent-browser**: New browser automation skill for web scraping, testing, and interaction
- **dev-browser**: Browser automation with persistent page state, supports Windows

### Enhanced Hooks
- **Category-Skill Reminder**: Reminds orchestrators about available categories and skills for delegation
- **Sisyphus Junior Notepad**: Conditional notepad rules injection for subagents
- **Active Working Context**: Compaction summary now includes active working context section

### Model & Provider Improvements
- **Connected Providers Cache**: New cache for model availability tracking
- **Explore Fallback**: Added `github-copilot/gpt-5-mini` to explore agent fallback chain

## Bug Fixes
- fix: generate skill/slashcommand descriptions synchronously when pre-provided (#1087)
- fix(tmux-subagent): enable 2D grid layout with divider-aware calculations

## Documentation
- docs(agent-browser): add detailed installation guide with Playwright troubleshooting
- docs: regenerate AGENTS.md knowledge base

---

No notable changes


## [3.0.1] - 2026-01-25

## What's New in v3.0.1

### Bug Fixes
- fix: add missing `name` property in `loadBuiltinCommands` causing TypeError on slashcommand
- fix: remove github-copilot association from gpt-5-nano model mapping
- fix(ralph-loop): skip user messages in transcript completion detection (#1086)
- fix: update documentation to use `load_skills` instead of `skills` parameter (#1088)
- docs: fix atlas agent name case in example config

### Refactoring & Cleanup
- refactor: sync `delegate_task` schema with OpenCode Task tool (resume→session_id, add command param)
- refactor(ultrawork): replace vague plan agent references with explicit `delegate_task(subagent_type="plan")` invocation syntax
- refactor: remove dead re-exports from tools barrel
- refactor: remove deprecated `config-path.ts` (dead code)
- refactor: remove unused background-compaction hook module

### Community
- New CLA signatures from @kvokka, @potb, @jsl9208, @sadnow, @ThanhNguyxn, @AamiRobin

---

No notable changes


## [3.0.0] - 2026-01-24

# v3.0.0: The Orchestration Revolution 🚀

We are thrilled to announce the release of **oh-my-opencode v3.0.0**. This major update transforms how agents are deployed and managed, moving away from static definitions toward a dynamic, intelligent orchestration ecosystem.

## 🧩 Dynamic Agent Composition: Categories & Skills

We've introduced **Categories** (model abstractions) and **Skills**, allowing you to configure sub-agents dynamically. 

*   **Beyond Hardcoded Agents:** The legacy "Frontend UI/UX Engineer" has been retired. In its place, the **Sisyphus** agent now dynamically combines the `visual-engineering` category with the `frontend-ui-ux` skill to assign the perfect agent for the task.
*   **Precision Sub-Agents:** Need efficient Git management? Combine the `quick` category with the `git-master` skill to spawn a lightweight, specialized sub-agent that follows your project's specific Git conventions.
*   **Extensible & Smart:** This system is fully customizable and scalable. As always, Sisyphus intelligently handles these combinations behind the scenes.

📚 [Category & Skill Guide](https://github.com/code-yeongyu/oh-my-opencode/blob/master/docs/category-skill-guide.md)

## 🔥 Enhanced Sisyphus & Ultrawork Mode

The core **Sisyphus** agent is now more proactive than ever. We've refined its prompts to encourage more aggressive delegation and assistance-seeking. Additionally, **Ultrawork Mode** has been optimized for tighter alignment, ensuring the agent stays perfectly on track during intense coding sessions.

## 🧠 Meet Prometheus: The Strategic Planner

Introducing **Prometheus**, a new agent designed to minimize your cognitive load while maximizing planning accuracy. 
*   Prometheus conducts an "interview" with you, asking deep, clarifying questions until every requirement is crystal clear.
*   To ensure nothing is missed, Prometheus consults other specialized agents after drafting the work plan to verify the strategy.

## 🏗️ Atlas: The Master Orchestrator

Once your plan is ready, simply type `/start-work` to activate **Atlas**, our powerful new orchestration mode.
*   **Right Tool, Right Job:** Atlas manages the entire lifecycle, mixing Categories and Skills to deploy the most efficient agent for every sub-task.
*   **Relentless Verification:** Atlas obsessively checks and validates every step against the work plan. If a task fails, it automatically resumes the agent to fix the issue.
*   **Cost Efficiency:** By using Atlas, you can optimize token usage across providers—for example, using **Sonnet** for orchestration, **GLM 4.7** for daily tasks, **Haiku 4.5** for quick fixes, and **GPT 5.2 Codex X-High** for complex backend logic.

📚 [Orchestration Guide](https://github.com/code-yeongyu/oh-my-opencode/blob/master/docs/orchestration-guide.md)

## 🛠️ Reimagined Installation & DX

We've overhauled the setup experience to get you up and running faster:
*   **Interactive CLI Installer:** A smooth, guided setup process.
*   **Auto Model Mapping:** Automatically maps models based on your subscription status.
*   **Native Binaries:** Platform-specific binaries allow you to run without a local runtime.
*   **Multi-Provider Support:** Full compatibility with GitHub Copilot, OpenCode Zen, Z.ai Coding Plan, and more.

📚 [Installation Guide](https://github.com/code-yeongyu/oh-my-opencode/blob/master/docs/guide/installation.md)

## 🔄 Seamless Migration & Performance

Existing user configurations are automatically migrated at runtime. To handle the increased complexity of new categories and agents, we've implemented a **runtime fuzzing system** for model mapping, ensuring the most appropriate model is always assigned to your tasks.

---

Thank you for being part of the journey. Let's keep pushing the boundaries of what's possible.

**just.. ulw ulw** ⚡️

## [3.0.0-beta.16] - 2026-01-23

- 444fbe3 fix(delegate-task): use lowercase sisyphus-junior agent name in API calls

## [3.0.0-beta.15] - 2026-01-23

- 7ed7bf5 fix(agents): use lowercase agent names in API calls

## [3.0.0-beta.14] - 2026-01-23

## v3.0.0-beta.14

Major refactoring release that standardizes agent configuration keys to lowercase and introduces the Prometheus agent.

### New Features

- **Prometheus Agent**: Added new planning agent for strategic task decomposition
- **Agent Display Names**: New module for consistent agent name presentation
- **Platform Binary Verification**: Enhanced publish workflow with binary verification steps
- **Model Cache Warning**: Show warning toast when model cache is unavailable

### Breaking Changes (Internal)

- **Agent Keys Normalized to Lowercase**: All agent configuration keys are now lowercase throughout the codebase
  - Affected: schema, plugin, model-requirements, agents utils, prometheus-hook
  - Migration added for backward compatibility

### Bug Fixes

- **Windows Binary**: Fixed segfault by building natively (#1019)
- **Session Preservation**: Custom agent now preserved after switching (#1017)
- **Skill Tool**: Enforce agent restriction properly (#1018)
- **Look At Tool**: Conditionally register when multimodal-looker enabled (#1016)
- **Bash Tool**: Use Unix shell syntax on all platforms (#1015)
- **Atlas**: Capture stderr from git commands to prevent help text leak
- **Model Resolver**: Use first fallback entry when model cache unavailable
- **Doctor**: Improved AST-Grep NAPI detection for bunx environments
- **Doctor**: Handle file:// protocol for local dev plugin detection
- **LSP**: Add data dir to LSP server detection paths (#992)

### Documentation

- Added model configuration section to overview and quick start
- Renamed Orchestrator-Sisyphus to Atlas
- Updated multimodal-looker model name and fallback chain

---

- c2247ae refactor(agents): add prometheus agent and normalize agent key lookups
- dfc57d0 refactor(model-requirements): use lowercase agent keys
- 12c9029 refactor(plugin): use lowercase agent keys throughout
- 91060c3 refactor(agents): use lowercase config keys in utils
- 90292db refactor(prometheus-hook): use lowercase config key
- cc4deed refactor(schema): use lowercase agent config keys
- 4e42888 refactor(migration): normalize agent keys to lowercase
- 629a4d3 feat(shared): add agent display names module
- 8806ed1 feat(publish): add platform binary verification steps
- e2f8729 @veetase has signed the CLA in code-yeongyu/oh-my-opencode#985
- bee8b37 docs: add model configuration section to overview and quick start to configurations
- 37e1a06 feat(agents): add aggressive resume instructions to Atlas prompt
- fc47a7a docs: update multimodal-looker model name and fallback chain
- 9b12e2a fix(cli): update zai-coding-plan hints to include multimodal-looker
- 3062277 feat(agents): add zai-coding-plan/glm-4.6v fallback for multimodal-looker
- 7093583 fix(lsp): add data dir to LSP server detection paths (#992)
- ec61df8 Merge pull request #913 from carlory/fix-doctor
- 6312d2d Merge pull request #962 from popododo0720/fix/issues-898-919
- 810dd93 fix(skill): enforce agent restriction in createSkillTool (#1018)
- 1a901a5 fix(ci): build Windows binary natively to fix segfault (#1019)
- f8155e7 fix(session): preserve custom agent after switching (#1017)
- 39d2d44 fix(tools): conditionally register look_at when multimodal-looker enabled (#1016)
- 15c4637 fix(hooks): use unix shell syntax for bash tool on all platforms (#1015)
- 262c711 docs(agents): update AGENTS.md with current commit hash and line counts
- 599fad0 fix(atlas): capture stderr from git commands to prevent help text leak
- afbdf69 fix(model-resolver): use first fallback entry when model cache unavailable
- af9beee @Ssoon-m has signed the CLA in code-yeongyu/oh-my-opencode#1014
- 6973a75 Merge pull request #999 from l3aro/dev
- c6d6bd1 refactor(models): update agent/category fallback chains
- 57b1043 fix(agents): use resolved variant from fallback chain instead of requirement default
- 6dfe091 refactor(atlas): rewrite prompt with lean orchestrator structure
- 75158ca fix(atlas): register tool.execute.before and pass backgroundManager
- e16bbbc feat: show warning toast when model cache is not available
- ab3e622 fix: use cache file for model availability instead of SDK calls
- f434888 fix: model fallback properly falls through to system default
- 2c81c8e @l3aro has signed the CLA in code-yeongyu/oh-my-opencode#999
- 3268782 docs: rename Orchestrator-Sisyphus to Atlas
- be9d6c0 fix(doctor): improve AST-Grep NAPI detection for bunx environments
- 45fe957 fix(doctor): handle file:// protocol for local dev plugin detection

