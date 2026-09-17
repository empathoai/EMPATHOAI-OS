# Marketing Profile Source Inventory

**Task:** 1 — Lock the read-only source contract
**Inspection mode:** Read-only
**Inspection date:** 2026-09-09
**Source root:** `F:\OS-Marketing`
**Receipt owner:** NEXUS

## Boundary result

The four required source locations exist under `F:\OS-Marketing`. The source root is not a Git repository in this environment, so Git history and clean-state checks are unavailable. No source file was written by this task.

| Source | Type | Exists | Observed size (bytes) | Runtime state |
|---|---|---:|---:|---|
| `F:\OS-Marketing\AGENTS.md` | Governing kernel and invariants | Yes | 13,641 | Read and verified |
| `F:\OS-Marketing\infrastructure\tools-registry.md` | Tool and integration registry | Yes | 7,869 | Read and verified |
| `F:\OS-Marketing\knowledge\sop-registry.md` | SOP lifecycle registry | Yes | 14,666 | Read and verified |
| `F:\OS-Marketing\.agents\agents\` | Existing agent definitions | Yes | Directory | Enumerated |
| `F:\OS-Marketing\.agents\skills\` | Local executable skills | Yes | Directory | Enumerated |

## Governing rules consumed

`AGENTS.md` establishes the rules that every new profile must inherit by reference:

- Raw source immutability and dossier grounding.
- Gate 0 compliance for health-related copy, scripts, hooks, headlines, and conversational bots.
- Tenant isolation and deterministic client attribution.
- Mutation gate: analysis, review, and audit are read-only unless the user explicitly authorizes a write.
- Verification-first completion and autonomous tool execution through the registry.
- English internal documentation and explicit agent-authoring protocol.
- `F:\EmpathoKnowledge` as the durable knowledge SSOT.
- OS-Marketing as the operational authority for campaign work, bot prompts, local telemetry, and client outputs.
- Provenance for qualitative claims, market insights, clinical mechanisms, statistics, and psychology claims.
- Full operational playbook preservation rather than high-level compression.
- Active patient acquisition conversation model and required conversation phases.
- Prompt freeze during testing and audits.
- One-question-at-a-time alignment for complex prompt or workflow changes.

New profiles consume these rules through read-only source pointers. They do not fork or rewrite them.

## Tool-registry dependencies

The tool registry defines nine operational categories that the profile map must respect:

1. Client communications and email dispatch.
2. Meta Ads telemetry and pacing.
3. Web research and clean extraction.
4. Local telemetry caches, including Meta Ads and GHL conversation evidence.
5. Knowledge graph, retrieval manifest, and deterministic auditing.
6. Local backend server and Mission Control.
7. Creative engine and 3:2:2 production.
8. Google Workspace and cloud asset governance.
9. Sovereign executive PDFs and brand assets.

Registry entries are capability declarations, not proof that a profile has credentials, account permissions, runtime connectivity, or authorization to create external side effects. Those states remain `UNKNOWN` until verified inside the target profile.

## SOP-registry dependencies

`knowledge/sop-registry.md` is an auxiliary eligibility and lifecycle index. It does not replace source dossiers or frameworks and does not alter ingestion.

- `sop_relevance`: `not-assessed`, `candidate`, `not-candidate`.
- `sop_status`: `not-requested`, `draft`, `reviewed`, `approved`, `superseded`.
- `candidate` does not mean an SOP exists or is approved for a client.
- Generated SOPs require an explicit reference, client/namespace, owner, version, and lifecycle status.
- `knowledge-to-sop` reads the registry but does not edit it.
- Uncertain or stale entries remain `not-assessed`.

## Existing agent definitions

Exactly three Markdown agent definitions were enumerated:

- `F:\OS-Marketing\.agents\agents\creative-director.md`
- `F:\OS-Marketing\.agents\agents\qa-sentinel.md`
- `F:\OS-Marketing\.agents\agents\system-architect.md`

These are upstream role references. The new profiles must not overwrite, rename, or convert them into orchestrators.

## Local skill inventory

Exactly 27 local `SKILL.md` files were enumerated:

- `agent-reach`
- `client-email-dispatch`
- `contextual-source-capture`
- `conversational-dm-triage`
- `creative-proposal-engine`
- `defuddle`
- `disrupter-322-copywriting`
- `empathoai-prostories`
- `ghl-bot-prompt-audit`
- `google-workspace-automation`
- `humanizer`
- `icp-builder`
- `impeccable`
- `json-canvas`
- `knowledge-to-sop`
- `last30days`
- `marketing-council`
- `meta-ads-4pi-audit`
- `meta-ads-creative-map`
- `notebooklm-extraction-pipeline`
- `obsidian-bases`
- `obsidian-cli`
- `obsidian-markdown`
- `organic-video-engine`
- `os-marketing-audit`
- `visual-prompt-engine`
- `writing-for-agents`

The profile plan must enable only the smallest relevant subset. Installation, discovery, credentials, and connectivity are separate verification steps.

## Role-to-source dependency matrix

| New profile | Primary upstream sources | Supporting sources | Side-effect default |
|---|---|---|---|
| Marketing Strategist | `AGENTS.md`, `icp-builder`, `marketing-council`, SOP registry | `agent-reach`, `last30days`, `os-marketing-audit`, approved EmpathoKnowledge references | Read-only; local drafts only |
| Performance / Meta Ads | `AGENTS.md`, tools registry, `meta-ads-4pi-audit` | `os-marketing-audit`, `last30days`, telemetry tools, QA-Sentinel contract | Read-only; no ad-account or budget mutation |
| Creative & Scripts | `AGENTS.md`, `creative-director.md`, Gate 0 rules | `disrupter-322-copywriting`, `meta-ads-creative-map`, `organic-video-engine`, `empathoai-prostories`, `humanizer`, `visual-prompt-engine` | Local drafts only; no publication |
| Conversation & Lifecycle | `AGENTS.md`, SOP registry, client dossiers | `ghl-bot-prompt-audit`, `conversational-dm-triage`, QA-Sentinel contract, approved client frameworks | Read-only; no live prompt, CRM, message, or automation mutation |

Cross-cutting references:

- QA review: `qa-sentinel.md`.
- Technical/data dependencies: `system-architect.md`, tools registry, Mission Control and telemetry entries.
- Durable knowledge: approved pointers into `F:\EmpathoKnowledge`; no duplicate vault.

## Capability status

The following capabilities are not yet verified in any new profile and must remain `UNKNOWN` until tested there:

- Hermes profile existence, isolated home, and profile-local configuration.
- Profile-specific skill discovery and enablement.
- Meta Graph API credential availability and connectivity.
- Composio Gmail or Google Workspace authentication and recipient permissions.
- GHL/WhatsApp read access, consent state, and outbound permissions.
- Firecrawl fallback access and cost posture.
- Mission Control connectivity and permitted local endpoints.
- Ability to write only to approved local draft/report locations.
- A2A or other inter-profile communication connectivity.
- Gateway, cron, and autonomous routine status.

## Bounded-test contract

Each new profile must pass one read-only mission before the next profile is created. The mission receipt must include:

1. Objective and scope.
2. Exact source paths read.
3. Findings separated from assumptions and recommendations.
4. Evidence and freshness limitations.
5. Exact local output path.
6. Blockers and `UNKNOWN` capabilities.
7. Required approver.
8. Confirmation that no file under `F:\OS-Marketing` was modified.

## Completion result

- Required sources: **PASS**
- Existing agents enumerated: **PASS — 3**
- Local skills enumerated: **PASS — 27**
- Source root Git state: **UNKNOWN — not a Git repository**
- Credentials and live integrations: **UNKNOWN — not tested in target profiles**
- OS-Marketing write activity: **NONE**
- Task 2 authorization: **BLOCKED pending Alex review of this receipt**
