# OpenCode Changelog


## [1.2.0] - 2026-02-14

This release includes a data migration that will execute on first run. It will migrate all flat files in data directory to a single sqlite database. Depending on how much data you have and speed of computer this can take some time.

If you have any issues with the migration the original data is not yet deleted and downgrading should work. But please open an issue so we can investigate and include sqlite in the issue title.

SDK Users

We now have a PartDelta event which sends only incremental changes to parts. This avoids sending the full content of text parts over and over when it is updated

```js
    PartDelta: BusEvent.define(
      "message.part.delta",
      z.object({
        sessionID: z.string(),
        messageID: z.string(),
        partID: z.string(),
        field: z.string(),
        delta: z.string(),
      }),
    )
```

## Core
- Revert to SQLite database implementation
- Move timeout configuration from programmatic API to CLI flag (@yanhao98)
- Update AI SDK packages and use adaptive reasoning for Claude Opus 4.6 on Vertex, Bedrock, and Anthropic
## TUI
- Prevent crash when tool inputs are malformed during opencode run (@0xK3vin)
- Add --dir option to run command (@BlankParticle)
## Desktop
- Fix Rust compilation issues in desktop application (@Brendonovich)
- Remove OPENCODE_SQLITE environment variable from desktop (@Brendonovich)
- Terminal resize handling fixed in app
- Use prompt_async endpoint to avoid timeout over VPN/tunnel (@eytans)
- Remount SDK and sync tree when server URL changes (@ysm-dev)
- Sync docs locale cookie on alias redirects (@Seungjun0906)
- Performance optimization for showing large diffs and files in desktop (@neriousy)

