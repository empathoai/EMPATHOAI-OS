# EmpathoAiOS Skill Routing

> Routing reference for project-local skills. Skills are model-invoked by default unless their frontmatter explicitly disables model invocation.

## Routing order

1. Read the task intent and applicable project instructions.
2. Load the smallest set of skills whose trigger conditions match.
3. Resolve overlapping skills using the precedence rules below.
4. Load linked references only when the selected skill requires them.
5. Verify the skill's completion criteria before reporting success.

## Automatic activation map

| Skill | Activate when | Precedence / boundary |
|---|---|---|
| `using-superpowers` | Any new coding-agent conversation or software task needs workflow discovery. | Bootstrap/meta skill. It routes the development workflow; it does not replace task-specific skills. |
| `grill-me` | A decision, ambiguity, plan, design, architecture, or context interview needs challenge and shared understanding. | Use before structural action when unresolved decisions remain. |
| `brainstorming` | A software feature, behavior change, or creative implementation needs intent and design refinement before code. | Use before `writing-plans`; do not use for a factual lookup or a settled mechanical edit. |
| `writing-plans` | A multi-step implementation has an approved specification or design. | Use before implementation; its output becomes input to `executing-plans` or `subagent-driven-development`. |
| `executing-plans` | A written plan is being executed in a separate session with checkpoints. | Use instead of ad-hoc implementation when a plan already exists. |
| `subagent-driven-development` | An approved plan contains independent implementation tasks in the current session. | Use when delegation improves throughput; preserve review gates. |
| `dispatching-parallel-agents` | Two or more independent tasks can run without shared state or ordering dependencies. | Never parallelize dependent or conflicting writes. |
| `using-git-worktrees` | Feature work or plan execution needs workspace isolation. | Use before implementation when isolation is needed; do not create worktrees for simple read-only or single-file tasks. |
| `test-driven-development` | Implementing a feature or bugfix before production code is written. | Red → green → refactor; use with `systematic-debugging` only when the task is also a defect. |
| `systematic-debugging` | A bug, test failure, regression, or unexpected behavior is observed. | Understand and reproduce before fixing; do not jump directly to a patch. |
| `verification-before-completion` | About to claim completion, success, a fix, passing tests, commit readiness, or PR readiness. | Final evidence gate for every implementation workflow. |
| `requesting-code-review` | A task or feature is complete enough for review or before merging. | Use before integration; review blocks completion when critical issues remain. |
| `receiving-code-review` | Code-review feedback is received and must be evaluated or implemented. | Verify feedback technically; do not agree or apply blindly. |
| `finishing-a-development-branch` | Implementation and verification are complete and branch integration must be decided. | Final branch workflow; never assume merge or commit without authorization. |
| `writing-for-agents` | Creating or editing skills, `AGENTS.md`, `CLAUDE.md`, agent-facing docs, or routing pointers. | Use before writing agent-consumed instructions; apply progressive disclosure and completion criteria. |
| `writing-skills` | Creating, editing, or validating a skill before deployment. | Use with `writing-for-agents`; preserve skill-specific frontmatter and test activation. |
| `audit` | Auditing AIOS reliability, routing, freshness, skill compatibility, migration readiness, or Four Cs. | Read-only toward inspected systems except the dated audit report it saves. |
| `link` | Adding a project, file, folder, or important source to AIOS routing. | Use for routing-only changes; do not copy source content unnecessarily. |
| `onboard` | Initial AIOS setup, intake, or refreshing the Day-1 file set after intake changes. | Use for onboarding, not incremental context interviews. |
| `level-up` | Closing one verified AIOS gap or selecting and shipping one useful workflow improvement. | Use after audit evidence identifies a bounded improvement. |
| `3d-brain` | Building or updating the interactive AIOS knowledge globe. | Keep generated app/config separate from canonical context. |
| `impeccable` | Designing, critiquing, auditing, polishing, or implementing frontend/UI/UX/HTML/CSS/design-system work. | Use for visual surfaces; combine with `writing-for-agents` only when writing agent instructions, not ordinary UI copy. |

## Overlap rules

- `grill-me` resolves unsettled decisions; `brainstorming` refines an approved software/design problem. Use both only when both conditions are real.
- `brainstorming` precedes `writing-plans`; `writing-plans` precedes implementation.
- `test-driven-development` governs new behavior; `systematic-debugging` governs observed failure.
- `requesting-code-review` precedes `finishing-a-development-branch`; `verification-before-completion` gates both.
- `writing-for-agents` and `writing-skills` govern agent-facing documents; `impeccable` governs UI-facing documents and interfaces.
- `audit` verifies routing and compatibility; it does not repair the system as a side effect.
- `onboard`, `link`, `level-up`, and `3d-brain` are specialized workflows and should not be loaded for unrelated tasks.

## Context discipline

Do not load every skill for every turn. Skill files are discoverable through their descriptions; full bodies and references load only after a trigger matches. Keep this routing file as the single source of truth for overlaps and do not duplicate the full descriptions in `AGENTS.md` or `CLAUDE.md`.
