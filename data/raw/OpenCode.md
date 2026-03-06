# OpenCode Changelog


## [1.2.18] - 2026-03-05

## Core
- Handle SIGHUP signal and kill process gracefully
## TUI
- Add onClick handler to InlineTool and Task components
- Add options to auth login command to skip interactive questions (@dbpolito)
- Don't let Dax touch the UI
## Desktop
- Fork Ghostty for web-based terminal implementation
- Show errors for stale keyed components
- Fixed locale error in app
- Resolve stale read error in app
- Improve provider settings consistency in app
- Preserve question dock state across session switches (@ualtinok)
- Fix icon jiggle in app
- Open search with Mod+F even when editor is not focused
- Improve error handling and translation in desktop server error formatting (@OpeOginni)
- Improve agent selection logic to correctly pass configured models and variants (@OpeOginni)
- Remove unnecessary macOS entitlements
- Add desktop deep link support for creating new sessions
- Prefer using useLocation hook instead of window.location in app
## SDK
- Update SDK package.json

**Thank you to 4 community contributors:**
- @stolinski:
  - docs: Add opencode-sentry-monitor to ecosystem documentation (#16037)
- @dbpolito:
  - feat(opencode): Adding options to auth login to skip questions (#14470)
- @OpeOginni:
  - fix(app): improve agent selection logic passing in configured models and variants correctly (#16072)
  - refactor(desktop): improve error handling and translation in server error formatting (#16171)
- @ualtinok:
  - fix(app): preserve question dock state across session switches (#16173)


## [1.2.17] - 2026-03-04

## Core
- Rework workspace integration and adaptor interface
- Clarify output capture guidance in bash tool documentation
## TUI
- Show scrollbar by default
- Prevent orphaned opencode subprocesses on shutdown
- Validate agent when running with attach flag (@alberti42)
## Desktop
- Remove blur from todos in app
- Delay dock animation on session load
- Remove diff lines from sessions in sidebar
- Loading session should be scrolled to the bottom
- Close terminal tabs properly

**Thank you to 3 community contributors:**
- @Copilot:
  - revert: undo turbo typecheck dependency change from #14828 (#15902)
- @alberti42:
  - fix: `run --attach` agent validation (#11812)
- @Niraj12chaudhary:
  - fix(docs): update dead opencode-daytona ecosystem link (#15979)


## [1.2.16] - 2026-03-03

## Core
- Normalize trailing slashes in auth login URLs (@elithrar)
- Upgrade OpenTUI to v0.1.86 and enable markdown rendering by default
- Avoid Gemini combiner schema sibling injection
- Forward metadata options to Cloudflare AI Gateway provider (@ryanskidmore)
- Clone part data in Bus event to preserve token values (@ryanskidmore)
- Recover from 413 Request Entity Too Large errors via automatic compaction (@bentrd)
- Show human-readable message for HTML error responses (@rianvdm)
- Kill orphaned MCP child processes and expose OPENCODE_PID on shutdown (@ryanwyler)
- Add workspace_id to session table
- Add WorkspaceContext to core
- Basic implementation of remote workspace support
- Change keybindings to navigate between child sessions
- Fixed test issues
- Fixed terminal rendering and interaction issues in the application
## TUI
- Replace curved arrow with straight arrow for better terminal compatibility
- Show pending tool call count in TUI instead of generic 'Running...' message
- Use arrow indicator for active tool execution in TUI
- Disable session navigation commands when no parent session (@jerome-benoit)
- Fixed project ID conflict and updated handling for same session ID (@noamzbr)
- Improve task tool display with subagent keybind hints and spinner animations
- Add Go provider list command
## Desktop
- Defer diff rendering
- Fixed timeline performance jank in the application
- Tighten up header elements in the app
- Stabilize project close navigation
- Add comprehensive animation system with multiple easing functions and transition utilities
- Default auto-respond to false
- Refactor app to use SolidJS
- Move session review bottom padding to UI layer
- Fix latest.json finalizer in desktop application
- Revert Polish Turkish translations
- Use correct download link in finalize-latest-json script
- Faster session switching via windowed rendering and staged timeline
- Add compact UI to the app (@neriousy)
- Polish Turkish translations (@vaur94)
- Fallback to synthetic icon for unknown provider IDs (@rexdotsh)
- Fixed scroll issues in the app
- Synchronize internationalization translations
- Add Warp to the open menu
- Add latest.json finalizer script for desktop builds
- Auto-accept permissions in app
- Add Turkish locale support for app and UI packages (@vaur94)
- Add recent projects section to command palette (@neriousy)
- Move desktop open_path functionality to Rust
- Allow providing username and password when connecting to remote server
- Fixed permission indicator in app
- Add permission notifications to app
- Show keybind on context tab close button
- Better diff and code comments in app
- Deduplicate file tree scroll state management
- Align review changes select height
- Mute inactive file tab icons
- Set max-width on session when review is closed but file tree is open
- Add border to file tree on scroll
- Fix session tab alignment in compact view to prevent vertical overflow
- New tabs styling in the app
- Auto-accept all permissions mode
- Enhance project tile interaction with suppress hover functionality (@OpeOginni)
- Simplify review layout
- Restore shell path environment for desktop sidecar
- Open app in PowerShell instead of Command Prompt on Windows (@neriousy)
## SDK
- Add zen mode feature

**Thank you to 17 community contributors:**
- @neriousy:
  - fix(app): open in powershell (#15112)
  - feat(app): recent projects section in command pallette (#15270)
  - fix(app): show proper usage limit errors (#15496)
  - fix(app): make provider icon resolved id reactive (#15583)
  - feat(app): add compact ui (#15578)
  - feat(app): show which messages are queued (#15587)
- @niushuai1991:
  - docs: Sync zh_CN docs with English Version (#15228)
- @OpeOginni:
  - refactor(desktop): enhance project tile interaction with suppress hover functionality (#15214)
- @pirrozani:
  - docs(readme): add Greek translation and update language navigation (#15281)
- @vaur94:
  - feat(app): add Turkish (tr) locale for app and ui packages (#15278)
  - fix(i18n): polish turkish translations (#15491)
- @Niraj12chaudhary:
  - docs: add missing Bosanski link to Arabic README (#15399)
- @alexyaroshuk:
  - fix(app): make bash output selectable (#15378)
  - fix(app): display skill name in skill tool call (#15413)
- @rexdotsh:
  - fix(app): fallback to synthetic icon for unknown provider IDs (#15295)
- @inkdust2021:
  - docs(ecosystem): add opencode-vibeguard (#15464)
- @ryanwyler:
  - fix: kill orphaned MCP child processes and expose OPENCODE_PID on shu… (#15516)
- @rianvdm:
  - fix(opencode): show human-readable message for HTML error responses (#15407)
- @noamzbr:
  - fix: project ID conflict, and update on same session id (#15596)
- @bentrd:
  - fix: recover from 413 Request Entity Too Large via auto-compaction (#14707)
- @ryanskidmore:
  - fix(opencode): clone part data in Bus event to preserve token values (#15780)
  - fix(provider): forward metadata options to cloudflare-ai-gateway provider (#15619)
- @jerome-benoit:
  - fix(opencode): disable session navigation commands when no parent session (#15762)
- @06ergin06:
  - fix: update Turkish translations (#15835)
- @elithrar:
  - fix(auth): normalize trailing slashes in auth login URLs (#15874)


## [1.2.15] - 2026-02-26

## Core
- Fix most segfaults on Windows with Bun v1.3.10 stable
- Split TUI and server configuration
## Desktop
- Remove interactive shell flag from sidecar spawn to prevent hang on macOS (@kilhyeonjun)
- Fixed permissions and questions handling from child sessions in the app
- Fixed keyboard navigation for previous/next message (@neriousy)
- Correct Copilot provider description in i18n files (@Oleksii-Pavliuk)

**Thank you to 5 community contributors:**
- @Oleksii-Pavliuk:
  - fix(app): correct Copilot provider description in i18n files (#15071)
- @neriousy:
  - fix(app): keyboard navigation previous/next message (#15047)
- @OpeOginni:
  - fix(docs): update schema URL in share configuration examples across multiple languages (#15114)
- @kilhyeonjun:
  - fix(desktop): remove interactive shell flag from sidecar spawn to prevent hang on macOS (#15136)
- @choephix:
  - fix(app): middle-click tab close in scrollable tab bar (#15081)


## [1.2.14] - 2026-02-25

## Core
- Add message delete endpoint (@shantur)
## TUI
- Consume stdout concurrently with process exit in auth login (@Ayushlm10)

**Thank you to 2 community contributors:**
- @Ayushlm10:
  - fix: consume stdout concurrently with process exit in auth login (#15058)
- @shantur:
  - feat(core): add message delete endpoint (#14417)


## [1.2.13] - 2026-02-25

No notable changes


## [1.2.12] - 2026-02-25

## Core
- Synchronize changes
- Temporarily disable plan enter tool to prevent unintended mode switches during task execution
- Migrate Bun.spawn to Process utility with timeout and cleanup
- Disable Bun config cache in CI
- Await git ID cache write in project module
- Import custom tools via file URL
## TUI
- Add Go SDK code generation script
- Show LSP errors for apply_patch tool
## Desktop
- Enhance Windows app resolution and UI loading states (@neriousy)
- Update desktop README for accuracy

**Thank you to 1 community contributor:**
- @neriousy:
  - feat(desktop): enhance Windows app resolution and UI loading states (#13320)


## [1.2.11] - 2026-02-24

## Core
- Add workspace-serve command (experimental)
- ACP both live and load share synthetic pending status preceding actual data (@noamzbr)
- Replace structuredClone with spread operator for process.env in tests
- Add 50ms tolerance for NTFS mtime precision in Windows FileTime assertions
- Replace Unix-only test assumptions with cross-platform alternatives
- Use path.sep in discovery test for cross-platform path matching
- Normalize backslash paths in config rel() and file ignore on Windows
- Fix plugin resolution with createRequire fallback on Windows
- Harden preload cleanup against Windows EBUSY errors
- Normalize git excludesFile path for Windows in tests
- Stream bash output and add synthetic pending events to ACP (@noamzbr)
- Add git flags for snapshot operations and fix tests for cross-platform on Windows
- Handle CRLF line endings in markdown frontmatter parsing on Windows
- Use path.join for cross-platform glob test assertions
- Upgrade to Bun 1.3.10 canary and force baseline builds always
- Normalize paths at permission boundaries on Windows
- Windows path support and canonicalization (@edemaine)
- Upgrade OpenTUI to v0.1.81
- Change detection on Windows, especially Cygwin (@edemaine)
- Cache platform binary in postinstall for faster startup
- Revert caching platform binary in postinstall for faster startup
- Cache platform binary in postinstall for faster startup
- Publish desktop beta releases to a separate repository
- Add experimental endpoint to list all sessions
- Fixed terminal issues in the app
- Respect info exclude in snapshot staging
- Missing plugin dependencies cause TUI to black screen (@elithrar)
## TUI
- Support variant parameter in GitHub Actions and OpenCode GitHub run command (@elithrar)
## Desktop
- Ignore stale part deltas in the application
- Fix bug where lines remain highlighted after canceling a comment (@neriousy)
- Replace error handling with serverErrorMessage utility and add ConfigInvalidError checks (@OpeOginni)
- Preserve native path separators in file path helpers
- Remove file tree tooltips
- Update createOpenReviewFile test to match new call order
- Wait for loadFile to complete before opening file tab
- Windows E2E test failures due to IPv6 networking issues resolved
- Correct inverted chevron direction in todo list (@kevinWangSheng)
- Feed customization options
- Add beta icon to desktop application
- E2E test updated to current version
- Remove double-border in share button
- Better sound effect disabling UX
- Add custom scroll view to app
- Show and hide reasoning summaries in the app
- Stay pinned with auto-scroll on todos, questions, and permissions
- Bring back -i flag in sidecar arguments for desktop
- Large text pasted into prompt input no longer causes main thread to lock
## SDK
- Scripts using Turbo commands would not run on Windows

**Thank you to 10 community contributors:**
- @elithrar:
  - fix(cli): missing plugin deps cause TUI to black screen (#14432)
  - fix(github): support variant in github action and opencode github run (#14431)
- @tuhin-cmd:
  - docs: add Bangla README translation (#14331)
- @Seungjun0906:
  - docs(ko): improve wording in gitlab, ide, index, keybinds, and lsp docs (#14517)
- @github-actions[bot]:
  - Update VOUCHED list
- @pirrozani:
  - docs(tui): correct typo in TUI documentation (#14604)
- @edemaine:
  - fix(desktop): change detection on Windows, especially Cygwin (#13659)
  - fix: Windows path support and canonicalization (#13671)
- @kevinWangSheng:
  - fix(app): correct inverted chevron direction in todo list (#14628)
- @noamzbr:
  - feat: ACP - stream bash output and synthetic pending events (#14079)
  - fix: ACP both live and load share synthetic pending status preceeding… (#14916)
- @OpeOginni:
  - refactor: replace error handling with serverErrorMessage utility and checks for if error is ConfigInvalidError (#14685)
- @neriousy:
  - fix(app): on cancel comment unhighlight lines (#14103)


## [1.2.10] - 2026-02-20

## Desktop
- Don't spawn sidecar if default is localhost server
## SDK
- Build SDK to dist/ instead of dist/src

**Thank you to 1 community contributor:**
- @rmk40:
  - docs: clarify tool name collision precedence (#14313)


## [1.2.9] - 2026-02-20

## Core
- Add missing id, sessionID, and messageID to MCP tool attachments (@NatChung)
- Remove unnecessary deep clones from session loop and LLM stream
- Remove User-Agent header assertion from LLM test to fix failing test
## TUI
- Use structuredClone instead of remeda's clone for better performance and native support (@mhart)
## Desktop
- Restore settings header mask

**Thank you to 2 community contributors:**
- @mhart:
  - Use structuredClone instead of remeda's clone (#14351)
- @NatChung:
  - fix: add missing id/sessionID/messageID to MCP tool attachments (#14345)


## [1.2.8] - 2026-02-19

## Core
- Support adaptive thinking for Claude Sonnet 4.6 (@tctev)
## TUI
- Add custom tool and MCP call responses that are visible and collapsible (@yanosh-k)
## Desktop
- Black screen on launch with sidecar server fixed
- Clear todos on abort

**Thank you to 2 community contributors:**
- @yanosh-k:
  - feat(tui): add custom tool and mcp call responses visible and collapsable (#10649)
- @tctev:
  - feat(opencode): support adaptive thinking for claude sonnet 4.6 (#14283)


## [1.2.7] - 2026-02-19

## Core
- Fixed terminal rendering and interaction issues in the application
- Normalize file status paths relative to instance directory (@shantur)
- Migrate from Bun.Glob to npm glob package
- Bump AI SDK packages for Google, Google Vertex, Anthropic, Bedrock, and provider utils
- Add support for medium reasoning with Gemini 3.1
- Remove use of Bun.file
- Text files misclassified as binary
- Fetch default server at top level in desktop application
- Terminal rework in the app
- Bake in the AWS and Google authentication packages
- Token substitution in OPENCODE_CONFIG_CONTENT now works correctly (@ariane-emory)
- Revert migration from Bun.file() to Filesystem module
- Migrate project.ts from Bun.file() to Filesystem/stat modules
- Migrate read tool from Bun.file() to Filesystem module
- Migrate write tool from Bun.file() to Filesystem module
- Migrate Edit tool from Bun.file() to Filesystem module
- Migrate remaining tool files from Bun.file() to Filesystem/stat modules
- Migrate storage.ts from Bun.file()/Bun.write() to Filesystem module
- Migrate src/storage/json-migration.ts from Bun.file() to Filesystem module
- Migrate MCP auth module from Bun file APIs to Filesystem module
- Migrate storage database from Bun.file() to statSync for file existence checks
- Migrate session prompt module from Bun.file() to Filesystem/stat modules
- Fix crash in `opencode run` and show errored tool calls in output
- Migrate skill discovery to use Filesystem module instead of Bun file APIs
- Migrate session instruction handling from Bun.file() to Filesystem module
- Migrate provider.ts from Bun.file() to Filesystem module
- Migrate shell.ts from Bun.file() to statSync for improved file system operations
- Migrate log utility from Bun.file() to Node.js fs module for better compatibility
- Migrate models.ts from Bun.file()/Bun.write() to Filesystem module
- Use HashiCorp releases API for installing terraform-ls (@edubxb)
- Migrate LSP server from Bun.file()/Bun.write() to Filesystem module
- Migrate session command from Bun.file() to statSync for improved file system operations
- Migrate agent.ts from Bun.file() to Filesystem module
- Migrate auth module from Bun.file()/Bun.write() to Filesystem module
- Pass sessionID and callID to shell.env hook input (@tesdal)
- Fix terminal cross-talk issue in the application
- Update SST version
- Migrate src/global/index.ts from Bun.file() to Filesystem module
- Emit PROMPT_TOO_LARGE error when GitHub context overflows (@elithrar)
- Migrate src/bun/index.ts from Bun.file()/Bun.write() to Filesystem module
- Migrate config/markdown.ts from Bun.file() to Filesystem module
- Migrate file/index.ts from Bun.file() to Filesystem module
- Migrate format/formatter.ts from Bun.file() to Filesystem module
- Allow readJson to be called without explicit type parameter
- Migrate file/ripgrep.ts from Bun APIs to Filesystem module
- Migrate index.ts from Bun.file() to Filesystem module
- Add Julia language server support (@zarly)
- Bump GitLab AI provider to 3.6.0 to add Sonnet 4.6 support (@vglafirov)
- Add centralized filesystem module for Bun.file migration
- Fix Clojure syntax highlighting (@finalfantasia)
- Ensure explore subagent prompts for external directory permission instead of auto-denying
- Don't autoload kilo
- Add Kilo as a native provider (@Nomadcxx)
- Simplify redundant ternary in updateMessage (@yikayiyo)
- Ensure Read tool uses fs/promises for all file system operations
- Make read tool more memory efficient
- Surface plugin auth providers in the login picker (@anoldguy)
- Invalidate OAuth credentials when OAuth provider indicates they are invalid (@GreenStage)
- Don't fetch models.dev on completion (@gigamonster256)
- Recover state after SSE reconnect and harden SSE streams
- Keep message part order stable when files resolve asynchronously
- Drop IDs from attachments in tools and assign them in prompt.ts instead
## TUI
- Improve GitHub action branch detection and handle 422 errors (@elithrar)
- Ensure onExit callback fires after terminal output is written
- Migrate TUI thread module from Bun.file() to Filesystem module
- Migrate agent command from Bun.file()/Bun.write() to Filesystem module
- Migrate import command from Bun.file() to Filesystem module
- Update pasteImage to only increment count when the previous attachment is an image (@OpeOginni)
- Migrate editor.ts from Bun.file()/Bun.write() to Filesystem module
- Migrate clipboard.ts from Bun.file() to Filesystem module
- Migrate CLI run command from Bun.file() to Filesystem/stat modules
- Session list --max-count parameter now correctly limits the number of sessions displayed (@mharris717)
- Exit cleanly without hanging after session ends
- Style scrollbox for permission and sidebar (@akronb)
- Increase button heights and improve permission prompt layout alignment
- Display new session banner with logo and project details in TUI
## Desktop
- Update Japanese translations for WSL integration (@taroj1205)
- Made localhost URLs work correctly in isLocal function
- Navigate to last session when navigating to a project
- Fix typecheck errors in app
- Deduplicate allServers list in app
- Adjust session turn horizontal padding
- Tighten prompt dock padding in app
- Fixed sidecar spawning a window on Windows
- Delay prompt mode toggle tooltip
- Shorten prompt mode toggle tooltips in the app
- Reduce review panel padding
- Tweak search button style in UI
- Expanded color state on titlebar buttons
- Tweak hover and active styles for title bar buttons
- Share button now has a border
- Adjust file tree background color
- Handle sidecar key in projectsKey for desktop projects
- Fixed desktop app incorrectly identifying local servers
- Refactor server management backend
- Use group-hover for file tree icon color swap at all nesting levels
- Simplify mode toggle icon styling in TUI
- Clean up desktop implementation
- Temporarily disable WSL support in desktop application
- Use radio group in prompt input
- Simplify prompt mode toggle icon colors via CSS and tighten message timeline padding in TUI
- Fix prompt input quirks in app
- Terminal disconnect and resync functionality fixed
- Replicate tauri-plugin-shell logic in desktop application
- Improve modified file visibility and button spacing in TUI
- Show monochrome file icons by default in tree view, revealing colors on hover to reduce visual clutter
- Fix share button text styling to use consistent 12px regular font weight
- Add warning icon to permission requests for better visibility
- Extract dock prompt shell component
- UI no longer flashes when switching tabs (@neriousy)
- Avoid sidecar health-check timeout on shell startup in desktop app (@ysm-dev)
- Increase prompt mode toggle height for better clickability
- Add more end-to-end tests for desktop application (@neriousy)
- Update magnifying-glass icon in UI
- Tighten titlebar action padding
- Refine titlebar search and open padding
- Center titlebar search and soften keybind styling
- Align titlebar search text size
- Match titlebar active background to hover
- Use weak borders in titlebar actions
- Reduce titlebar right padding
- Keep file tree toggle visible
- Adjust icon button spacing in UI
- Session timeline and turn handling reworked in app
- Keep Escape handling local to prompt input on macOS desktop (@itskritix)
- Hide server CLI window on Windows
## SDK
- Fix nested exports transformation in SDK publish script

**Thank you to 25 community contributors:**
- @itskritix:
  - fix(app): keep Escape handling local to prompt input on macOS desktop (#13963)
- @vynnlee:
  - docs(ko): improve Korean translation accuracy and clarity in Zen docs (#13951)
- @chenmijiang:
  - docs: improve zh-cn and zh-tw documentation translations (#13942)
- @hmu332233:
  - fix(docs): correct reversed meaning in Korean plugins logging section (#13945)
- @neriousy:
  - feat(desktop): more e2e tests (#13975)
  - fix(app): ui flashing when switching tabs (#13978)
- @ysm-dev:
  - fix(desktop): avoid sidecar health-check timeout on shell startup (#13925)
- @alexcarpenter:
  - fix: Homepage video section layout shift (#13987)
- @gigamonster256:
  - fix: don't fetch models.dev on completion (#13997)
- @GreenStage:
  - fix: Invalidate oauth credentials when oauth provider says so (#14007)
- @anoldguy:
  - feat: surface plugin auth providers in the login picker (#13921)
- @akronb:
  - fix(tui): style scrollbox for permission and sidebar (#12752)
- @yikayiyo:
  - refactor: simplify redundant ternary in updateMessage (#13954)
- @Nomadcxx:
  - feat: add Kilo as a native provider (#13765)
- @finalfantasia:
  - fix(opencode): fix Clojure syntax highlighting (#13453)
- @mharris717:
  - fix(cli): session list --max-count not honored, shows too few sessions (#14162)
- @vglafirov:
  - feat: GitLab Duo - bump gitlab-ai-provider to 3.6.0 (adds Sonnet 4.6) (#14115)
- @zarly:
  - feat: add Julia language server support (#14129)
- @elithrar:
  - fix(github): emit PROMPT_TOO_LARGE error on context overflow (#14166)
  - fix(github): action branch detection and 422 handling (#14322)
- @OpeOginni:
  - fix(opencode): update pasteImage to only increment count when the previous attachment is an image too (#14173)
- @tesdal:
  - feat(plugin): pass sessionID and callID to shell.env hook input (#13662)
- @edubxb:
  - fix(lsp): use HashiCorp releases API for installing terraform-ls (#14200)
- @ariane-emory:
  - fix: token substitution in OPENCODE_CONFIG_CONTENT (alternate take) (#14047)
- @Seungjun0906:
  - docs(ko): improve wording in ecosystem, enterprise, formatters, and github docs (#14220)
- @shantur:
  - fix(core): normalize file.status paths relative to instance dir (#14207)
- @taroj1205:
  - feat(i18n): update Japanese translations to WSL integration (#13160)


## [1.2.6] - 2026-02-16

## Core
- Add dfmt formatter support for D language files (@burner)
- Bump GitLab provider and auth plugin for mid-session token refresh (@vglafirov)
- Remove unnecessary per-message title LLM calls (@rmk40)
- Prioritize user-defined variables over environment variables in Google Vertex AI configuration
- Add OpenAI-compatible endpoint support for Google Vertex provider (@leehack)
- Add Venice support for temperature, topP, topK, and smallOption parameters (@dpuyosa)
- Add cljfmt formatter support for Clojure files (@finalfantasia)
## TUI
- Make use of server directory path for file references in prompts (@OpeOginni)
- Add database migration command to convert JSON storage to SQLite
- Add --continue and --fork flags to attach command
- Fixed inaccurate tips in TUI (@imanolmzd-svg)
## Desktop
- Normalize Linux Wayland/X11 backend and decoration policy (@bnema)
- Use process-wrap library instead of manual job object handling in desktop (@Brendonovich)

**Thank you to 12 community contributors:**
- @finalfantasia:
  - feat(opencode): add `cljfmt` formatter support for Clojure files (#13426)
- @pkx07:
  - fix(website): correct zh-CN translation of proprietary terms in zen.mdx (#13734)
- @Brendonovich:
  - desktop: use process-wrap instead of manual job object (#13431)
- @dpuyosa:
  - feat(opencode): Add Venice support in temperature, topP, topK and smallOption (#13553)
- @bnema:
  - fix(desktop): normalize Linux Wayland/X11 backend and decoration policy (#13143)
- @leehack:
  - feat: add openai-compatible endpoint support for google-vertex provider (#10303)
- @hobostay:
  - fix(docs): correct critical translation errors in Russian zen page (#13830)
- @rmk40:
  - fix(core): remove unnecessary per-message title LLM calls (#13804)
- @imanolmzd-svg:
  - fix (tui): Inaccurate tips (#13845)
- @vglafirov:
  - fix: bump GitLab provider and auth plugin for mid-session token refresh (#13850)
- @OpeOginni:
  - fix(tui): make use of server dir path for file references in prompts (#13781)
- @burner:
  - feat(opencode): add `dfmt` formatter support for D language files (#13867)


## [1.2.5] - 2026-02-15

## Core
- Ensure SQLite migration logs to stderr instead of stdout
## Desktop
- Fixed issue viewing new files opened from the file tree (@shanebishop1)
- Only navigate prompt history at input boundaries (@nexxeln)
- Add keyboard shortcut Shift+Tab to the application (@neriousy)
- Focus window after update and relaunch (@zerone0x)
- Add GeistMono Nerd Font to available mono font options (@brandon-julio-t)

**Thank you to 7 community contributors:**
- @brandon-julio-t:
  - feat: Add GeistMono Nerd Font to available mono font options (#13720)
- @zerone0x:
  - fix(desktop): focus window after update/relaunch (#13701)
- @dector:
  - docs: add Ukrainian README translation (#13697)
- @neriousy:
  - fix(app): keybind [shift+tab] (#13695)
- @nexxeln:
  - fix(app): only navigate prompt history at input boundaries (#13690)
- @shanebishop1:
  - fix(desktop): issue viewing new files opened from the file tree (#13689)
- @alexyaroshuk:
  - feat(app): localize "free usage exceeded" error & "Add credits" clickable link (#13652)


## [1.2.4] - 2026-02-15

## Core
- Add db command for database inspection and querying
- Derive all IDs from file paths during JSON migration
## Desktop
- Clear notifications action
- Fixed stack overflow issue in file tree component


## [1.2.3] - 2026-02-15

## Core
- Ensure Anthropic models on OpenRouter also have variant support
- Add WAL checkpoint on database open
- Ensure Vercel variants pass Amazon models under Bedrock key


## [1.2.0] - 2026-02-14

This release includes a data migration that will execute on first run. It will migrate all flat files in data directory to a single sqlite database. Depending on how much data you have and speed of computer this can take some time.

if anything goes wrong you can retrigger the migration by deleting ~/.local/share/opencode/opencode.db* files (%APPDATA% on windows)

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


## [1.2.2] - 2026-02-14

## Core
- Add comprehensive test coverage for Session.list() filters
- Filter sessions at database level to improve session list loading performance
- Fix Vercel gateway variants
- Bump Vertex AI packages


## [1.2.1] - 2026-02-14

v1.2.0 and beyond includes a data migration that will execute on first run. It will migrate all flat files in data directory to a single sqlite database. Depending on how much data you have and speed of computer this can take some time.

if anything goes wrong you can retrigger the migration by deleting `~/.local/share/opencode/opencode.db*` files (%APPDATA% on windows)

If you have any issues with the migration the original data is not yet deleted and downgrading should work. But please open an issue so we can investigate and include sqlite in the issue title.


SDK Users

We now have a PartDelta event which sends only incremental changes to parts. This avoids sending the full content of text parts over and over when it is updated

## Core
- Show all project sessions from any working directory
- Tweak websearch tool description date info to avoid cache busts


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

