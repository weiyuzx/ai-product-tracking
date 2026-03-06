# RooCode Changelog


## [3.51.0] - 2026-03-05

Release v3.51.0

## [cli-v0.1.17] - 2026-03-04

## What's New


### Added

- **Custom Session ID Support**: New `--create-with-session-id` flag allows specifying a custom UUID session ID when creating tasks. Session IDs are now validated as UUIDs for both create and resume operations, as well as for `start.taskId` in stdin-stream mode.

### Tests

- Added integration coverage for create+resume loading the correct session.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.17 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
cf3c1612cd6cd1e50d3db005548a071a634f17a62ca8e8b1ead5a6e832763537  roo-cli-darwin-arm64.tar.gz
d22cf06ccbaf3e9eaed8a9ccebbc4df700e00469390381dfcb33e6af5c672d53  roo-cli-linux-arm64.tar.gz
4f007b9016bb0792943680890f5aa0b52279ee168437100b9f4d32240be5b538  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.16] - 2026-03-04

## What's New


### Added

- **Custom Shell Selection**: New `--terminal-shell` flag to specify which shell to use for inline command execution. The shell path is validated at the CLI layer and passed through the standard settings mechanism.

### Tests

- Added integration coverage for stdin stream routing and race invariants.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.16 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
3fecad24f9a8c0cc16c4701bd03ca1eb4e59704d25af74dbfb9075f156378530  roo-cli-darwin-arm64.tar.gz
879b3e3365d8cc87a0d935f5f27a9bdf190a478ce4bd4bd255d412a0cd50441f  roo-cli-linux-arm64.tar.gz
9b126dbc9228c8f943d833b1b053e0a3da4492ce9836cd967d04d3e18252250c  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.15] - 2026-03-03

## What's New


### Fixed

- **Follow-up Routing for Completion Asks**: Fixed routing of follow-up messages when the agent asks for clarification (ask_followup_question) in stdin-stream mode. Messages sent after a completion ask are now correctly delivered to the agent instead of being queued.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.15 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
d216522eb88e036b83889bed36d91cc9330fb9a2900f257d29b269d3cc04bbe5  roo-cli-darwin-arm64.tar.gz
c37047031a684b4b2a2bb51a0b8e37b46573d7ef317590587734765cbcca36e3  roo-cli-linux-arm64.tar.gz
8854ba9d52291f61ce01a306c8a022f71bf500c7152032a4238d29ddf0b71f3e  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.14] - 2026-03-03

## What's New


### Fixed

- **Command Output Streaming**: Ensure full command output is streamed before the done event is emitted, preventing truncated output in stdin-stream mode.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.14 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
c6cbbd3041187b2dcd4570180fc2a9cba6bf63f812280f64004f609207e56a22  roo-cli-darwin-arm64.tar.gz
cba14598aa7baaa6cf6bbf22a955ad9803793f18c5d44d9c9d50884f87565068  roo-cli-linux-arm64.tar.gz
d13e7091270185c0acd7c7fabd0d464f17bcd03bd5b37eedb8100b0e0955c0dd  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.9] - 2026-03-02

## What's New


### Fixed

- **Stdin Stream Cancel Race**: Fixed a race condition during startup cancellation in stdin-stream mode that could cause unexpected behavior when canceling tasks immediately after starting them.

### Tests

- **Integration Test Suite**: Added comprehensive integration test suite for stdin-stream protocol covering cancel, followup, multi-message queue, and shutdown scenarios.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.9 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
c9d4f359ceb0e226da7a24eb055c3fb4fc4741199f50944e2e84267b949cbec5  roo-cli-darwin-arm64.tar.gz
a5fb4cd77a6f5e22b24f485b52c6194a22b16bca31adb7211c8bb7ae59f3c47f  roo-cli-linux-arm64.tar.gz
7ee4ab328771df429cdd69cb8a23d493b7d5dfb5c6ef4407ec18af04d5eec69b  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.8] - 2026-03-02

## What's New


### Changed

- **Command Execution Timeout**: Increased timeout for command execution to improve reliability for long-running operations.

### Fixed

- **Stdin Stream Queue Handling**: Fixed stdin stream queued messages and command output streaming to ensure messages are properly processed.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.8 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
d2608f3ce0f05fa9fa2b505c2ff1ad2ab01a65f6b00348a5785e55e93e00bde7  roo-cli-darwin-arm64.tar.gz
e23bfa12a790f9792fe14fe64cab4ba3feb12fdab06ec9ba472defddcb9c33cc  roo-cli-linux-arm64.tar.gz
280c8d1c3ef37de70ecc1339f5a79a6e756cf8a201047b211540264b34a64e4c  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.13] - 2026-03-02

