# Plan: Separate EmpathoAiOS Context from NEXUS Collaboration Context

## Goal

Define and implement a clear context boundary so using EmpathoAiOS through Claude Code, Codex, or another interface can evolve the OS without silently changing NEXUS's personal relationship with Alex.

## Current context / assumptions

- `aios-intake.md` is currently the source of truth for `/onboard` and is intended to scaffold the OS.
- `README.md` describes the Four Cs architecture and identifies `context/` as business and personal operating context.
- `AGENTS.md` and `CLAUDE.md` are shared operating manuals and currently contain personalization placeholders plus standing instructions.
- Hermes has a separate persistent memory/context layer that is not stored in this repository. That layer should not be treated as an automatic mirror of repository content.
- The repository must remain usable outside Hermes, including in Claude Code and Codex.
- Existing user-authored changes must be preserved. No commit, push, or broad refactor is part of this plan.
- The desired behavior is: OS content may be consumed by any supported agent; only explicitly approved, stable collaboration facts may be copied into NEXUS memory.

## Architecture / proposed approach

Create two explicit information domains: the **OS domain** in the repository, which is portable and operational, and the **NEXUS domain**, which is private collaboration context managed by Hermes. Add a repository policy and intake classification that mark each fact as portable OS context, NEXUS-only context, or temporary/unconfirmed material. Make `/onboard`, `/grill-me`, and future context updates write only to the OS domain unless Alex explicitly requests a NEXUS memory update.

Use append-only provenance for cross-domain promotion: every promoted fact must record its source file, confirmation date, and intended scope. Do not synchronize the domains automatically or copy credentials, sensitive personal details, or transient brainstorm material.

## Step-by-step tasks

### 1. Document the context boundary and data-flow rules

Create `docs/context-boundary.md` with:

- Definitions of `OS context`, `NEXUS context`, and `temporary material`.
- A one-way default flow: source material → OS context; no automatic OS context → NEXUS memory.
- The explicit promotion workflow: propose → Alex confirms → record provenance → update NEXUS memory manually/through an approved Hermes action.
- Rules for conflicts, deletions, stale facts, secrets, and sensitive information.
- A decision table showing where identity, business facts, voice samples, priorities, connections, preferences, brainstorms, and credentials belong.
- Examples for Claude Code, Codex, and Hermes usage.

Verification command:

```bash
python -c "from pathlib import Path; p=Path('docs/context-boundary.md'); assert p.exists(); text=p.read_text(encoding='utf-8'); assert 'NEXUS' in text and 'OS context' in text and 'provenance' in text; print('context boundary documentation: PASS')"
```

Expected output:

```text
context boundary documentation: PASS
```

Commit after review:

```bash
git add docs/context-boundary.md && git commit -m "Document OS and NEXUS context boundary"
```

### 2. Add an explicit classification schema to the intake

Update `aios-intake.md` without increasing the seven-question cap. Add a short section before Q1 named `Context handling` that tells Alex to answer the intake for the portable OS and identifies fields that should not be copied into NEXUS memory automatically. Add a classification note after Q7 with these labels:

- `OS`: safe and useful for the portable EmpathoAiOS.
- `NEXUS`: private collaboration preference or relationship context; requires explicit confirmation before saving outside the repository.
- `TEMPORARY`: tentative, sensitive, or time-bounded material; do not promote automatically.

Keep the existing questions and answer placeholders intact.

Verification commands:

```bash
python -c "from pathlib import Path; p=Path('aios-intake.md'); t=p.read_text(encoding='utf-8'); assert t.count('## Q') == 7; assert all(x in t for x in ('OS', 'NEXUS', 'TEMPORARY')); print('intake classification: PASS')"
git diff --check
```

Expected output:

```text
intake classification: PASS
```

Commit after review:

```bash
git add aios-intake.md && git commit -m "Classify intake facts by context scope"
```

### 3. Add routing instructions to both operating manuals

Update `AGENTS.md` and `CLAUDE.md` together with a short section named `Context boundary` that states:

- Repository files are the portable OS source of truth.
- An agent may read repository context to perform OS work.
- An agent must not claim that repository content changed NEXUS memory.
- NEXUS-only memory changes require an explicit request from Alex.
- New facts should be labeled `confirmed`, `tentative`, or `temporary` and should include a source path when written to the repository.
- Secrets and credentials must never be placed in intake, context pages, brainstorms, or manuals.

Do not alter the existing voice, attribution, or skill descriptions.

Verification commands:

```bash
python -c "from pathlib import Path; a=Path('AGENTS.md').read_text(encoding='utf-8'); c=Path('CLAUDE.md').read_text(encoding='utf-8'); assert a == c; assert 'Context boundary' in a; print('manual parity and boundary rules: PASS')"
git diff --check
```

Expected output:

```text
manual parity and boundary rules: PASS
```

Commit after review:

```bash
git add AGENTS.md CLAUDE.md && git commit -m "Add context boundary to operating manuals"
```

### 4. Define provenance for promoted facts

Create `context/provenance.md` as a template, not a dump of personal data. Include a table with these exact columns:

```text
| Fact ID | Fact summary | Scope | Source path | Status | Confirmed on | Review by | Notes |
|---|---|---|---|---|---|---|---|
```

