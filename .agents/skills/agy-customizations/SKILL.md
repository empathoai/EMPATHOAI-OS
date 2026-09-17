---
name: agy-customizations
description: >-
  Comprehensive guide and operational doctrine for the Unified AI Customization System
  across Google Antigravity, OpenAI Codex, and Anthropic Claude Code (The Power Triad).
  Use whenever creating, modifying, debugging, or synchronizing rules, skills, MCP servers,
  hooks, custom commands, or subagents with 100% cross-runtime parity.
---

# Unified AI Customization System (The Power Triad: Antigravity, Codex & Claude)

## Executive Summary

EmpathoAiOS operates on a **Power Triad** of AI development runtimes:
* **Google Antigravity (AGY / Gemini):** Deep filesystem IDE integration, fast multimodal reasoning, native subagents, and lazy MCP tools.
* **OpenAI Codex (Codex CLI / AIOS):** High-precision code generation, autonomous terminal execution, and strict instruction following.
* **Anthropic Claude Code (Claude CLI):** Terminal-native agentic development, interactive CLI loops, custom slash commands, and first-class MCP management.

This skill provides the comprehensive architecture, loading precedence, configuration schemas, and synchronization runbooks to author customizations with **100% Cross-Runtime Parity**.

---

## 1. Quick Navigation to In-Depth Engine References

Detailed technical documentation for each engine is modularized in `references/`:

* **[Claude Code Complete Customization Guide](references/claude-code.md):** `CLAUDE.md` memory hierarchy, `.claude/commands/` custom slash commands, `.claudeignore`, MCP management (`claude mcp add` / `~/.claude.json`), and safety settings.
* **[OpenAI Codex & AIOS Customization Guide](references/codex.md):** `AGENTS.md` system prompts, `.agents/skills/` execution, CLI scripting standards, multi-agent coordination, and environment variables.
* **[Google Antigravity Customization Guide](references/antigravity.md):** Rules discovery (`GEMINI.md`, `.agents/rules/*.md`), 4-tier precedence hierarchy, `hooks.json` lifecycle specification (`PreToolUse`, `PostToolUse`), MCP tool registries, and subagents.
* **[Cross-Runtime Parity & Synchronization Guide](references/cross-runtime-parity.md):** The "Write Once, Run in the Triad" (WOR-T) doctrine, SSOT delegation, tool-calling compatibility, and pre-deployment checklists.

---

## 2. Master Comparison Matrix: The Power Triad

```
+-------------------+------------------------------+------------------------------+-------------------------------+
| DIMENSION         | GOOGLE ANTIGRAVITY (Gemini)  | OPENAI CODEX (OpenAI / AIOS) | ANTHROPIC CLAUDE CODE         |
+-------------------+------------------------------+------------------------------+-------------------------------+
| Root Instruction  | GEMINI.md                    | AGENTS.md                    | CLAUDE.md                     |
| SSOT Pointer      | -> delegates to agents_guide | -> delegates to agents_guide | -> delegates to agents_guide  |
+-------------------+------------------------------+------------------------------+-------------------------------+
| Local / Scoped    | .agents/rules/*.md           | Nested AGENTS.md             | Nested CLAUDE.md              |
| Rules             | and nested GEMINI.md         | in directories               | in directories                |
+-------------------+------------------------------+------------------------------+-------------------------------+
| Skills Directory  | .agents/skills/<name>/       | .agents/skills/<name>/       | .claude/skills/<name>/        |
| (Discovery Path)  | (Hierarchical workspace)     | (Standard shared path)       | (Mirrored native path)        |
+-------------------+------------------------------+------------------------------+-------------------------------+
| Skill Schema      | SKILL.md with YAML metadata: | SKILL.md with YAML metadata: | SKILL.md with YAML metadata:  |
|                   | name + description           | name + description           | name + description            |
+-------------------+------------------------------+------------------------------+-------------------------------+
| Custom Commands   | Slash commands in chat UI    | Script execution / CLI flags | .claude/commands/*.md         |
| / Shortcuts       | /<skill-name>, /goal, etc.   | via python / powershell      | with $ARGUMENTS substitution  |
+-------------------+------------------------------+------------------------------+-------------------------------+
| Lifecycle Hooks   | hooks.json                   | Shell wrapper scripts        | Native permission hooks       |
|                   | (PreToolUse, PostToolUse)    | in scripts/                  | and command settings          |
+-------------------+------------------------------+------------------------------+-------------------------------+
| MCP Tooling       | mcp_config.json &            | CLI bridges, scripts, and    | claude mcp add <server>       |
| Configuration     | ~/.gemini/antigravity/mcp/   | environment integration      | or ~/.claude.json / mcp.json  |
+-------------------+------------------------------+------------------------------+-------------------------------+
| Subagents         | Native invoke_subagent /     | Subagent runner scripts and  | Forked terminal sessions      |
| Orchestration     | define_subagent tools        | isolated execution           | or parallel CLI invocations   |
+-------------------+------------------------------+------------------------------+-------------------------------+
```