## What's New


### Added

- **Skills as Slash Commands**: Skills are now exposed as slash commands, so you can invoke skill workflows directly from command-style input.
- **Skill Fallback Execution**: When a slash command does not match a command file but matches a skill slug, the CLI can resolve and execute that skill path.

### Changed

- **Slash Command Resolution Priority**: Command precedence is preserved, with skill fallback only used when no matching slash command is found.

### Tests

- Added and updated tests for slash command + skill fallback behavior, including command precedence and duplicate skill-slug handling.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.13 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
7bf51a35dfd113b9d18b5c285c4c1d4c4e31a86c2a057fc0207f549944f4088f  roo-cli-darwin-arm64.tar.gz
ed6a4bba176568b47ff5fa20fdd53168483f21c63a323c75df4fa3e6e1f4ca5c  roo-cli-linux-arm64.tar.gz
fb7c4e82888e084c75102d9ce4e0a3ff6f6ef4ed08ca5c212ca6c4c951d61f58  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.12] - 2026-03-02

## What's New


### Fixed

- **Command Timeout Handling**: CLI runtime now correctly ignores model-provided background timeouts for commands, ensuring command lifetime is governed solely by the `--timeout` setting.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.12 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
45b28f7c578e555a6c3a679977a744e9783c3ebb30a0c1dfec5fa886cac36337  roo-cli-darwin-arm64.tar.gz
edf29223fd44628d93426ce981ef3df04c846d886c352fc99523bf789820bc8c  roo-cli-linux-arm64.tar.gz
35f98a13e507331050fb1ad697aa81845fa5d54703d657de12f886ae743bae47  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.11] - 2026-03-02

## What's New


### Added

- **Image Support in Stdin Stream**: The `start` and `message` commands in stdin-stream mode now support an optional `images` field (array of base64 data URIs) to attach images to prompts.

### Fixed

- **Upgrade Version Detection**: Fixed version detection in the `upgrade` command to correctly identify when updates are available.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.11 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
3f0b87ea0eab5a153bf580e2c091608fe71cb3d172cd1a9d19dfb6ea0326cc27  roo-cli-darwin-arm64.tar.gz
51685e02a604cbaa1e640f131b704200f3d313a510c19b25e21761363c3e7f9a  roo-cli-linux-arm64.tar.gz
32b5afce8edad0b060c2eac0d4b42fb04e737c17d12b05b3875d916cc53b138c  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.10] - 2026-03-02

## What's New


### Added

- **Command Exit Code in Events**: The `tool_result` event for command executions now includes an `exitCode` field, allowing CLI consumers to programmatically distinguish between successful and failed command executions without parsing output text.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.10 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
1a59a75f9765ec205db464339aa643cb365aaa18e03494e40afb4fab635e0d1d  roo-cli-darwin-arm64.tar.gz
f67f4962811e2ed53338ffd21e5eb9e00afdf9f77a7d78f1b8a658b64cf9ca63  roo-cli-linux-arm64.tar.gz
014d06e609bdef715c5dddc3b7f5d694e2b45a3c302c2560da28faa2ef4aa7e4  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.7] - 2026-03-01

## What's New


### Fixed

- **Stdin Stream Control Flow**: Gracefully handle control-flow errors in stdin-stream mode to prevent unexpected crashes during cancellation and shutdown sequences.

### Changed

- **Type Definitions**: Refactored and simplified JSON event type definitions for better type safety.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.7 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
96c4d0f19f06d918884d3ec0f6f5c769ed88bff2b6cf2a2c940f07484fe47171  roo-cli-darwin-arm64.tar.gz
745440a9fd878e1c4dbff951c3d6d413ed5fae44240cec3a16b7cffbc6634cfe  roo-cli-linux-arm64.tar.gz
45c26affd127296c1f1630ec6cf5e4467701da3b954d01f16b13e93b9c12ed3e  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.6] - 2026-02-27

## What's New


### Added

- **Consecutive Mistake Limit**: New `--mistake-limit` flag to configure the maximum number of consecutive mistakes before the agent pauses for intervention.

### Changed

- **Workspace-Scoped Sessions**: The `list sessions` command and `--resume` flag now only show and resume sessions from the current workspace directory.

### Fixed

