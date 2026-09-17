# Cross-Runtime Parity & Triad Synchronization Guide

## The Triad Operational Model

In EmpathoAiOS, three autonomous engines operate on the same codebase:
1. **Antigravity (Gemini)**
2. **OpenAI Codex (OpenAI)**
3. **Claude Code (Anthropic)**

To prevent drift, broken paths, and divergent behaviors, all customizations must follow the **Triad Synchronization Standard**.

---

## 1. Single Source of Truth (SSOT) Architecture

```
                      +-------------------+
                      |  agents_guide.md  |  <--- Single Source of Truth
                      +-------------------+
                                ^
         +----------------------+----------------------+
         |                      |                      |
  +--------------+       +--------------+       +--------------+
  |  GEMINI.md   |       |  AGENTS.md   |       |  CLAUDE.md   |
  | (Antigravity)|       |   (Codex)    |       | (Claude Code)|
  +--------------+       +--------------+       +--------------+
```

### Constitutional Rule
- Never duplicate business rules, tone instructions, or operating frameworks across `GEMINI.md`, `AGENTS.md`, and `CLAUDE.md`.
- Keep these three files as lightweight entrypoints that point directly to `agents_guide.md`.
- Protect all four files under strict immutability governance: no modifications without explicit user authorization.

---

## 2. The Universal Skill Authoring Standard (WOR-T)

When building a new skill:
1. **Canonical Source:** Always author the original skill inside `.agents/skills/<skill-name>/SKILL.md`.
2. **Claude Mirror:** Replicate the folder to `.claude/skills/<skill-name>/`.
3. **Trigger Density:** Use trigger words that match how each runtime discovers skills:
   - Antigravity: Exact verb and task matching.
   - Claude: Task intent and slash command invocation.
   - Codex: Step-by-step problem statements and domain tags.

### Universal Directory Layout
```
.agents/skills/<skill-name>/
├── SKILL.md                 # Universal instructions (Antigravity & Codex)
├── scripts/                 # Reusable scripts (PowerShell / Python / Bash)
├── references/              # Detailed background material
└── examples/                # Verified input/output cases

.claude/skills/<skill-name>/
└── SKILL.md                 # Mirror for Claude Code native discovery
```

---

## 3. Tool Calling & Shell Command Compatibility

| Runtime Requirement | PowerShell (Windows) | Bash (Linux/macOS) | Universal Strategy |
|:---|:---|:---|:---|
| Path separators | `\` or `/` | `/` | Use forward slashes `/` in all documentation and relative paths. |
| Line endings | CRLF | LF | Configure Git `.gitattributes` to handle checkout normalization. |
| File viewing | `view_file` (Antigravity) | `cat` / `head` (Codex/Claude) | Document tool-agnostic file inspection steps in skills. |
| Python execution | `python` | `python3` | Use `python` with virtual environment activation in scripts. |

---

## 4. MCP Parity Mapping

When integrating a new MCP tool into the workspace:

1. **Antigravity Registration:** Add to `~/.gemini/antigravity/mcp/` or `mcp_config.json`.
2. **Claude Code Registration:** Execute `claude mcp add <name> -- <command>` or update `~/.claude.json`.
3. **Codex Registration:** Ensure credentials and entrypoint scripts are registered in `.env` and `connections.md`.

---

## 5. Pre-Deployment Parity Audit Checklist

Before considering any skill or rule ready for production:
- [ ] Frontmatter YAML parses cleanly with `name` and `description`.
- [ ] Description contains concrete trigger conditions and negative boundaries.
- [ ] Canonical copy in `.agents/skills/` matches mirror in `.claude/skills/`.
- [ ] Registered in `references/skill-routing.md`.
- [ ] No hardcoded operating-system absolute paths (use relative or dynamic resolution).
- [ ] Read-only tests pass across all active runtimes.
