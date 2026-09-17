# OpenAI Codex & AIOS Customization Guide

## Overview
OpenAI Codex operates as an autonomous agentic programming engine, interpreting repository guidelines, executing terminal commands, evaluating test suites, and orchestrating multi-step software tasks.

---

## 1. System Memory & Instructions (`AGENTS.md`)

### Loading Hierarchy
- **Repository Root:** Codex automatically ingests `AGENTS.md` located at the root of the project as its primary system prompt and standing operational doctrine.
- **Subdirectory Hierarchies:** When modifying or reasoning about code within a specific subdirectory, Codex loads nested `AGENTS.md` files to inherit folder-specific conventions (e.g., `frontend/AGENTS.md` vs. `backend/AGENTS.md`).
- **Delegation Standard:** In EmpathoAiOS, `AGENTS.md` establishes constitutional immutability and delegates execution doctrine directly to `agents_guide.md`.

### Mandatory Format
- Markdown with clear headers (`#`, `##`).
- Imperative, enforceable instructions (*"You MUST", "PROHIBITED", "ALWAYS"*).
- Grounding in verifiable evidence before assertions.

---

## 2. Skills Discovery in Codex (`.agents/skills/`)

Codex natively discovers and executes skills located in `.agents/skills/`.

### Directory Layout
```
.agents/skills/<skill-name>/
├── SKILL.md                 # Primary instructions & execution contract
├── scripts/                 # Python / Shell automation scripts
├── references/              # Detailed background docs
└── examples/                # Verified input/output patterns
```

### Frontmatter Standard
Codex parses YAML frontmatter to index skill metadata:
```yaml
---
name: skill-identifier
description: Exact triggers and scope. When Codex receives a task matching this description, it reads SKILL.md.
---
```

### Progressive Disclosure Protocol
- Codex scans available skills at startup using the frontmatter `description`.
- Codex does not preload the full text of all skills into context. It performs targeted reads (`view_file` or cat) only when a skill's trigger matches the task intent.

---

## 3. Automation Scripts & CLI Tool Integration

Codex excels at executing local Python, PowerShell, and Bash scripts:
- **Scripts Directory:** Place deterministic utilities in `scripts/` (e.g., `scripts/aios-health-check.ps1`, `scripts/build-assets.py`).
- **Execution Rules:**
  - Prefer non-interactive commands.
  - Set timeouts and capture exit codes.
  - Never prompt for stdin if arguments can be passed via flags.

---

## 4. Subagent & Parallel Agent Orchestration

When Codex handles complex, multi-component refactors:
1. **Isolation:** Independent tasks run without shared mutable state.
2. **Subagent Instructions:** Subagents inherit the parent repository's `AGENTS.md` and can be pointed to specific skill playbooks.
3. **Verification Before Completion:** Every subagent must present tangible test/execution evidence before its findings are merged.

---

## 5. Environment & Credentials Governance

- Store sensitive API keys in `.env` (gitignored).
- Codex accesses environment variables through standard shell inheritance.
- Never hardcode keys in `AGENTS.md`, scripts, or skill documentation.
