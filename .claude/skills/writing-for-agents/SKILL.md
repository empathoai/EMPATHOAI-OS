---
name: writing-for-agents
description: Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.
---

Reference for writing any document an agent consumes: a skill, an `AGENTS.md` / `CLAUDE.md`, a doc reached by a pointer. The packaging differs; the writing does not: the same levers make each one predictable, since the agent takes the same process every run rather than producing the same output.

When the document you're writing is a skill, read [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) for frontmatter, invocation choice, and router skills.

## Context pointers

A **context pointer** is a reference held in the agent's context that names some out-of-context material and encodes the condition for reaching it. A skill's description is one; a line in `AGENTS.md` naming a doc is the same object. The pointer's wording, not its target, decides when the agent reaches the material, and how reliably. A must-have target behind a weakly worded pointer is a variance bug: sharpen the wording first, and inline the material only if sharpening fails.

A pointer does two jobs: state what the material is, and list the branches that should trigger reaching it. Every word of an always-loaded pointer costs on every turn, so prune pointers aggressively.

## The two loads

Every document and pointer spends one of two budgets:

- **Context load:** always-loaded material in the agent's window.
- **Cognitive load:** the human's burden of knowing which documents exist and when to reach for each.

Material reached only through a pointer escapes context load at the price of the pointer's own line.

## Information hierarchy

Use this hierarchy:

1. **In-file step:** ordered actions the agent performs.
2. **In-file reference:** rules consulted on demand.
3. **Disclosed reference:** separate material reached through a pointer.

Use progressive disclosure to keep the main file legible. Co-locate a concept's definition, rules, and caveats. Split by real branches or sequence, not by arbitrary file size.

## Steps and completion criteria

Every step ends with a checkable, exhaustive completion criterion. Vague criteria invite premature completion. Sharpen the criterion before hiding later steps behind another file or handoff.

## Leading words

Prefer established terms that activate useful prior knowledge. Define new terms only when necessary. Use concise leading words to replace repeated explanations. State positive target behavior; avoid relying on negations as the main control mechanism.

## Pruning

Keep each meaning in one source of truth. Treat the environment as a source of truth and avoid stale copies of one-file, one-command facts. Remove irrelevant lines, sediment, and no-ops. Shorter, sharper documents are easier to follow and maintain.