- **Task Configuration Forwarding**: Task configuration (custom modes, disabled tools, etc.) passed via the stdin-prompt-stream protocol is now correctly forwarded to the extension host instead of being silently dropped.
- **Stream Error Recovery**: Improved recovery from streaming errors to prevent task interruption.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.6 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
7e8ce71d5c25277a1bae54be202151d9236405dc7de7a53da51684a8c87a6fe4  roo-cli-darwin-arm64.tar.gz
63cd3da918b013b140e20e948fc65f046208ff070b833ea39050b23ac724d0cd  roo-cli-linux-arm64.tar.gz
f7265cba7f663060777353c44a59be849814fe8454db2c4def57a722447c6f8a  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.5] - 2026-02-26

## What's New


### Added

- **Session History**: New `list sessions` subcommand to view recent CLI sessions with task IDs, timestamps, and initial prompts.
- **Session Resume**: New `--resume <taskId>` flag to continue a previous session from where it left off.
- **Upgrade Command**: New `upgrade` command to check for and install the latest CLI version.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.5 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
7b72f3b76960abcc7fb74f50cf7d4bbdd33da884bc679d1a6bed8a7eba29b380  roo-cli-darwin-arm64.tar.gz
50df8931d84fd5de80982c78103b74bd57b569e379d75e8451a650210fca3bb4  roo-cli-linux-arm64.tar.gz
2aad64715772d669eed6e855c3ea926bee9a82753da70d8ce86362475bafeaa0  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.4] - 2026-02-26

## What's New


### Fixed

- **Exception Handling**: Improved recovery from unhandled exceptions in the CLI to prevent unexpected crashes.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.4 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
8e0e816f9af501a05d3230b70ee6a431dad707e4f3a6b8e490597f5502eccacc  roo-cli-darwin-arm64.tar.gz
6d82116c26e0228d88d0ba59485dd15ec26542d4b32e10e4363f3f5fb7d7dbf0  roo-cli-linux-arm64.tar.gz
2b757425c06e1c312f806f11c7947e5e0d3299ed456e2d4d1b7abddf149fb2c6  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.3] - 2026-02-25

## What's New


### Fixed

- **Task Resumption**: Fixed an issue where resuming a previously suspended task could fail due to state initialization timing in the extension host.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.3 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
2b056cd503255be4b9650931d29d76385587c7be86b5f6afe45abb1f348f9483  roo-cli-darwin-arm64.tar.gz
0f3611c13808eabaf7562ca30e002da152468f827b6dffc60f46d7e8ac32943c  roo-cli-linux-arm64.tar.gz
9978dd30dea2c2264352c172a1c3180b89ceb17206893c3f7d276ea2a0198ed8  roo-cli-linux-x64.tar.gz
```

## [cli-v0.1.2] - 2026-02-25

## What's New


### Changed

- **Streaming Deltas**: Tool use ask messages (command, tool, mcp) are now streamed as structured deltas instead of full snapshots in json-event-emitter for improved efficiency.
- **Task ID Propagation**: Task ID is now generated upfront and propagated through runTask/createTask so currentTaskId is available in extension state immediately.
- **Custom Tools**: Enabled customTools experiment in extension host.

### Fixed

- **Cancel Recovery**: Wait for resumable state after cancel before processing follow-up messages to prevent race conditions in stdin-stream.
- **Custom Tool Schema**: Provide valid empty JSON Schema for custom tools without parameters to fix strict-mode API validation.
- **Path Handling**: Skip paths outside cwd in RooProtectedController to avoid RangeError.
- **Retry Handling**: Silently handle abort during exponential backoff retry countdown.
- Fixed spelling/grammar and casing inconsistencies.

### Added

- **Telemetry Control**: Added `ROO_CODE_DISABLE_TELEMETRY=1` environment variable to disable cloud telemetry.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.2 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
c8919cc89bc99c42d10e21d4a44166ec8ad214d63a9417e558c42154bdfe593c  roo-cli-darwin-arm64.tar.gz
b8ca68de226f8941917e3af04c7d0e9e41d941d074e0b5cdfde2b6a7b0ca0b43  roo-cli-linux-arm64.tar.gz
32309b4cf6d6176d479e44e43be66d7b35014710e91b87048f8db3c6af28c338  roo-cli-linux-x64.tar.gz
```


## [3.50.5] - 2026-02-24

Release v3.50.5

## [cli-v0.1.1] - 2026-02-24

## What's New


### Added

