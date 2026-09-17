# Claude Code Customization Guide (Anthropic)

## Overview
Claude Code is Anthropic's agentic CLI tool. It operates directly in the terminal, reading project instructions, executing shell commands, managing files, and interfacing with external tools via MCP.

---

## 1. Project Memory & Instruction Files (`CLAUDE.md`)

### Loading & Discovery Hierarchy
- **Root Project File:** Upon startup in any directory, Claude Code automatically searches for and reads `CLAUDE.md` in the current working directory and walks up to the Git repository root.
- **Hierarchical Overrides:** Subdirectory `CLAUDE.md` files are loaded dynamically when Claude works inside or touches files within that specific directory tree.
- **Global Configuration:** User-level instructions can reside in `~/.claude/CLAUDE.md` across all projects.

### Best Practices for `CLAUDE.md`
- Keep it concise and operational. Claude Code prioritizes concrete rules, build commands, test commands, code style rules, and file routing.
- In EmpathoAiOS, `CLAUDE.md` acts as a constitutional pointer delegating standing operating guidance to `agents_guide.md`.

---

## 2. Custom Slash Commands (`.claude/commands/`)

Claude Code allows creating reusable custom slash commands as Markdown files inside `.claude/commands/`.

### Directory Structure
```
.claude/
└── commands/
    ├── test-run.md        # Invoked with /test-run
    ├── audit.md           # Invoked with /audit
    └── deploy.md          # Invoked with /deploy
```

### Command Syntax & Argument Handling
Inside `.claude/commands/<command-name>.md`:
```markdown
---
description: Run targeted unit tests and report failures
---

Execute the test suite for $ARGUMENTS using pytest.
If any test fails, run a systematic debugging pass and explain the root cause.
```

- `$ARGUMENTS`: Captures all text typed after the slash command (e.g., `/test-run auth_service`).
- `$1`, `$2`: Captures positional arguments.

---

## 3. Skills Architecture (`.claude/skills/`)

Claude Code discovers skills placed in `.claude/skills/<skill-name>/SKILL.md`.

### Frontmatter Schema
```yaml
---
name: skill-name
description: Trigger-rich description explaining when Claude should activate this skill.
---
```

### Progressive Disclosure
Claude Code reads the `name` and `description` to decide whether to load the full skill body. Detailed reference docs belong in a `references/` subfolder inside the skill folder.

---

## 4. MCP (Model Context Protocol) in Claude Code

Claude Code has native, first-class MCP management via the CLI and configuration files.

### Adding MCP Servers via CLI
```bash
# Add a stdio MCP server (e.g., Composio or custom tool)
claude mcp add composio -- npx -y composio-mcp

# Add an SQLite database inspector
claude mcp add db-tools -- python -m sqlite_mcp --db ./data/app.db
```

### Configuration Files
- **Global User Config:** `~/.claude.json`
- **Project-Level Config:** `.claude/mcp.json` or project settings.

Structure:
```json
{
  "mcpServers": {
    "composio": {
      "command": "npx",
      "args": ["-y", "composio-mcp"],
      "env": {
        "COMPOSIO_API_KEY": "..."
      }
    }
  }
}
```

### Managing MCP Servers
```bash
claude mcp list       # List active servers
claude mcp remove <id> # Remove server
claude mcp status     # Check server connectivity and active tools
```

---

## 5. File Exclusion (`.claudeignore`)

To prevent Claude Code from reading huge files, logs, node_modules, or sensitive credentials, create a `.claudeignore` file in the project root:
```
node_modules/
dist/
build/
*.log
.env*
archives/
```

---

## 6. Permission & Safety Governance

Claude Code can be configured to auto-approve safe operations or prompt for dangerous ones:
- In `~/.claude.json`:
  ```json
  {
    "autoApprove": [
      "ViewFile",
      "ListDirectory"
    ]
  }
  ```
- Command-line flags:
  `claude --dangerously-skip-permissions` (use only in isolated containers or dev environments).