Document allowed `Scope` values (`OS`, `NEXUS`, `BOTH`) and require `BOTH` to have explicit confirmation from Alex. Document allowed `Status` values (`confirmed`, `tentative`, `temporary`, `retired`). Leave the table empty except for one clearly marked example row using fictional data, or leave it empty if the project convention rejects examples.

Verification command:

```bash
python -c "from pathlib import Path; t=Path('context/provenance.md').read_text(encoding='utf-8'); assert all(x in t for x in ('Fact ID', 'Source path', 'BOTH', 'confirmed', 'retired')); print('provenance template: PASS')"
```

Expected output:

```text
provenance template: PASS
```

Commit after review:

```bash
git add context/provenance.md && git commit -m "Add provenance template for promoted context"
```

### 5. Add a regression check for accidental domain coupling

Create `scripts/check-context-boundary.py` using only Python's standard library. It must:

- Read `aios-intake.md`, `AGENTS.md`, `CLAUDE.md`, and `docs/context-boundary.md` as UTF-8.
- Fail if any of those files contain common credential markers such as `OPENAI_API_KEY=`, `ANTHROPIC_API_KEY=`, `GOOGLE_APPLICATION_CREDENTIALS=`, or `password=`.
- Fail if `AGENTS.md` and `CLAUDE.md` differ.
- Fail if the intake no longer contains exactly seven `## Q` headings.
- Fail if the boundary document does not state that NEXUS updates require explicit confirmation.
- Print one `PASS` line and exit 0 on success; print a useful error and exit 1 on failure.

TDD sequence for this task:

1. Add `scripts/test-check-context-boundary.py` with tests for the seven-question count, manual parity, explicit confirmation rule, and credential-marker rejection. Run:

   ```bash
   python -m unittest scripts/test-check-context-boundary.py
   ```

   Expected initial result: at least one failure because `scripts/check-context-boundary.py` does not exist yet.

2. Implement `scripts/check-context-boundary.py` minimally until the tests pass.

3. Run:

   ```bash
   python -m unittest scripts/test-check-context-boundary.py
   python scripts/check-context-boundary.py
   git diff --check
   ```

   Expected result: all tests pass, followed by a `context boundary: PASS` line.

4. Commit:

   ```bash
   git add scripts/check-context-boundary.py scripts/test-check-context-boundary.py && git commit -m "Add context boundary regression check"
   ```

### 6. Update the README with the user-facing rule

Add a concise subsection to `README.md` near the existing context/Four Cs explanation titled `Portable OS context vs. NEXUS context`. State that:

- EmpathoAiOS is portable across supported assistants.
- Repository context is not automatically Hermes memory.
- Explicit promotion and provenance are required for facts intended to affect the NEXUS relationship.
- The canonical policy is `docs/context-boundary.md`.

Do not rewrite the README or change the Four Cs definitions.

Verification commands:

```bash
python scripts/check-context-boundary.py
git diff --check
git status --short
```

Expected output includes:

```text
context boundary: PASS
```

Commit after review:

```bash
git add README.md && git commit -m "Explain portable and NEXUS context"
```

### 7. Run the complete validation and perform a manual review

Run:

```bash
python -m unittest scripts/test-check-context-boundary.py
python scripts/check-context-boundary.py
git diff --check
git status --short
```

Expected result:

- Unit tests report `OK`.
- The boundary checker reports `context boundary: PASS`.
- `git diff --check` produces no output and exit code 0.
- `git status --short` shows only the intended files, unless prior user changes are present.

Manually review that no existing user changes were overwritten, no credentials were added, and no document claims that NEXUS memory is synchronized automatically.

## Tests / validation

- Documentation and intake checks must pass as exact commands in tasks 1–4.
- The regression checker must be developed with the TDD sequence in task 5: failing tests first, minimal implementation second, passing tests third.
- `AGENTS.md` and `CLAUDE.md` must remain byte-for-byte identical after their shared update.
- The intake must retain exactly seven question headings.
- `git diff --check` must pass before completion.
- Do not test or modify Hermes profile memory as part of the repository change. Any NEXUS-memory update must be a separate, explicit, user-authorized action after the repository policy is accepted.

## Risks, tradeoffs, and open questions

- **Risk: duplicated context drifts.** Mitigation: keep the repository as the OS source of truth and require provenance for any fact promoted to NEXUS.
- **Risk: over-classification slows normal work.** Mitigation: classify only durable facts and sensitive boundaries; leave routine OS notes in the OS domain.
- **Risk: a future skill ignores the policy.** Mitigation: add the regression checker and update both operating manuals together.
- **Tradeoff: no automatic two-way synchronization.** This is intentional because automatic synchronization could change the personal assistant relationship without Alex's consent.
- **Tradeoff: `BOTH` facts require confirmation.** This adds one step but prevents accidental leakage and preserves portability.
- **Open question:** Should `context/` be entirely portable, or should the project later introduce a gitignored `context-private/` directory for OS-local sensitive material? Default recommendation: do not add it until a concrete use case appears.
- **Open question:** Should NEXUS memory promotion be recorded through a dedicated Hermes command or remain a deliberate conversational action? Decide after the boundary documents are accepted; do not couple the repository to Hermes internals prematurely.
