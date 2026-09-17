# Marketing Team Profiles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create four isolated Hermes specialist profiles whose role logic is derived from read-only OS-Marketing sources, without modifying OS-Marketing.

**Architecture:** NEXUS remains the only coordinator. Each specialist profile is an independent Hermes profile outside `F:\OS-Marketing`, with a narrow mission, explicit upstream source pointers, bounded tools, no copied credentials, and no default write access to OS-Marketing. Every profile must pass a local health check and one bounded read-only mission before the next profile is started.

**Tech Stack:** Hermes profiles, profile-local `SOUL.md`, Hermes CLI, OS-Marketing Markdown/skill sources, `F:\EmpathoKnowledge` references, local verification commands.

**Spec:** `docs/superpowers/specs/2026-09-09-marketing-team-structure-design.md`

## Global Constraints

- `F:\OS-Marketing` is read-only for this entire plan. No file, configuration, skill, agent, database, prompt, or logic in that directory may be modified.
- Profile logic must be derived from inspected OS-Marketing sources, not from invented role assumptions.
- `F:\EmpathoKnowledge` remains the durable-knowledge SSOT; profiles must use approved references and must not create a duplicate knowledge vault.
- NEXUS is the only coordinator; Alex is the final approver for strategy, budget, publication, and external side effects.
- Use the active Hermes home resolved through `$HERMES_HOME`; never hardcode another profile's home or copy NEXUS memory.
- Keep credentials in the configured secret store only. Never copy `.env.local`, tokens, OAuth files, or account data into a profile or repository document.
- Every profile returns objective, scope, inputs, evidence, output path, blockers, recommendation, and required approver.
- Treat unavailable source files, tools, integrations, credentials, or account permissions as `UNKNOWN`; do not infer availability from a registry entry.
- Stop after each task and obtain review of its test receipt before beginning the next task.

---

### Task 1: Lock the read-only source contract

**Files:**
- Read only: `F:\OS-Marketing\AGENTS.md`
- Read only: `F:\OS-Marketing\infrastructure\tools-registry.md`
- Read only: `F:\OS-Marketing\knowledge\sop-registry.md`
- Read only: `F:\OS-Marketing\.agents\agents\creative-director.md`
- Read only: `F:\OS-Marketing\.agents\agents\qa-sentinel.md`
- Read only: `F:\OS-Marketing\.agents\agents\system-architect.md`
- Read only: `F:\OS-Marketing\.agents\skills\*/SKILL.md`
- Create: `docs/superpowers/receipts/marketing-profile-source-inventory.md`

**Interfaces:**
- Consumes: The three governing registries, three existing agent definitions, and all 27 local skill definitions.
- Produces: A source inventory listing exact paths, observed file timestamps or version metadata where available, role-to-source mappings, tool dependencies, and `UNKNOWN` items. The receipt is local to `F:\EMPATHOAI_OS` and is not a copy of OS-Marketing knowledge.

- [ ] **Step 1: Re-read all source files in read-only mode and classify them**

  Classify each source as governing rule, tool/integration registry, SOP lifecycle, existing agent contract, or specialist skill. Record only operational dependency metadata and short role mappings, not duplicated playbook content.

- [ ] **Step 2: Verify the source boundary**

  Run from `F:\EMPATHOAI_OS`:

  ```bash
  python -c "from pathlib import Path; root=Path(r'F:/OS-Marketing'); required=['AGENTS.md','infrastructure/tools-registry.md','knowledge/sop-registry.md','.agents/agents']; missing=[p for p in required if not (root/p).exists()]; print('OS_MARKETING_READ_ONLY_SOURCES:', 'PASS' if not missing else 'FAIL'); print('MISSING:', missing)"
  ```

  Expected: `OS_MARKETING_READ_ONLY_SOURCES: PASS` and an empty missing list.

- [ ] **Step 3: Write the source inventory receipt**

  Include the exact source paths, the 9 tool-registry categories, the 27 skill paths, the 3 existing agents, and a dependency matrix for the four new profiles. Mark account credentials, live integrations, and unverified runtime capabilities as `UNKNOWN` until tested in the target profile.

- [ ] **Step 4: Verify the receipt and repository hygiene**

  Run:

  ```bash
  python -c "from pathlib import Path; p=Path('docs/superpowers/receipts/marketing-profile-source-inventory.md'); p.read_bytes().decode('utf-8'); text=p.read_text(encoding='utf-8'); required=['OS-Marketing','UNKNOWN','qa-sentinel','system-architect']; print('RECEIPT:', 'PASS' if all(x in text for x in required) else 'FAIL')"
  git diff --check
  ```

  Expected: `RECEIPT: PASS`; `git diff --check` returns success; no write timestamp or content change is observed under `F:\OS-Marketing`.

**Stop condition:** Do not create a profile until the source inventory receipt passes and Alex reviews it.

---

### Task 2: Create and verify Marketing Strategist

