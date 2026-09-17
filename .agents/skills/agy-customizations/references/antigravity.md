# Google Antigravity (AGY) Customization Guide

## Overview
Google Antigravity is a multimodal agentic IDE and CLI environment. It features deep integration with Gemini models, native lifecycle hooks, lazy and eager MCP tool loading, and built-in subagent orchestration.

---

## 1. Operating Instructions & Rules Hierarchy

### Rules Discovery
1. **Workspace Root:** `GEMINI.md` in repository root.
2. **Dedicated Rule Directory:** `.agents/rules/*.md` (e.g., `adversarial-auditing-and-prompt-neutrality.md`).
3. **Hierarchical Directory Rules:** Nested `GEMINI.md` files in subdirectories.
4. **Global Rules:** `~/.gemini/config/` (machine-wide).

### Rule Activation Modes
- **Always On:** Rules loaded into context unconditionally.
- **Model Decision:** Rules loaded progressively when the model determines relevance based on task context.

---

## 2. Skills Discovery & Precedence

Antigravity resolves skills through a strict 4-tier precedence hierarchy:
1. **Workspace Project (Priority 1):** `.agents/skills/<name>/SKILL.md` (Overrides all lower levels).
2. **Declared Project Configs (Priority 2):** Listed in workspace `skills.json` or `plugins.json`.
3. **Global User Config (Priority 3):** `~/.gemini/config/skills/`.
4. **Built-in System Defaults (Priority 4):** Bundled with Antigravity in `~/.gemini/antigravity/builtin/skills/`.

---

## 3. Lifecycle Hooks Architecture (`hooks.json`)

Hooks execute shell commands at defined moments in the agent loop. Configured in `.agents/hooks.json` or global configuration.

### Supported Events
- `PreToolUse`: Triggers before a tool call executes. Can block execution if the script exits with non-zero code.
- `PostToolUse`: Triggers immediately after a tool finishes. Ideal for automated linting, formatting, or test verification.
- `PreInvocation`: Triggers before the agent processes a new user message.
- `PostInvocation`: Triggers after the agent completes a response turn.

### Syntax Example
```json
{
  "linter-guard": {
    "enabled": true,
    "PostToolUse": [
      {
        "matcher": "replace_file_content",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -File ./scripts/lint-check.ps1",
            "timeout": 15
          }
        ]
      }
    ]
  },
  "safety-firewall": {
    "PreToolUse": [
      {
        "matcher": "run_command",
        "hooks": [
          {
            "command": "powershell -File ./scripts/block-destructive-commands.ps1"
          }
        ]
      }
    ]
  }
}
```

---

## 4. MCP Servers in Antigravity

Antigravity supports both **Eager** and **Lazy** MCP tools:
- **Eager Tools:** Schema loaded directly into the model's native tool registry (e.g., `mcp_<server>_<tool>`).
- **Lazy Tools:** Schema stored on disk in `~/.gemini/antigravity/mcp/<serverName>/<toolName>.json`. Loaded dynamically via `call_mcp_tool` when needed, saving context tokens.

### Configuration
Managed in `~/.gemini/antigravity/mcp/` or project `mcp_config.json`:
```json
{
  "mcpServers": {
    "composio": {
      "command": "npx",
      "args": ["-y", "composio-mcp"],
      "env": {
        "COMPOSIO_API_KEY": "${COMPOSIO_API_KEY}"
      }
    }
  }
}
```

---

## 5. Native Subagent System

Antigravity provides first-class subagent orchestration via:
- `invoke_subagent`: Spawns subagents (`self`, `research`, or custom types) with their own prompt and isolated context.
- `define_subagent`: Registers custom dynamic subagent types during a session with custom toolsets.
- `manage_subagents`: Inspects live subagent state, sends inputs, or terminates agents.
- `send_message`: Asynchronous message dispatch between parent and subagents.