- **Roo Model Warmup**: When configured with the Roo provider, the CLI now proactively fetches and warms the model list during activation so that model information is available before the first prompt is sent. The warmup has a 10s timeout and failures are logged only in debug mode.
- **Unbound Provider**: Added Unbound as an available provider option.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.1 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
5c23ecde7a0e3926d9ad0cd8096028c39fe4f0b8b2243954e9c4929bdfba2f06  roo-cli-darwin-arm64.tar.gz
4c889304cba49c41d8aaef7051d1663e33fa588022bf0624a1f7fc6d223e69b5  roo-cli-linux-arm64.tar.gz
832c1f1aa2bc6b079ebad7450f235538def169e38033ca4c01052c6c54545ba9  roo-cli-linux-x64.tar.gz
```


## [3.50.4] - 2026-02-21

- Feat: Add MiniMax M2.5 model support (#11471 by @love8ko, PR #11458 by @roomote)


## [3.50.3] - 2026-02-20

Release v3.50.3


## [3.50.2] - 2026-02-20

Release v3.50.2


## [3.50.1] - 2026-02-20

Release v3.50.1


## [3.50.0] - 2026-02-19

Release v3.50.0


## [3.49.0] - 2026-02-19

Release v3.49.0

## [cli-v0.1.0] - 2026-02-19

## What's New


### Added

- **NDJSON Stdin Protocol**: Overhauled the stdin prompt stream from raw text lines to a structured NDJSON command protocol (`start`/`message`/`cancel`/`ping`/`shutdown`) with requestId correlation, ack/done/error lifecycle events, and queue telemetry. See [`stdin-stream.ts`](src/ui/stdin-stream.ts) for implementation.
- **List Subcommands**: New `list` subcommands (`commands`, `modes`, `models`) for programmatic discovery of available CLI capabilities.
- **Shared Utilities**: Added `isRecord` guard utility for improved type safety.

### Changed

- **Modularized Architecture**: Extracted stdin stream logic from `run.ts` into dedicated [`stdin-stream.ts`](src/ui/stdin-stream.ts) module for better code organization and maintainability.

### Fixed

- Fixed a bug in `Task.ts` affecting CLI operation.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.1.0 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
4dd399bc9d26ef587dddaa28185f901c72a3823cc15442f1f56d9807251487df  roo-cli-darwin-arm64.tar.gz
52b439bf016377b478b84f8c70e3f161e1005e0f3234951d376a6aefa620ab71  roo-cli-linux-arm64.tar.gz
4f4a746b9909782d0e04ff666c74f3648242205d60947e8044c6b76100e02ef9  roo-cli-linux-x64.tar.gz
```


## [3.48.1] - 2026-02-18

Release v3.48.1


## [3.48.0] - 2026-02-17

## [3.48.0]