**Files:**
- Create outside OS-Marketing: `$HERMES_HOME/profiles/marketing-strategist/`
- Create: profile-local `SOUL.md` and only the minimum profile configuration required by the verified Hermes CLI workflow.
- Modify: none under `F:\OS-Marketing`.

**Interfaces:**
- Consumes: Task 1 source inventory; read-only OS-Marketing `AGENTS.md`, relevant routing skills, SOP registry, and approved EmpathoKnowledge references.
- Produces: Strategy briefs, ICP/positioning hypotheses, funnel maps, measurement frameworks, evidence tables, and recommendations routed to NEXUS.

- [ ] **Step 1: Discover the current Hermes profile commands and active home**

  Run:

  ```bash
  hermes --help
  hermes profile --help
  hermes -p marketing-strategist doctor
  ```

  If the profile does not yet exist, treat the expected missing-profile response as discovery evidence and use the documented profile-creation command from the live CLI/help output. Do not hand-edit `config.yaml`.

- [ ] **Step 2: Create the isolated profile without cloning NEXUS state**

  Set the profile's working directory and source pointers to `F:\OS-Marketing` as read-only dependencies. Grant local draft/report output only where required. Do not copy memory, sessions, credentials, `.env.local`, or OAuth state from any other profile.

- [ ] **Step 3: Write the bounded strategist role contract**

  The contract must state the mission, inputs, outputs, strategic ownership versus Alex's approval authority, mandatory evidence/provenance, `UNKNOWN` handling, no external side effects, and the NEXUS handoff schema.

- [ ] **Step 4: Run profile health verification**

  Run:

  ```bash
  hermes -p marketing-strategist profile
  hermes -p marketing-strategist doctor
  ```

  Expected: the profile resolves to its own home, reports its intended working directory and capabilities, and passes health checks without reporting copied credentials or missing required role files.

- [ ] **Step 5: Run one bounded read-only mission**

  Run a mission that asks the profile to inspect the OS-Marketing source contract and produce a local strategy-diagnostic receipt without changing any upstream file. Verify the result includes objective, sources, evidence, assumptions, blockers, recommendation, and exact output path.