---

## 3. Precedence & Discovery Hierarchy

Understanding which file takes priority prevents subtle configuration bugs:

### In Google Antigravity
1. **Workspace Project (Priority 1 - Highest):** `.agents/skills/<name>/` or `.agents/rules/` in the project root. Overrides built-in defaults.
2. **Declared Project Configs (Priority 2):** Listed in workspace `skills.json` or `plugins.json`.
3. **Global Configuration (Priority 3):** `~/.gemini/config/`.
4. **Built-in System Defaults (Priority 4 - Lowest):** Bundled in application data.

### In Anthropic Claude Code
1. **Subdirectory `CLAUDE.md`:** When editing files inside that subfolder.
2. **Project Root `CLAUDE.md`:** Always loaded at launch.
3. **Custom Commands:** `.claude/commands/*.md` mapped directly to `/<command>`.
4. **Global `~/.claude.json` / `~/.claude/CLAUDE.md`:** Machine-wide fallback.

### In OpenAI Codex
1. **Target Subdirectory `AGENTS.md`:** Scoped context for the target package.
2. **Repository Root `AGENTS.md`:** Primary system prompt and governance.
3. **Skills Inventory:** Discovered progressively via `.agents/skills/`.

---

## 4. The 4-Step Triad Synchronization Protocol

Whenever you create a new skill, rule, or MCP integration:

1. **Step 1 (Author Canonical Skill):**
   * Create `.agents/skills/<skill-name>/SKILL.md`.
   * Add required scripts to `scripts/` and deep docs to `references/`.
2. **Step 2 (Mirror to Claude Code):**
   * Copy the skill folder to `.claude/skills/<skill-name>/`.
   * If a custom slash command is desired, add `.claude/commands/<command>.md`.
3. **Step 3 (Update Routing Index):**
   * Add the trigger condition and precedence boundary to `references/skill-routing.md`.
4. **Step 4 (Validate MCP Parity if Applicable):**
   * Ensure the tool is configured in Antigravity (`mcp_config.json` or MCP directory) and Claude Code (`~/.claude.json`).

---

## 5. Triad Troubleshooting Runbook

* **Symptom: Skill works in Antigravity but not Claude Code:**
  - Check if the mirror exists in `.claude/skills/<skill-name>/SKILL.md`.
  - Check `.claudeignore` to confirm `.claude/` is not excluded.
* **Symptom: Antigravity loads the generic factory skill instead of workspace version:**
  - Verify that the folder name inside `.agents/skills/` matches the skill `name` in YAML frontmatter exactly.
* **Symptom: Subagent or CLI tool fails on Windows PowerShell vs. Bash:**
  - Always use forward slashes `/` in file paths.
  - Avoid OS-specific shell builtins (e.g. use standard python scripts rather than bash-only pipelines).