- Add Anthropic Claude Sonnet 4.6 support across all providers — Anthropic, Bedrock, Vertex, OpenRouter, and Vercel AI Gateway (PR #11509 by @PeterDaveHello)
- Add lock toggle to pin API config across all modes in a workspace (PR #11295 by @hannesrudolph)
- Fix: Prevent parent task state loss during orchestrator delegation (PR #11281 by @hannesrudolph)
- Fix: Resolve race condition in new_task delegation that loses parent task history (PR #11331 by @daniel-lxs)
- Fix: Serialize taskHistory writes and fix delegation status overwrite race (PR #11335 by @hannesrudolph)
- Fix: Prevent chat history loss during cloud/settings navigation (#11371 by @SannidhyaSah, PR #11372 by @SannidhyaSah)
- Fix: Preserve condensation summary during task resume (#11487 by @SannidhyaSah, PR #11488 by @SannidhyaSah)
- Fix: Resolve chat scroll anchoring and task-switch scroll race conditions (PR #11385 by @hannesrudolph)
- Fix: Preserve pasted images in chatbox during chat activity (PR #11375 by @app/roomote)
- Add disabledTools setting to globally disable native tools (PR #11277 by @daniel-lxs)
- Rename search_and_replace tool to edit and unify edit-family UI (PR #11296 by @hannesrudolph)
- Render nested subtasks as recursive tree in history view (PR #11299 by @hannesrudolph)
- Remove 9 low-usage providers and add retired-provider UX (PR #11297 by @hannesrudolph)
- Remove browser use functionality entirely (PR #11392 by @hannesrudolph)
- Remove built-in skills and built-in skills mechanism (PR #11414 by @hannesrudolph)
- Remove footgun prompting (file-based system prompt override) (PR #11387 by @hannesrudolph)
- Batch consecutive tool calls in chat UI with shared utility (PR #11245 by @hannesrudolph)
- Validate Gemini thinkingLevel against model capabilities and handle empty streams (PR #11303 by @hannesrudolph)
- Add GLM-5 model support to Z.ai provider (PR #11440 by @app/roomote)
- Fix: Prevent double notification sound playback (PR #11283 by @hannesrudolph)
- Fix: Prevent false unsaved changes prompt with OpenAI Compatible headers (#8230 by @hannesrudolph, PR #11334 by @daniel-lxs)
- Fix: Cancel backend auto-approval timeout when auto-approve is toggled off mid-countdown (PR #11439 by @SannidhyaSah)
- Fix: Add follow_up param validation in AskFollowupQuestionTool (PR #11484 by @rossdonald)
- Fix: Prevent webview postMessage crashes and make dispose idempotent (PR #11313 by @0xMink)
- Fix: Avoid zsh process-substitution false positives in assignments (PR #11365 by @hannesrudolph)
- Fix: Harden command auto-approval against inline JS false positives (PR #11382 by @hannesrudolph)
- Fix: Make tab close best-effort in DiffViewProvider.open (PR #11363 by @0xMink)
- Fix: Canonicalize core.worktree comparison to prevent Windows path mismatch failures (PR #11346 by @0xMink)
- Fix: Make removeClineFromStack() delegation-aware to prevent orphaned parent tasks (PR #11302 by @app/roomote)
- Fix task resumption in the API module (PR #11369 by @cte)
- Make defaultTemperature required in getModelParams to prevent silent temperature overrides (PR #11218 by @app/roomote)
- Remove noisy console.warn logs from NativeToolCallParser (PR #11264 by @daniel-lxs)
- Consolidate getState calls in resolveWebviewView (PR #11320 by @0xMink)
- Clean up repo-facing mode rules (PR #11410 by @hannesrudolph)
- Implement ModelMessage storage layer with AI SDK response messages (PR #11409 by @daniel-lxs)
- Extract translation and merge resolver modes into reusable skills (PR #11215 by @app/roomote)
- Add blog section with initial posts to roocode.com (PR #11127 by @app/roomote)
- Replace Roomote Control with Linear Integration in cloud features grid (PR #11280 by @app/roomote)
- Add IPC query handlers for commands, modes, and models (PR #11279 by @cte)
- Add stdin stream mode for the CLI (PR #11476 by @cte)
- Make CLI auto-approve by default with require-approval opt-in (PR #11424 by @cte)
- Update CLI default model from Opus 4.5 to Opus 4.6 (PR #11273 by @app/roomote)
- Add linux-arm64 support for the Roo CLI (PR #11314 by @cte)
- CLI release: v0.0.51 (PR #11274 by @cte)
- CLI release: v0.0.52 (PR #11324 by @cte)
- CLI release: v0.0.53 (PR #11425 by @cte)
- CLI release: v0.0.54 (PR #11477 by @cte)

## [cli-v0.0.55] - 2026-02-17

## What's New


### Fixed

- **Stdin Stream Mode**: Fixed issue where new tasks were incorrectly being created in stdin-prompt-stream mode. The mode now properly reuses the existing task for subsequent prompts instead of creating new tasks.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.0.55 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
f208607adbff5c1e935c7068e997a5136508cc0768a587b6cb27c973cb81753b  roo-cli-darwin-arm64.tar.gz
21ec62755e6c8741ee8e18cb185f7d8c0c517ebe2a71110ed287317fa55cd7e7  roo-cli-linux-arm64.tar.gz
ee7c25fd22b9acb66f666f0cab2c30579ee1015b1485cde209a65cae71536540  roo-cli-linux-x64.tar.gz
```

## [cli-v0.0.54] - 2026-02-15

## What's New


### Added

- **Stdin Stream Mode**: New `stdin-prompt-stream` mode that reads prompts from stdin, allowing batch processing and piping multiple tasks. Each line of stdin is processed as a separate prompt with streaming JSON output. See [`stdin-prompt-stream.ts`](src/ui/stdin-prompt-stream.ts) for implementation.

### Fixed

- Fixed JSON emitter state not being cleared between tasks in stdin-prompt-stream mode
- Fixed inconsistent user role for prompt echo partials in stream-json mode

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

Or install a specific version:
```bash
ROO_VERSION=0.0.54 curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh | sh
```

## Requirements

- Node.js 20 or higher
- macOS Apple Silicon (M1/M2/M3/M4), Linux x64, or Linux ARM64

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
- `roo-cli-linux-arm64.tar.gz` - Linux ARM64

## Checksums

```
510b05e41a799ea3c1aeaf63b3f8ef0e083d1b03a14d2a6c1160ba0d9504bb6b  roo-cli-darwin-arm64.tar.gz
17bfb44f7295e45217e9cec1fda864f4a097d4551b7eba0a891f9e6a7e9bb698  roo-cli-linux-arm64.tar.gz
0b0e7f57d02b00b87f6fa315431b7a860b3e88ef99e65a8e736bd098659a398b  roo-cli-linux-x64.tar.gz
```


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