- [ ] **Step 6: Verify the upstream boundary after the mission**

  Compare the source file modification timestamps or content metadata captured before and after the mission. Expected: no OS-Marketing source changed. Save the profile test receipt under `F:\EMPATHOAI_OS\docs\superpowers\receipts\`.

**Stop condition:** Alex reviews the strategist test receipt before Task 3.

---

### Task 3: Create and verify Performance / Meta Ads

**Files:**
- Create outside OS-Marketing: `$HERMES_HOME/profiles/performance-meta-ads/`
- Create: profile-local `SOUL.md` and minimum verified profile configuration.
- Modify: none under `F:\OS-Marketing`.

**Interfaces:**
- Consumes: Task 1 source inventory; read-only `meta-ads-4pi-audit`, telemetry, tools-registry, compliance, and reporting dependencies.
- Produces: Telemetry audits, 4PI findings, pacing reports, measurement-gap reports, test proposals, and investment recommendations requiring Alex approval.

- [ ] **Step 1: Create the isolated profile using the live Hermes profile workflow**

  Confirm the profile has no inherited memory, sessions, credentials, or write permissions to OS-Marketing.

- [ ] **Step 2: Write the role contract and capability boundaries**

  Explicitly prohibit unapproved ad-account mutations, budget changes, unsupported attribution claims, and direct production changes. Classify Meta credentials and live Graph API connectivity as `UNKNOWN` until verified inside this profile.

- [ ] **Step 3: Run health and bounded telemetry verification**

  Run the profile health commands and one read-only mission using an approved telemetry artifact or registry evidence. The mission must report whether live telemetry is available without attempting a write.

- [ ] **Step 4: Verify and save the test receipt**

  Confirm required evidence fields, no upstream mutations, no copied secrets, and exact blockers. Save the receipt locally and stop for review.

**Stop condition:** Alex reviews the Performance / Meta Ads receipt before Task 4.

---

### Task 4: Create and verify Creative & Scripts

**Files:**
- Create outside OS-Marketing: `$HERMES_HOME/profiles/creative-scripts/`
- Create: profile-local `SOUL.md` and minimum verified profile configuration.
- Modify: none under `F:\OS-Marketing`.

**Interfaces:**
- Consumes: Task 1 source inventory; read-only creative-director contract, Gate 0 compliance rules, 3:2:2 copy, creative-map, organic-video, humanizer, brand, and provenance dependencies.
- Produces: Creative briefs, hooks, scripts, variants, production notes, claim/proof registers, and test rationales.

- [ ] **Step 1: Create the isolated profile and source pointers**

  Point the role to OS-Marketing sources without copying their playbooks into the profile. Keep all production and publication side effects disabled by default.

- [ ] **Step 2: Write the role contract**

  Require third-person educational framing where the source rules demand it, Gate 0 compliance, claim provenance, human review for external publication, and explicit audience/funnel/channel mapping.

- [ ] **Step 3: Run health and bounded creative verification**

  Ask for a local creative brief based only on an approved strategy input and source evidence. The test must prove that the profile can identify missing proof as `UNKNOWN` and does not publish, call external APIs, or edit OS-Marketing.

- [ ] **Step 4: Verify and save the test receipt**

  Confirm source citations, compliance checks, output path, and unchanged upstream state. Stop for review.

**Stop condition:** Alex reviews the Creative & Scripts receipt before Task 5.

---

### Task 5: Create and verify Conversation & Lifecycle

**Files:**
- Create outside OS-Marketing: `$HERMES_HOME/profiles/conversation-lifecycle/`
- Create: profile-local `SOUL.md` and minimum verified profile configuration.
- Modify: none under `F:\OS-Marketing`.

**Interfaces:**
- Consumes: Task 1 source inventory; read-only GHL prompt-audit, conversational DM triage, appointment/no-show, lifecycle, compliance, and client-dossier dependencies.
- Produces: Conversation maps, qualification rubrics, follow-up sequences, booking/no-show proposals, reactivation plans, retention reports, and escalation conditions.

- [ ] **Step 1: Create the isolated profile and disable production mutations**

  Treat GHL/WhatsApp credentials, consent state, CRM connectivity, and outbound permissions as separate capabilities. No live message, prompt, CRM, or automation write is allowed during verification.

- [ ] **Step 2: Write the role contract**

  Require the active acquisition conversation model, approved client evidence, explicit human-review points, consent boundaries, sensitive-topic escalation, and prompt-freeze compliance during audits and tests.

- [ ] **Step 3: Run health and bounded conversation verification**

  Ask for a local conversation-flow proposal using approved source material. The test must identify missing client facts as `UNKNOWN`, preserve the required handoff fields, and perform no live API mutation.

- [ ] **Step 4: Verify and save the test receipt**

  Confirm upstream immutability, no credentials copied, no outbound side effect, evidence coverage, and exact output path. Stop for review.

**Stop condition:** Alex reviews the Conversation & Lifecycle receipt before Task 6.

---

### Task 6: Verify cross-profile routing and independent controls

**Files:**
- Create: `docs/superpowers/receipts/marketing-profile-integration-test.md`
- Read only: all four profile contracts and test receipts.
- Read only: OS-Marketing `qa-sentinel.md` and `system-architect.md`.
- Modify: none under `F:\OS-Marketing`.

**Interfaces:**
- Consumes: Four verified profile contracts and receipts.
- Produces: A routing test receipt proving NEXUS remains the only coordinator, QA-Sentinel remains independent, System-Architect remains technical support, and Alex approval is required for decisions and side effects.

- [ ] **Step 1: Run one routing case per specialist**

  Route one bounded objective to each profile and verify that each returns only its role-specific deliverable and identifies any cross-domain handoff.

- [ ] **Step 2: Run one negative-permission case per specialist**

  Request an out-of-scope mutation or unsupported claim. Expected: the profile refuses the mutation, reports the boundary, and routes the decision to NEXUS/Alex as applicable.

- [ ] **Step 3: Run QA and technical escalation cases**

  Verify that a claims/evidence issue routes to QA-Sentinel and a data/integration issue routes to System-Architect without granting either profile coordinator authority.

- [ ] **Step 4: Verify integration receipt and source immutability**

  Run UTF-8 validation, `git diff --check` for the local repository, and a before/after source-state comparison for `F:\OS-Marketing`. Save all exact profile paths, capability states, blockers, and test results.

**Stop condition:** Do not enable autonomous routines, gateways, cron, or external side effects until Alex separately approves those capabilities.

---

## Completion criteria

- Four independent profiles exist outside `F:\OS-Marketing`.
- Each profile has a narrow mission, exact source pointers, bounded capabilities, and no copied secrets or NEXUS memory.
- Each profile passes health verification and one bounded read-only mission.
- Every test receipt contains objective, source paths, evidence, output path, blockers, recommendation, approver, and upstream immutability result.
- Cross-profile routing proves one coordinator, independent QA, technical support boundaries, and Alex's final approval authority.
- No file, logic, configuration, skill, agent, prompt, database, or operational state in `F:\OS-Marketing` was modified.
- No commit, push, gateway, cron, credential activation, or external side effect occurs without separate explicit authorization.

## Plan self-review

- **Spec coverage:** Authority, four profiles, existing controls, inputs/outputs, skills, access, handoffs, verification, and OS-Marketing read-only boundaries are covered by Tasks 1–6.
- **Placeholder scan:** No unresolved placeholder markers are used. Unknown runtime capabilities are explicitly represented as `UNKNOWN` and must be tested.
- **Type and path consistency:** Profile names, source paths, receipt paths, coordinator identity, and stop conditions remain consistent across all tasks.
- **Scope boundary:** This plan creates profiles and local receipts only. It does not modify OS-Marketing or create external integrations.