**Thank you to 12 community contributors:**
- @BlankParticle:
  - feat(cli): add --dir option to run command (#12443)
- @neriousy:
  - fix(desktop): performance optimization for showing large diff & files  (#13460)
- @Seungjun0906:
  - fix(web): sync docs locale cookie on alias redirects (#13109)
  - docs(ko): polish Korean phrasing in acp, agents, config, and custom-tools docs (#13446)
- @ysm-dev:
  - fix(app): remount SDK/sync tree when server URL changes (#13437)
- @Annopick:
  - docs: Fix zh-cn translation mistake in tools.mdx (#13407)
- @eytans:
  - fix(web): use prompt_async endpoint to avoid timeout over VPN/tunnel (#12749)
- @G36maid:
  - docs: add pacman installation option for Arch Linux alongside AUR (#13293)
- @yanhao98:
  - fix(test): move timeout config to CLI flag (#13494)
- @niushuai1991:
  - fix: standardize zh-CN docs character set and terminology (#13500)
- @kitlangton:
  - fix(ui): support cmd-click links in inline code (#12552)
- @0xK3vin:
  - fix: prevent opencode run crash on malformed tool inputs (#13051)
- @Brendonovich:
  - desktop: remote OPENCODE_SQLITE env (#13545)
  - desktop: fix rust


## [1.1.65] - 2026-02-13

## Core
- Revert token substitution in OPENCODE_CONFIG_CONTENT
- Ensure @-mentioning a directory uses the read tool instead of deprecated list tool
- Add tool.definition hook for plugins to modify tool description and parameters (@spoons-and-mirrors)
- Remove worktree delete functionality
- Resolve ACP hanging indefinitely in thinking state on Windows (@ASidorenkoCode)
## Desktop
- Reconnect event stream on disconnect
- Toggle all provider models in settings
- Clean up desktop loading page (@Brendonovich)
- Notification should navigate to session
- Fix prompt input behavior quirks
- Failed to create store in app
- Only show loading window if SQLite migration is necessary (@Brendonovich)

**Thank you to 3 community contributors:**
- @ASidorenkoCode:
  - fix: resolve ACP hanging indefinitely in thinking state on Windows (#13222)
- @Brendonovich:
  - desktop: only show loading window if sqlite migration is necessary
  - cleanup desktop loading page
- @spoons-and-mirrors:
  - feat(hook): add tool.definition hook for plugins to modify tool description and parameters (#4956)


## [1.1.64] - 2026-02-12

## Core
- Token substitution in OPENCODE_CONFIG_CONTENT environment variable (@ariane-emory)
- Look for recent model in fallback in CLI (@smitchaudhary)
- Baseline CPU detection fixed (@Hona)
- Windows selection behavior and manual Ctrl+C handling (@Hona)
- Terminal PTY isolation for app
## TUI
- Do not open console on error
## Desktop
- Option to turn off sound effects
- Normalize OAuth error messages
- Suggestion active state broken
- Fixed remote HTTP server connections in the app

**Thank you to 4 community contributors:**
- @amankalra172:
  - docs: update STACKIT provider documentation with typo fix (#13357)
- @Hona:
  - feat: windows selection behavior, manual ctrl+c (#13315)
  - fix: baseline CPU detection (#13371)
- @smitchaudhary:
  - fix: look for recent model in fallback in cli (#12582)
- @ariane-emory:
  - fix: token substitution in OPENCODE_CONFIG_CONTENT (#13384)


## [1.1.63] - 2026-02-12

## Core
- Improve Codex model list


## [1.1.62] - 2026-02-12

## Core
- Return image attachments from webfetch tool
- Expose tool arguments in shell hook for plugin visibility
## Desktop
- Project icons no longer unload unexpectedly
- Preserve undo history for plain-text paste in app (@gitRasheed)
- Refactor app for better SolidJS hygiene
- More defensive session context metrics handling in app

**Thank you to 2 community contributors:**
- @dtfiedler:
  - fix(docs): correct `format` attribute in `StructuredOutputs` (#13340)
- @gitRasheed:
  - fix(app): preserve undo history for plain-text paste (#13351)


## [1.1.61] - 2026-02-12

## Core
- Allow model configurations without npm/api provider details
- Tool outputs are now more LLM-friendly
## Desktop
- Add diff virtualization to improve performance for large diffs
- Display progress bar for SQLite migrations in desktop app (@Brendonovich)

**Thank you to 1 community contributor:**
- @Brendonovich:
  - desktop: sqlite migration progress bar (#13294)
  - Testing SignPath Integration (#13308)


## [1.1.60] - 2026-02-12

## Core
- Support Claude agent SDK-style structured outputs in the OpenCode SDK (@K-Mistele)
- Support custom API URL per model
- Add automatic variant generation for Venice models (@dpuyosa)
- Use Promise.all for MCP listTools calls to improve performance
- Upgrade OpenTUI to version 0.1.79
- Improve compaction check logic
- Make read tool offset 1-indexed to match line numbers and avoid confusion
- Add directory reading capability to the read tool
## TUI
- Use FFI to resolve Windows raw input and Ctrl+C handling issues (@Hona)
- Add toggle to hide session header in TUI (@kitlangton)
## Desktop
- Guard randomUUID in insecure browser contexts
- Workspace reset functionality fixed (@neriousy)

**Thank you to 6 community contributors:**
- @neriousy:
  - fix(app):workspace reset (#13170)
- @github-actions[bot]:
  - Update VOUCHED list
- @dpuyosa:
  - feat(opencode): Venice Add automatic variant generation for Venice models (#12106)
- @kitlangton:
  - feat(tui): add toggle to hide session header (#13244)
- @K-Mistele:
  - feat: support claude agent SDK-style structured outputs in the OpenCode SDK  (#8161)
- @Hona:
  - fix(win32): use ffi to get around bun raw input/ctrl+c issues (#13052)


## [1.1.59] - 2026-02-11

## Desktop
- Add translations support to the application
- I don't have access to git commands. Could you provide the full commit message or the PR description for #13166 so I can create an appropriate changelog entry? (@neriousy)
- Add more end-to-end tests for the application
- Fixed sidebar remounting issue

**Thank you to 1 community contributor:**
- @neriousy:
  - Fix/reverception (#13166)


## [1.1.58] - 2026-02-11

## TUI
- Dismiss dialogs with Ctrl+C in TUI (@kitlangton)
- Keep /share command available to copy existing share link (@kitlangton)
- Add mode-specific input placeholders to improve context-aware prompts (@kitlangton)
- Prevent home wordmark corruption in height-constrained terminals (@kitlangton)
## Desktop
- Revert WSL backend mode feature for desktop
- Notifications enabled on child sessions
- Terminal PTY buffer now properly carries over between sessions
- Terminal resize functionality fixed in app

**Thank you to 1 community contributor:**
- @kitlangton:
  - fix(tui): prevent home wordmark corruption in height-constrained terminals (#13069)
  - feat(prompt): mode-specific input placeholders (#12388)
  - fix(tui): keep /share available to copy existing link (#12532)
  - fix(tui): dismiss dialogs with ctrl+c (#12884)


## [1.1.57] - 2026-02-11

## Core
- Add additional context overflow cases and remove overcorrecting ones
- Ensure compaction is more reliable by adding reserve token buffer to provide enough room for input window compaction
- Improve /review prompt to detect behavior changes more explicitly
- Improve Amazon Bedrock check to include container credentials (@OpeOginni)
## TUI
- Default session sidebar to auto
## Desktop
- Fixed terminal copy/paste functionality
- Copy path button styles fixed in app
- Use tracing for logging in desktop application (@Brendonovich)
- Enhance Windows app resolution and UI loading states (@neriousy)
- Improve desktop app server spawn resilience
- Read Wayland preference from store in desktop application (@Brendonovich)
- Add WSL backend mode for desktop (@Brendonovich)
## SDK
- Encode non-ASCII directory paths in v1 SDK HTTP headers (@MrMushrooooom)

**Thank you to 9 community contributors:**
- @github-actions[bot]:
  - Update VOUCHED list
- @OpeOginni:
  - fix(tui): improve amazon-bedrock check to include container credentials (#13037)
- @ariane-emory:
  - docs: remove 'Migrating to 1.0' documentation section (#13076)
- @Brendonovich:
  - feat(desktop): add WSL backend mode (#12914)
  - fix(desktop): read wayland preference from store (#13081)
  - desktop: use tracing for logging (#13135)
- @webwww123:
  - fix(docs): avoid footer language selector truncation (#13124)
- @Seungjun0906:
  - docs(ko): improve translations for intro, cli, and commands (#13094)
- @neriousy:
  - feat(desktop): enhance Windows app resolution and UI loading states (#13084)
- @MrMushrooooom:
  - fix: encode non-ASCII directory paths in v1 SDK HTTP headers (#13131)
- @taroj1205:
  - fix(web): prevent language select label truncation (#13100)


## [1.1.56] - 2026-02-10

## Desktop
- Task tool rendering fixed in app
- Open apps with executables on Windows (@neriousy)
- Don't close sidebar on session change

**Thank you to 1 community contributor:**
- @neriousy:
  - fix(desktop): open apps with executables on Windows (#13022)


## [1.1.55] - 2026-02-10

## Core
- Increase test timeout to 30s to prevent failures during package installation
- Memory leak fixed in platform fetch for events
- Show helpful message when free usage limit is exceeded
## Desktop
- Disable terminal transparency


## [1.1.54] - 2026-02-10

## Core
- No changes in review pane
- Fix terminal replay in application
- Fix workspace reset issues in the app
- Resolve Homebrew upgrade requiring multiple runs (@GeneCodeSavvy)
- Publish session.error event for invalid model selection (@surma)
- Create file if it doesn't exist when writing via ACP (@BryceRyan)
- Adjust agent variant logic to check if variant is available for model instead of requiring exact match
- Add new ContextOverflowError type
- Remove obsolete Copilot model enablement instructions (@fgonzalezurriola)
- Enable thinking for all reasoning models on Alibaba Cloud (DashScope) (@AdJIa)
- Parse mid-stream OpenAI response errors to prevent infinite retries on unrecoverable errors
- Revert web input focus shortcut feature (@gigamonster256)
- Add web input focus shortcut (@ChangeHow)
- Add models.dev schema reference for model autocomplete in opencode.json (@remorses)
- Set variant in assistant messages (@shantur)
- Add skill discovery from URLs via well-known RFC
- Clean up orphaned worktree directories (@maharshi365)
- Properly encode file URLs with special characters (@yudgnahk)
- SessionPrompt.shell() now triggers loop if messages are queued (@goniz)
- Use reasoning summary auto for GPT-5 models that are not chat (@scratchmex)
- Add specific system prompt for Trinity model (@mariamjabara)
- Correct prefix selection for amazon-bedrock provider in getSmallModel (@NachoFLizaur)
- Don't rely on metadata.summary in task tool render
- Handle step-start and step-finish parts in GitHub response text extraction (@elithrar)
- Bump @gitlab/gitlab-ai-provider to 3.5.0 (@vglafirov)
- Add directory parameter to plugin client for multi-project support (@cooooooooooode)
- Correct /data API usage and data format for importing share URLs (@yuvrajvirk)
- Parallelize skill downloads for faster loading in TUI
- Add skill discovery from URLs via well-known RFC
- Handle dollar sign character with file pattern in configuration (@hstove)
## TUI
- Clean up dialog-model.tsx per code review
- Revert addition of version to session header and status dialog
- Revert showing connected providers in /connect dialog
- Use sender color for queued messages in TUI (@mcostasilva)
- Revert footer restoration in session view
- Add Claude Code-style --fork flag to duplicate sessions before continuing (@ariane-emory)
- Restore footer to session view (@ariane-emory)
- Increase skill dialog width
- Improve skills dialog readability (@kynnyhsap)
## Desktop
- Back to platform fetch for now
- Include basic authentication in app
- Fixed global event default fetch behavior in app
- Fixed memory leak in event fetch operation
- Don't dispose instance after reset workspace
- Based on the commit message "fix(app): regressions" without access to the actual changes, I can only provide a generic summary:

Fix regressions in the app
- Use agent configured variant in app
- Persist defensiveness in app
- Add redo and undo end-to-end test (@neriousy)
- Use absolute paths for sidebar session navigation (@riftzen-bit)
- New session in workspace now correctly uses the selected workspace
- Add Cmd+[/] keybinds for session history navigation (@kitlangton)
- Correct module name for linux_display in main.rs (@Hona)
- Set maximum widths in app
- Incorrect workspace on new session
- Update tab file contents on change
- Polish Open in icon treatment
- Add fallback for when crypto.randomUUID is unavailable
- Allow creating sessions on touch devices (@kitlangton)
- Add native Wayland toggle on Linux desktop (@IsraelAraujo70)
- Include sandboxes in project unseen message and error notifications (@Brendonovich)
- Persist current sidecar URL in state when isSidecar prop is true (@OpeOginni)
- Track current sidecar URL in desktop application (@Brendonovich)
- Exclude devtools from production builds (@sneycampos)
- Add isSidecar prop to AppInterface and persist sidecar server URLs (@OpeOginni)
- Localize "close tab" in command palette (@alexyaroshuk)
- Improve workspace header truncation and item interaction (@kitlangton)
- Add default clipboard copy affordance to TextField component (@kitlangton)
- Fix stale context in prompt input
- Tighten slash command autocomplete matching (@kitlangton)
- Display toast notification when session is missing on prompt submit (@DNGriffin)
- Add native clipboard image paste and fix text paste in desktop app (@invarrow)
- Respect terminal toggle keybind when terminal is focused (@ryanmiville)
- Keep /share available to copy existing link (@kitlangton)
- Disable 3 Safari prompt-input annoyances (@DNGriffin)
- Add drag-and-drop support for @mentioning files in the app (@DNGriffin)
- Handle Windows paths in frontend file URL encoding (@yudgnahk)
- Move workspace New session button into header (@kitlangton)
- Toggle file tree and review panel with improved UX (@ProdigyRahul)
- Allow agent select to use full width on Windows (@abdiths)
- Keep startup script field scrollable in edit project dialog (@itskritix)
- Fix terminal replay issues in app
- Added macOS support for displaying only installed editors and added Sublime Text editor (@OpeOginni)
- Remove extra error page and use default error boundary
- Add loading window and restructure Rust desktop code (@Brendonovich)
- Hide 'open in app' button on narrow viewports
- Update server removal logic to clear default server URL if removed (@OpeOginni)
- Display session last updated time in command palette search (@alexyaroshuk)
- Add Windows File Explorer icon for session header (@maharshi365)
- Support desktop titlebar double-click maximize (@crob19)
- Add keyboard accelerators to menu items (@Brendonovich)
- Add more basic menu bar items to desktop application (@Brendonovich)
- Always show project menu button on mobile for accessibility (@DNGriffin)
- Maximize main window by default (@Brendonovich)

**Thank you to 44 community contributors:**
- @kynnyhsap:
  - fix(opencode): improve skills dialog readability (#12356)
- @hstove:
  - fix(config): handle $ character with {file:} pattern (#12390)
- @AksharP5:
  - feat(tui): highlight esc label on hover in dialog (#12383)
- @Brendonovich:
  - desktop: maximize main window by default (#12433)
  - desktop: add more basic menu bar items
  - desktop: add key accelerators to menu itms
  - desktop: add loading window and restructure rust (#12176)
  - desktop: track currentSidecarUrl
  - app: include sandboxes in project unseen/error notifs
- @DNGriffin:
  - fix(app): always show project menu button for mobile a11y  (#11258)
  - feat(app): drag-n-drop to @mention file (#12569)
  - fix(app): disable 3 safari prompt-input annoyances (#12558)
  - fix(app): Toast when session is missing on prompt-submit (#12654)
- @crob19:
  - fix(desktop): support desktop titlebar double-click maximize (#12459)
- @maharshi365:
  - fix(ui): add Windows File Explorer icon for session header (#12386)
  - fix(opencode): cleanup orphaned worktree directories (#12399)
- @alexyaroshuk:
  - feat(app): session last updated time display in command pallete's search (#12376)
  - fix(app): localize "close tab" in command pallete (#12756)
- @OpeOginni:
  - fix(desktop): update server removal logic to clear default server URL if removed (#12372)
  - feat(desktop): added Macos support for displaying only installed editors & added sublime text editor (#12501)
  - fix(docs-windows-wsl): update caution note for server security (#12467)
  - feat(desktop): add isSidecar prop to AppInterface and logic to persist sidecar server urls (#12366)
  - feat(desktop): persist currentSidecarUrl in state when isSidecar prop is true (#12792)
- @yuvrajvirk:
  - fix: correct /data API usage and data format for importing share URLs (#7381)
- @cooooooooooode:
  - fix: add directory parameter to plugin client for multi-project support (#11344)
- @vglafirov:
  - chore(deps): bump @gitlab/gitlab-ai-provider to 3.5.0 (#12496)
- @elithrar:
  - fix(github): handle step-start/step-finish parts in extractResponseText (#12470)
- @ariane-emory:
  - feat(tui): restore footer to session view (#12245)
  - feat(tui): add Claude Code-style --fork flag to duplicate sessions before continuing (resolves #11137) (#11340)
  - docs(cli): add documentation for --fork flag (#12561)
- @NachoFLizaur:
  - fix(opencode): correct prefix selection for amazon-bedrock provider in getSmallModel (#12281)
- @mariamjabara:
  - feat: add specific system prompt for Trinity model (#12144)
- @scratchmex:
  - feat(opencode): use reasoning summary auto for gpt-5 models that are not chat (#12502)
- @dbpolito:
  - feat(desktop): Session Review Images (#12360)
- @goniz:
  - fix(opencode): SessionPrompt.shell() now triggers loop if messages are queued (#10987)
- @itskritix:
  - fix(app): keep startup script field scrollable in edit project dialog (#12431)
- @abdiths:
  - fix(desktop): allow agent select to use full width on windows (#12428)
- @yudgnahk:
  - fix: properly encode file URLs with special characters (#12424)
  - fix(app): handle Windows paths in frontend file URL encoding (#12601)
- @shantur:
  - feat(core): Set variant in assistant messages too (#12531)
- @remorses:
  - feat: add models.dev schema ref for model autocomplete in opencode.json (#12528)
- @ProdigyRahul:
  - fix(app): toggle file tree and review panel better ux (#12481)
- @kitlangton:
  - fix(app): move workspace New session into header (#12624)
  - fix(web): keep /share available to copy existing link (#12533)
  - refine(app): tighten slash autocomplete matching (#12647)
  - ui: default TextField copy affordance to clipboard (#12714)
  - fix(layout): improve workspace header truncation and item interaction (#12655)
  - fix(app): allow creating sessions on touch devices (#12765)
  - feat(app): add Cmd+[/] keybinds for session history navigation (#12880)
- @ChangeHow:
  - feat(app): add web input focus shortcut (#12493)
- @gigamonster256:
  - fix: revert "feat(app): add web input focus shortcut (#12493)" (#12639)
  - feat(nix): disable build time models.dev fetching (#12644)
  - feat(nix): expose overlay for downstream use (#12643)
- @ryanmiville:
  - fix(app): respect terminal toggle keybind when terminal is focused (#12635)
- @invarrow:
  - fix(desktop): add native clipboard image paste and fix text paste (#12682)
- @jerome-benoit:
  - refactor(nix): use native Bun APIs and propagate errors (#12694)
  - fix(nix): watch scripts in nix-hashes workflow (#12818)
  - fix(nix): restore install script in fileset for desktop build (#12842)
- @AdJIa:
  - fix: enable thinking for all reasoning models on alibaba-cn (DashScope) (#12772)
- @fgonzalezurriola:
  - fix(provider): remove obsolete copilot model enablement instructions (#12739)
- @sneycampos:
  - feat: exclude devtools from production builds (#12290)
- @IsraelAraujo70:
  - feat(desktop): add native Wayland toggle on Linux (#11971)
- @jcampuza:
  - fix(app): make keyboard focus visible in settings (#12612)
- @BryceRyan:
  - fix(opencode): ACP File write should create the file if it doesn't exist (#12854)
- @Hona:
  - fix(desktop): correct module name for linux_display in main.rs (#12862)
- @surma:
  - fix: publish session.error event for invalid model selection (#8451)
- @mcostasilva:
  - fix(tui): use sender color for queued messages (#12832)
- @github-actions[bot]:
  - Update VOUCHED list
- @GeneCodeSavvy:
  - fix: resolve homebrew upgrade requiring multiple runs (#5375) (#10118)
- @riftzen-bit:
  - fix: use absolute paths for sidebar session navigation (#12898)
- @neriousy:
  - test(e2e): redo & undo test (#12974)


## [1.1.53] - 2026-02-05

## Core
- Load user plugins after built-in plugins
- Fix unhandled errors when aborting with queued messages
- User plugins override built-in plugins for the same provider (@rmk40)
- Move Codex 5.3 model definition to plugin to avoid showing unsupported model to other users
- Add session usage tracking to ACP (@SteffenDE)
- Update transforms for GPT-5.3
## TUI
- Allow mouse escape via "esc" labels in dialogs (@AksharP5)
## Desktop
- Make close comment button visible in prompt input (@alexyaroshuk)
- Hide prompt input when there are permissions requests or questions
- More terminal stability fixes
- Modified file color contrast in app for better visibility
- Add button to open files in external applications
- Allow toggling file tree closed independently
- Stop showing SessionSkeleton on new workspace (@dbpolito)
- Set workspace name earlier to improve creation and deletion (@dbpolito)

**Thank you to 7 community contributors:**
- @SteffenDE:
  - feat(acp): add session usage (#12299)
- @dbpolito:
  - feat(desktop): Set Workspace Name Earlier to Improve Creation / Deletion (#12213)
  - feat(desktop): Stop Showing SessionSkeleton on New Workspace (#12209)
- @alexyaroshuk:
  - fix(app): make close comment button visible in prompt input  (#12349)
- @edoedac0:
  - docs: add Bosnian README translation (#12341)
- @ariane-emory:
  - docs: websearch tool (#12359)
- @rmk40:
  - fix(plugin): user plugins override built-in plugins for same provider (#12361)
- @AksharP5:
  - fix(tui): allow mouse escape via "esc" labels in dialogs  (#11421)


## [1.1.52] - 2026-02-05

## Core
- Enable Claude 3.5 Sonnet (new) model support
- Silently ignore proxy command failures to prevent config initialization crashes
- Ensure GitHub Copilot plugin properly sets headers when used in clients other than TUI
- Bundle GitLab auth plugin directly instead of dynamic install
- Fix plugin installation to use direct package.json manipulation instead of bun add
- Fix image reading with OpenAI-compatible providers like Kimi K2.5 (@zhming0)
- Downgrade xai ai-sdk package due to errors
- Revert model autocomplete feature using models.dev schema reference
- Add models.dev schema reference for model autocomplete in opencode.json (@remorses)
- Adjust task tool description and input to reduce tool call failures with GPT models
- Wait for dependencies before loading custom tools and plugins
- Allow the function to hide or show thinking blocks to be bound to a key (@ariane-emory)
- Skip dependency installation in read-only configuration directories (@shantur)
- Ensure Kimi for Coding plan has thinking enabled by default for k2p5 (@monotykamary)
- Fixed Cloudflare Workers AI provider
- Prevent random hangs in plugin installs when using HTTP proxy by adding --no-cache flag
- Session errors when attachment file not found are now handled gracefully
- Support remote server connections in terminal and fix GLIBC compatibility (@lucas-jo)
## TUI
- Add running spinner to bash tool in TUI (@goniz)
- Add hover states to question tool tabs (@maharshi365)
## Desktop
- File changes not always available in app
- File tree kept in sync with filesystem changes
- Add Bosnian locale (@edoedac0)
- Fix terminal URL handling issues
- Remove extra horizontal padding around prompt input on mobile (@Brendonovich)
- Refresh workspace sessions when switching projects (@neriousy)
- Fixed terminal URL handling in the application
- Fix terminal end-of-line handling issues
- Refresh file contents when changing workspaces to prevent stale data (@ParkerSm1th)
- Derive terminal WebSocket URL from browser origin instead of hardcoded localhost (@0xdsqr)
- Last turn changes rendered in review pane
- Safety triangle for sidebar hover to prevent menu from closing
- Clear comments on prompt submission
- Fix e2e test action in app
- Terminal hyperlink clicks now work correctly
- Fix dated e2e tests in app
- Don't show scroll-to-bottom button unnecessarily
- File tree not staying in sync across projects/sessions
- Move session options to the session page
- Add session options to app
- Opened tabs follow created session
- Removed compression from RPM bundle to save 15 minutes in CI (@goniz)

**Thank you to 13 community contributors:**
- @lucas-jo:
  - fix(terminal): support remote server connections and fix GLIBC compatibility (#11906)
- @goniz:
  - fix(desktop): removed compression from rpm bundle to save 15m in CI (#12097)
  - feat(tui): add running spinner to bash tool in TUI (#12317)
- @monotykamary:
  - fix: ensure kimi-for-coding plan has thinking on by default for k2p5 (#12147)
- @0xdsqr:
  - fix(app): derive terminal WebSocket URL from browser origin instead o… (#12178)
- @ParkerSm1th:
  - fix(desktop): Refresh file contents when changing workspaces to not have stale contents (#11728)
- @shantur:
  - fix(core): skip dependency install in read-only config dirs (#12128)
- @maharshi365:
  - fix(tui): add hover states to question tool tabs (#12203)
- @ariane-emory:
  - feat: Allow the function to hide or show thinking blocks to be bound to a key (resolves #12168) (#12171)
- @neriousy:
  - fix(app): refresh workspace sessions on project switch (#12189)
- @remorses:
  - feat: add models.dev schema ref for model autocomplete in opencode.json (#12112)
- @zhming0:
  - fix(opencode): Fixes image reading with OpenAI-compatible providers like Kimi K2.5. (#11323)
- @Brendonovich:
  - app: remove extra x padding around prompt input on mobile
- @edoedac0:
  - feat(i18n): add Bosnian locale (#12283)


## [1.1.51] - 2026-02-04

## Core
- Revert change that caused headers to be double merged if provider was authenticated in multiple places
- Document the built-in agents
- Prevent double-prefixing of Bedrock cross-region inference models (@sergical)
- Prioritize OPENCODE_CONFIG_DIR for AGENTS.md (@lgladysz)
## TUI
- Restore direct OSC52 support
## Desktop
- Tighten up session padding-top for mobile (@DNGriffin)

**Thank you to 4 community contributors:**
- @lgladysz:
  - fix: prioritize OPENCODE_CONFIG_DIR for AGENTS.md (#11536)
- @DNGriffin:
  - fix(app): tighten up session padding-top for mobile (#11247)
- @sergical:
  - fix: prevent double-prefixing of Bedrock cross-region inference models (#12056)
- @schaoss:
  - docs: add agent-compatible paths to skills documentation (#12067)


## [1.1.50] - 2026-02-04

## Core
- Prevent memory leaks from AbortController closures (@MaxLeiter)
- Revert addition of Trinity model system prompt support
- Add Trinity model system prompt support (@mariamjabara)
- Add shell.env hook for manipulating environment in tools and shell (@tylergannon)
- Use official ai-gateway-provider package for Cloudflare AI Gateway (@elithrar)
- Allow theme colors in agent customization (@IdrisGit)
- Add support for reading skills from .agents/skills directories
- Provider headers from config not applied to fetch requests (@cloudyan)
- Ensure MCP tools are sanitized
- Add .slnx to C#/F# LSP root detection (@workedbeforepush)
- Improve skills system with better prompting, fix permission requests after skill invocation, and ensure agents can locate scripts and resources
- Exclude k2p5 from reasoning variants (@neavo)
- Handle nested array items for Gemini schema validation (@mugnimaestra)
- Plugins are always reinstalled (@neriousy)
- Strip properties and required fields from non-object types in Gemini schema (@ChickenBreast-ky)
- Make CLI run command non-interactive
## TUI
- Add --thinking flag to show reasoning blocks in run command
- Always fall back to native clipboard after OSC52 (@MartinWie)
## Desktop
- Faster end-to-end tests (@neriousy)
- Update command palette placeholder text
- Model selector truncating too soon
- Improve spacing in application UI
- Allow empty prompt with review comments in desktop (@dbpolito)
- Fixed terminal serialization bug in app
- Don't force mount tooltips in the app
- Restore previously opened session tabs on app restart (@ProdigyRahul)
- Edit project dialog icon now shows on hover (@ProdigyRahul)
- Move session search to command palette
- Fix custom providers overflow in app (@DNGriffin)

**Thank you to 18 community contributors:**
- @ChickenBreast-ky:
  - fix(provider): strip properties/required from non-object types in Gemini schema (#11888)
- @neriousy:
  - fix(core): plugins are always reinstalled  (#9675)
  - refactor(e2e): faster tests (#12021)
- @DNGriffin:
  - fix(app):  custom providers overflow (#11252)
- @ProdigyRahul:
  - fix(app): edit project dialog icon on hover (#11921)
  - fix(app): session tabs to open the previous opened (#11914)
- @luiz290788:
  - docs: add --mdns-domain flag documentation (#11933)
- @dbpolito:
  - feat(desktop): Allow empty prompt with review comments (#11953)
- @mugnimaestra:
  - fix: handle nested array items for Gemini schema validation (#11952)
- @neavo:
  - fix: exclude k2p5 from reasoning variants (#11918)
- @workedbeforepush:
  - feat: Add .slnx to C#/F# LSP root detection (#11928)
- @cloudyan:
  - fix: provider headers from config not applied to fetch requests (#11788)
- @MartinWie:
  - fix: always fall back to native clipboard after OSC52 (#11994)
- @IdrisGit:
  - docs: add missing environmental flags to the list (#11146)
  - feat(tui): allow theme colors in agent customization (#11444)
- @elithrar:
  - fix(opencode): use official ai-gateway-provider package for Cloudflare AI Gateway (#12014)
- @tylergannon:
  - feat(plugin): add shell.env hook for manipulating environment in tools and shell (#12012)
- @tlinhart:
  - docs: fix logging example for plugin (#11989)
- @Evren-os:
  - docs: fix grammar and formatting in README (#11985)
- @mariamjabara:
  - feat: add Trinity model system prompt support (#12025)
- @MaxLeiter:
  - fix: prevent memory leaks from AbortController closures (#12024)


## [1.1.49] - 2026-02-03

## Core
- Revert pull request that was mistakenly merged
- Add --mdns-domain flag to customize mDNS hostname (@luiz290788)
- Added and deleted file status now correctly calculated in app
- Add User-Agent header for GitLab AI Gateway requests (@vglafirov)
- Add Ormolu code formatter for Haskell (@mimi1vx)
- Use OpenTUI OSC52 clipboard implementation
- Convert system message content to string for Copilot provider (@jogi47)
- Give OPENCODE_CONFIG_CONTENT proper priority for setting config based on docs (@OpeOginni)
- Fixed session title generation with OpenAI models (@oomathias)
- Simplify directory tree output for prompts
- Fix task status to show current tool state from message store
- Allow starting new sessions after errors by fixing stuck session status
- Adjust resolve parts to properly order tool calls when messages contain multiple @ references
- Hide badge for builtin slash commands
- Add workspace tests to the app (@neriousy)
- Send custom agent prompts as developer messages instead of user messages when using Codex subscriptions
- Fixed variant logic for Anthropic models through OpenAI compatibility endpoint
- Add prompt caching support for Claude Opus on AWS Bedrock (@rgodha24)
- Scope agent variant to model (@neavo)
- Prevent duplicate AGENTS.md injection when reading instruction files (@code-yeongyu)
- OpenCode no longer hangs when using client.app.log() during initialization (@desmondsow)
- Remove outer backtick wrapper in session transcript tool formatting (@zerone0x)
- Allow user plugins to override built-in auth plugins (@JosXa)
- Binary file handling in file view (@alexyaroshuk)
- Ensure switching Anthropic models mid-conversation works without errors and fix reasoning opaque not being picked up for Gemini models
- Fix issue where folders and files starting with "." could not be mentioned with @
- Show actual retry error message instead of generic error message
- Use process.env directly for runtime environment mutations in provider (@jerome-benoit)
- Add reasoning variants support for SAP AI Core (@jerome-benoit)
- Add UTF-8 encoding defaults for Windows PTY (@01luyicheng)
## TUI
- Respect terminal transparency in system theme (@pablopunk)
- Truncate session title in exit banner to prevent display overflow
- Show exit message banner in TUI
- Add spinner animation for Task tool
- Correct pluralization of match count in grep and glob tools (@adamjhf)
- Remove extra padding between search and results in dialog-select
- Add UI for skill tool in session view
- Conditionally render bash tool output in TUI
- Add skill dialog for selecting and inserting skills
- Enable password authentication for remote session attachment
- Fix documentation issues (@lailoo)
- Revert skill slash commands feature
- Add skill slash commands to the app
## Desktop
- Fix prompt input overflow issue in app (@neriousy)
- Sidebar losing projects on collapse has been fixed
- Add workspace toggle command to command palette and prompt input (@alexyaroshuk)
- Search through sessions
- Standardize icon sizes in the application
- Navigate to last project on open
- User messages not rendering consistently
- Add project context menu on right-click
- Open project search in app (@neriousy)
- Add tab close keybind to app (@ProdigyRahul)
- Enhance responsive design with additional breakpoints for larger screen layout adjustments (@OpeOginni)
- Add keyboard shortcuts for navigating between unread sessions (@Brendonovich)
- Fix Rust build and bindings formatting in desktop application (@Brendonovich)
- Remove unnecessary setTimeout in desktop app (@Brendonovich)
- Throttle window state persistence in desktop application (@Brendonovich)
- Integrate tauri-specta for desktop application (@Brendonovich)
- Keep macOS titlebar stable under zoom (@Brendonovich)
- Kill zombie server process on startup timeout (@heyitsmohdd)
- Show skill and MCP badges for slash commands
- Use static language names in Thai localization (@alexyaroshuk)
- Add tests for general settings, shortcuts, providers and status popover (@neriousy)
- Fixed session header 'share' button to hug content (@alexyaroshuk)

**Thank you to 29 community contributors:**
- @alexyaroshuk:
  - fix(app): session header 'share' button to hug content (#11371)
  - fix(app): use static language names in Thai localization (#11496)
  - fix(app): binary file handling in file view (#11312)
  - feat(app): add workspace toggle command to command palette and prompt input (#11810)
- @01luyicheng:
  - fix(pty): Add UTF-8 encoding defaults for Windows PTY (#11459)
  - docs: improve zh-TW punctuation to match Taiwan usage (#11574) (#11589)
- @jerome-benoit:
  - feat(opencode): add reasoning variants support for SAP AI Core (#8753)
  - fix(nix): restore native runners for darwin hash computation (#11495)
  - fix(provider): use process.env directly for runtime env mutations (#11482)
  - fix(ci): portable hash parsing in nix-hashes workflow (#11533)
- @lailoo:
  - docs: fix documentation issues (#11435)
- @neriousy:
  - test(app): general settings, shortcuts, providers and status popover  (#11517)
  - fix(app): rendering question tool when the step are collapsed (#11539)
  - fix(app): show retry status only on active turn (#11543)
  - docs: prefer wsl over native windows stuff (#11637)
  - test(app): workspace tests (#11659)
  - fix(app): open project search (#11783)
  - fix(app): prompt input overflow issue (#11840)
- @adamjhf:
  - fix: correct pluralization of match count in grep and glob tools (#11565)
- @AlperKartkaya:
  - docs: add Turkish README translation (#11524)
- @JosXa:
  - fix: allow user plugins to override built-in auth plugins (#11058)
- @AxelMrak:
  - fix(ecosystem): fix link Daytona  (#11621)
- @zerone0x:
  - fix(tui): remove outer backtick wrapper in session transcript tool formatting (#11566)
- @desmondsow:
  - fix: opencode hanging when using client.app.log() during initialization (#11642)
- @code-yeongyu:
  - fix: prevent duplicate AGENTS.md injection when reading instruction files (#11581)
- @neavo:
  - fix(opencode): scope agent variant to model (#11410)
- @gigamonster256:
  - fix(desktop): nix - add missing dep (#11656)
- @rgodha24:
  - fix: prompt caching for opus on bedrock (#11664)
- @sum2it:
  - docs (web): Update incorrect Kimi model name in zen.mdx (#11677)
- @aaroniker:
  - feat(ui): Select, dropdown, popover styles & transitions (#11675)
  - feat(ui): Smooth fading out on scroll, style fixes (#11683)
- @oomathias:
  - fix: session title generation with OpenAI models. (#11678)
- @OpeOginni:
  - fix(opencode): give OPENCODE_CONFIG_CONTENT proper priority for setting config based on docs (#11670)
  - fix(desktop): added inverted svg for steps expanded for nice UX (#10462)
  - feat(app): enhance responsive design with additional breakpoints for larger screen layout adjustments (#10459)
- @jogi47:
  - fix: convert system message content to string for Copilot provider (#11600)
- @heyitsmohdd:
  - fix(desktop): kill zombie server process on startup timeout (#11602)
- @Brendonovich:
  - fix(desktop): keep mac titlebar stable under zoom (#11747)
  - chore(desktop): integrate tauri-specta (#11740)
  - fix(desktop): throttle window state persistence (#11746)
  - fix(desktop): remove unnecessary setTimeout
  - desktop: fix rust build + bindings formatting
  - feat(app): unread session navigation keybinds (#11750)
- @ldelelis:
  - fix(ui): adjusts alignment of elements to prevent incomplete scroll (#11649)
- @sam-huckaby:
  - Fix(app): the Vesper theme's light mode (#9892)
- @mimi1vx:
  - feat(opencode): ormolu code formatter for haskell (#10274)
- @ProdigyRahul:
  - feat(app): add tab close keybind (#11780)
- @vglafirov:
  - feat(provider): add User-Agent header for GitLab AI Gateway requests (#11818)
- @pablopunk:
  - fix(tui): respect terminal transparency in system theme (#8467)
- @luiz290788:
  - feat(server): add --mdns-domain flag to customize mDNS hostname (#11796)


## [1.1.48] - 2026-01-31

## Core
- Sync changes
- Allow specifying custom models file path via OPENCODE_MODELS_PATH environment variable
- Ensure models configuration is not empty before loading
- Make skills invokable as slash commands in the TUI
- Don't follow symbolic links by default in grep and ripgrep operations
- Prevent parallel test runs from contaminating environment variables
- Ensure Mistral ordering fixes also apply to Devstral
- Add Copilot-specific provider to properly handle reasoning tokens (@SteffenDE)
- Respect OPENCODE_MODELS_URL environment variable in build process (@bbartels)
- Use snake_case for thinking parameter with OpenAI-compatible APIs (@Chesars)
- Bump AI SDK packages
- Ensure ask question tool isn't included when using acp
- Handle redirected statement treesitter node in bash permissions (@pschiel)
- Remove special case handling for Google Vertex Anthropic provider in response generation (@MichaelYochpaz)
- Exclude chat models from textVerbosity setting
## Desktop
- Revert transitions, spacing, scroll fade, and prompt area updates
- Add session actions tests (@neriousy)
- Refactored tests and added project tests (@neriousy)

**Thank you to 7 community contributors:**
- @neriousy:
  - refactor(app): refactored tests + added project tests (#11349)
  - test(app): session actions (#11386)
- @MichaelYochpaz:
  - refactor(provider): remove google-vertex-anthropic special case in ge… (#10743)
- @pschiel:
  - fix: handle redirected_statement treesitter node in bash permissions (#6737)
- @IdrisGit:
  - docs: update agents options section to include color and top_p options (#11355)
- @Chesars:
  - fix(provider): use snake_case for thinking param with OpenAI-compatible APIs (#10109)
- @bbartels:
  - feat(build): respect OPENCODE_MODELS_URL env var (#11384)
- @SteffenDE:
  - feat(opencode): add copilot specific provider to properly handle copilot reasoning tokens (#8900)


## [1.1.47] - 2026-01-30

## Core
- I need to see the actual commit message to summarize it. Could you please provide the commit message you'd like me to summarize for the changelog entry?


## [1.1.46] - 2026-01-30

## Core
- Remove unused experimental keys from TUI (@IdrisGit)
- Add continuous integration configuration
- Remove AI SDK middleware that was preventing think blocks from being sent back as assistant message content
## Desktop
- Change language test in app (@neriousy)
- Add transitions, spacing improvements, scroll fade effects, and prompt area updates (@aaroniker)

**Thank you to 3 community contributors:**
- @aaroniker:
  - feat: Transitions, spacing, scroll fade, prompt area update (#11168)
- @neriousy:
  - test(app): change language test (#11295)
- @IdrisGit:
  - chore(tui): remove unused experimental keys (#11195)


## [1.1.45] - 2026-01-30

## Desktop
- Free model layout improvements in app


## [1.1.44] - 2026-01-30

No notable changes


## [1.1.43] - 2026-01-30

No notable changes


## [1.1.42] - 2026-01-29

## Core
- Revert to Anthropic completions endpoint to avoid rate limiting issues with copilot
- Fix frontmatter adding newlines causing invalid model IDs
- Ensure that Kimi doesn't have fake variants available
- Add sequential numbering for forked session titles (@ariane-emory)
## TUI
- Add additional timeout race condition guards
- Guard destroyed input field in timeout callback
- Include cache tokens in CLI statistics (@bold84)

**Thank you to 2 community contributors:**
- @bold84:
  - feat(cli): include cache tokens in stats (#10582)
- @ariane-emory:
  - feat: Sequential numbering for forked session titles (Issue #10105) (#10321)


## [1.1.41] - 2026-01-29

## Core
- Ensure variants for Copilot models work with maxTokens being set
- Fixed maxOutputTokens being accidentally hardcoded to undefined which caused kimi-k2.5 issues on some inference providers (@ideallove)
- Include provider ID in SDK cache key to prevent cache collisions (@saba-ch)
- Allow media-src data: URL for small audio files in Content Security Policy (@tanapok)
- Update experimental environment variables in CLI documentation (@bbabou)
- Add `ctx.abort` to grep tool
- Add AbortSignal support to Ripgrep.files() and GlobTool (@goniz)
## Desktop
- Make settings more responsive for mobile and small web/desktop (@DNGriffin)
- Fixed type errors in app package (@Brendonovich)
- Auto scroll to file tabs on open and enable mouse wheel scrolling (@alexyaroshuk)
- Remove duplicate keys causing TypeScript failures (@eXamadeus)
- Normalize Chinese punctuation for Chinese UI (@MaxMiksa)
- Fill missing Chinese translation keys to avoid English fallback (@MaxMiksa)
- Fix alignment and padding in dialogs (@alexyaroshuk)

**Thank you to 12 community contributors:**
- @R44VC0RP:
  - fix(script): remove highlights template from release notes (#11052)
- @zerone0x:
  - fix(ui): allow KaTeX inline math to be followed by punctuation (#11033)
- @alexyaroshuk:
  - fix(app): alignment and padding in dialogs (#10866)
  - fix(app): file tabs - auto scroll on open & scroll via mouse wheel (#11070)
- @MaxMiksa:
  - fix(app): fill missing zh keys to avoid English fallback (#10841)
  - fix(opencode): normalize zh punctuation for Chinese UI (#10842)
  - fix(ui): improve zh duration display formatting (#10844)
- @goniz:
  - fix(opencode): add `AbortSignal` support to `Ripgrep.files()` and `GlobTool` (#10833)
- @eXamadeus:
  - fix(typescript errors): remove duplicate keys causing typescript failures (#11071)
- @Brendonovich:
  - fix(app): types
- @bbabou:
  - docs: update experimental environment variables in CLI docs (#11030)
- @DNGriffin:
  - fix(app): make settings more responsive for mobile and small web/desktop (#10775)
- @tanapok:
  - fix(opencode): allow media-src data: URL for small audio files (#11082)
- @saba-ch:
  - fix(provider): include providerID in SDK cache key (#11020)
- @ideallove:
  - fix: maxOutputTokens was accidentally hardcoded to undefined  (#10995)


## [1.1.40] - 2026-01-28

## Core
- Add SubtaskPart with metadata reference (@YangTianz)
- Add global configuration support to app
- Global configuration updates in app package
- Bump plugins
## TUI
- Add streaming prop to markdown element (@remorses)
## Desktop
- Close review pane when pressing escape key
- Enable ctrl+n and ctrl+p for popover navigation in desktop app (@sairajchouhan)
- Add Thai locale support (@natt-v)
- Add custom provider support to app

**Thank you to 4 community contributors:**
- @natt-v:
  - feat(i18n): add th locale support (#10809)
- @sairajchouhan:
  - fix(desktop): enable ctrl+n and ctrl+p for popover navigation (#10777)
- @YangTianz:
  - fix: add SubtaskPart with metadata reference (#10990)
- @remorses:
  - fix(markdown): Add streaming prop to markdown element (#11025)


## [1.1.39] - 2026-01-28

## Core
- Ensure Copilot plugin properly sets headers for new messages API


## [1.1.38] - 2026-01-28

## Core
- Prevent AGENTS.md from being loaded multiple times during parallel tool execution
- Bump plugin version
- Ensure unsubscribe from PartUpdated is always called in TaskTool (@goniz)
- Restore brand integrity of CLI wordmark (@mynameistito)
- Add experimental OpenTUI markdown component to app (@remorses)

**Thank you to 4 community contributors:**
- @remorses:
  - feat(app): use opentui markdown component behind experimental flag (#10900)
- @jamesmurdza:
  - docs: add Daytona OpenCode plugin to ecosystem (#10917)
- @mynameistito:
  - fix(cli): restore brand integrity of CLI wordmark (#10912)
- @goniz:
  - fix(opencode): ensure unsub(PartUpdated) is always called in TaskTool (#9992)


## [1.1.37] - 2026-01-28

## Core
- Support headless authentication for ChatGPT/Codex (@rgodha24)
- Add recommended topP and temperature settings for Kimi K2.5 model
- Adjust retry check to be more defensive
- Handle Venice cache creation tokens (@dpuyosa)
- Add worktree to plugin tool context
- Expose Instance.directory to custom tools
- Use Instance.directory instead of process.cwd() in read tool
- Fix reactive file tree to properly update when files change
- Attach Anthropic beta headers when using Messages API for Copilot
- Add retry logic to handle certain provider problems
- Ensure OpenAI 404 errors are retried (@tim-smart)
- Use Anthropic-compatible messages API for Anthropic models through Copilot
- Upgrade OpenTUI to v0.1.75
- Dynamically resolve AGENTS.md files from subdirectories as agent explores them
- Add agent description to OpenCode (@SteffenDE)
- Fix query selector handling of non-Latin characters
- Await SessionRevert.cleanup for shell to prevent race conditions (@noamzbr)
- Don't override source in custom provider loaders
- Add provider settings to app
- Run start command after reset in app
- Remove log statement
## TUI
- Handle 4-5 digit codes in copy logic
- Make diff wrapping toggle always available in command list and fix type error (@ariane-emory)
- Add visual feedback for diff wrap and conceal toggles (@IdrisGit)
- Adjust TUI syncing logic to prevent agents from being undefined or missing
- Remove broken app.tsx command option
- Move animations toggle to global System category (@ariane-emory)
## Desktop
- Reintroduce review tab in app
- Auto-scroll to keep relevant content in view
- Add 'connect provider' button to the manage models dialog (@alexyaroshuk)
- Fix terminal corruption issue in app
- File tree not always loading in app
- Fix outdated e2e test in app package
- Do not auto-navigate to last project on app load
- Add Tauri localization support to desktop application
- Add internationalization support for Tauri desktop application
- Better memory management in app
- Don't connect to localhost through VPN
- Show 5 highlights in app
- Highlight selected change in the app
- Set filetree padding to 6px
- Align file tree change styling
- Delay navigation tooltips
- Adjust titlebar left spacing
- Shorten navigation tooltips
- Add filetree tooltips with diff labels
- Color file tree change dots by diff kind
- Improved app layout
- Fix session diffs not always loading in app
- New end-to-end smoke tests for app
- Add translations to the app
- Update settings in general settings
- Swallow file search errors in app
- Fix tooltips causing getComputedStyle errors in model select
- Clean up Tailwind CSS versus pure CSS usage in app
- Navigate to tabs when opening file in app
- Open markdown links in external browser
- Shared terminal ghostty-web instance for better performance
- Cleanup connect provider timers
- Don't keep parts in memory
- Don't show session skeleton after workspace reset
- Add max-width to tabs with text truncation
- Use smaller close icon on tabs to match comment cards
- Only show left border on plus button when sticky
- Update review empty states to 14px font size and align select file empty state
- Center file tree empty state with 32px top margin
- Implement non-fatal error handling in app
- Fix agent fallback colors in app
- Added forward and back navigation buttons
- Add missing tooltips in app
- Auto-scroll button sometimes sticks in the app
- Deduplicate Tauri configuration files (@Brendonovich)
- Only show files in select dialog when clicking + tab
- Disable magnification gestures on macOS desktop (@ysm-dev)
- Add Connect provider in model selector (@ProdigyRahul)
- Add file tree specification tests
- Enable file watcher in app
- Improve file tree performance in app
- Add highlights feature
- Add new release modal
- Fix Zen mode disconnect not working in app
- Disconnect Zen provider
- Fix e2e test in app package
- Disable tooltips in file tree tabs
- Move file tree toggle button to the right side
- Fade filetree guide lines on hover
- Dim non-deep filetree guide lines in the app interface
- Reduce file tree folder indent
- Refine file tree row spacing and indentation
- Use medium font weight for filetree items
- Use chevron icons for filetree folders
- Tighten file tree row spacing
- Adjust filetree panel padding
- Scope filetree pill tabs styling
- Add Vercel AI Gateway provider description
- Add provider descriptions to settings
- Add transition to command palette
- Add transition to select provider dialog
- Add optional transition animations to dialog
- Style view all button with interactive color and margin
- Add models icon and use in settings UI
- Add providers icon and use in settings
- Use default cursor for environment provider text
- Add hover text for environment-connected providers
- Set provider row height to 56px
- Update button styles and disconnect button size in UI
- Fix session synchronization issue in application
- Add missing i18n strings in app
- Add session load limit to prevent excessive memory usage
- Add end-to-end test for sidebar navigation
- Replace signals with createStore in app
- Add file tree mode to app
- Add file tree view to app
- Use focus-visible instead of focus to prevent sticky hover effect on click (@ProdigyRahul)
- Better sidebar hover behavior when collapsed
- Make sidebar full-height in app
- Add full-height hover effect to sidebar
- Add model settings to application
- Add model settings interface to app
- Handle non-tool call permissions in app
- Default servers on web
- Performance improvements in the app
- Add missing translations for status messages
- Don't allow workspaces in non-VCS projects

**Thank you to 17 community contributors:**
- @MartinWie:
  - docs: fix permission event name (permission.asked not permission.updated) (#10588)
- @ariane-emory:
  - fix(tui): Move animations toggle to global System category (resolves #10495) (#10497)
  - fix: Make diff wrapping toggle always available in command_list and correct a type error (resolves #10682) (#10683)
- @R44VC0RP:
  - Add highlight tag parsing for changelog with video support
  - Add collapsible sections, sticky version header, and style refinements for changelog highlights
  - fix(web): update spacing on the changelog page
  - docs: add warning about Claude Pro/Max subscription support (#10595)
  - fix: move changelog footer outside content div to fix padding (#10712)
  - fix: add 44px top padding to sticky version header on changelog (#10715)
  - feat(release): add highlights template to draft releases (#10745)
  - feat: add /learn command to extract session learnings to scoped AGENTS.md files (#10717)
- @IdrisGit:
  - fix(tui): add visual feedback for diff wrap and conceal toggles (#10655)
- @noamzbr:
  - fix: await SessionRevert.cleanup for shell (#10669)
- @SteffenDE:
  - feat(opencode): add agent description (#10680)
- @sam-huckaby:
  - fix(app): Order themes alphabetically (#10698)
- @alexyaroshuk:
  - fix(app): restore external link opening in system browser (#10697)
  - feat(app): add 'connect provider' button to the manage models dialog (#10887)
- @ProdigyRahul:
  - fix(ui): use focus-visible instead of focus to prevent sticky hover effect on click (#10651)
  - fix(app): add connect provier in model selector (#10706)
- @zerone0x:
  - fix(enterprise): add message navigation to share page desktop view (#10071)
- @tim-smart:
  - fix: ensure openai 404 errors are retried (#10590)
- @fabiomartino:
  - docs: add Italian README (#10732)
- @ysm-dev:
  - fix(desktop): disable magnification gestures on macOS (#10605)
- @Brendonovich:
  - desktop: deduplicate tauri configs
- @dpuyosa:
  - feat(opencode): Handle Venice cache creation tokens (#10735)
- @OpeOginni:
  - chore(docs): Better explanation on how to allow tools in external directories (#10862)
- @rgodha24:
  - feat: support headless authentication for chatgpt/codex (#10890)


## [1.1.36] - 2026-01-25

## Core
- Enable thinking for Google Vertex Anthropic models (@MichaelYochpaz)
- Make question validation more lax to avoid tool call failures
## TUI
- Prevent crash when theme search returns no results (@ishaksebsib)
## Desktop
- Visual cleanup in app
- Scroll to comment on click in app
- Fixed crash when no default model is set
- Performance improvements in the app package
- Clean up comment component usage in app

**Thank you to 5 community contributors:**
- @MichaelYochpaz:
  - fix(provider): enable thinking for google-vertex-anthropic models (#10442)
- @ProdigyRahul:
  - fix(app): cursor on resize (#10293)
- @DNGriffin:
  - fix(app): mobile horizontal scrolling due to session stat btn (#10487)
- @ishaksebsib:
  - fix(tui): prevent crash when theme search returns no results (#10565)
- @R44VC0RP:
  - fix(web): add & fix the download button (#10566)

