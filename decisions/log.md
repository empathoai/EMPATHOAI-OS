# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-09-06 - Audit evidence and routing maintenance

**Decision:** Ship audit rubric v2 and a small /link skill. Audit scores working evidence across the Four Cs, checks operating-manual routing and freshness, and passes one concrete gap into /level-up. A selected repair can improve an existing workflow instead of creating another skill.

**Why:** File counts, configured keys, named rituals, and recent edits do not prove an operational EmpathoAiOS. Source findability and freshness need explicit checks.

**Alternatives considered:** Keeping presence-based scoring or requiring a hot cache. Neither reliably establishes retrieval quality or successful execution.

## 2026-09-06 - Portable skills and automatic audit history

**Decision:** Ship all four skills for Claude Code and Codex, with bundled resources, matching operating manuals, and a script for regenerating Codex copies. Audit reports are saved automatically, preserve previous runs, and track findings across comparable inspections.

**Why:** Students need the same shared guidance when switching assistants and evidence of actual improvements over time. Intentional runtime adaptations, unknown verification, and confirmed defects are reported separately.

## 2026-09-06 - Portable 3D Brain skill

**Decision:** Add `/3d-brain` for Claude Code and Codex. Ask for a name and categories, map selected local folders, and scaffold a bundled, configurable application with spherical placement, Cinema, and interactive growth replay.

**Why:** Shipping the working renderer preserves the intended appearance and interactions across EmpathoAiOS installations. A prose-only prompt would produce inconsistent recreations. User config and graph data remain local; the public package includes only code, documentation, dependency notices, and fictional test inputs.

## 2026-09-06 - Add ongoing context interviews

**Decision:** Adapt the upstream grill-me skill for EmpathoAiOS and ship matching Claude/Codex packages. Save every answer to brainstorms/, preserve resumable Q&A history, and update canonical context only with confirmed facts during requested context-building sessions.

**Why:** Onboarding is an initial snapshot. Ongoing interviews capture changing priorities, decisions, and preferences while keeping tentative ideas distinct from current business facts.

## 2026-09-09 - One task per session

**Decision:** Execute one task per session and defer unrelated work to a later session.

**Why:** Focused sessions preserve execution context, reduce cross-task contamination, and make work easier to resume and verify.

**Alternatives considered:** Combining several related tasks in one session. This was rejected because apparent relatedness can still dilute context and completion evidence.

## 2026-09-09 - EmpathoKnowledge as the enterprise knowledge SSOT

**Decision:** Use `F:\EmpathoKnowledge` as the single enterprise-wide source of truth for durable knowledge, including client context. `F:\EMPATHOAI_OS` remains an execution and orchestration system and must not maintain duplicate permanent knowledge copies.

**Why:** Multiple OS-specific knowledge bases create conflicting versions, repeated client context, and uncertainty about which source controls. Centralizing durable knowledge preserves one authority while allowing each OS to keep its local tools, telemetry, scratch data, and deliverables.

**Alternatives considered:** Maintaining separate knowledge bases with synchronization, or copying central knowledge into each OS. Both were rejected because synchronization and copies recreate the duplication problem.

**Owner:** Alex Guajardo.

## 2026-09-16 - Evidence-gated prospect-audit completion

**Decision:** Prospect audits cannot be declared `COMPLETE` from narrative quality alone. Each audit must declare required phases, record raw evidence and coverage in a manifest, and pass the local validator. Missing mandatory artifacts, including review intelligence, force `PARTIAL` or `BLOCKED`.

**Why:** The Groves Coffee House run produced a persuasive diagnosis but did not download and analyze the available Google Maps reviews. The framework contained the topic, but the execution contract lacked an independent blocking control.

**Where:** `F:\EmpathoKnowledge\frameworks\ai-prospect-audit-framework-healthcare-food-services-us.md`, `references\prospect-audit-manifest.template.json`, `scripts\validate-prospect-audit-manifest.ps1`, and mirrored `prospect-audit` skills.

## 2026-09-16 - Update empathoai.com tone and positioning (priority this week)

**Decision:** Rework empathoai.com's tone and add cross-vertical proof before sending it to any prospect. Keep the Diagnosis → Architecture → Execution → Scale framework — it is genuinely vertical-agnostic. Remove exclusivity/gatekeeping language ("WE DO NOT WORK WITH MOST COMPANIES", "SECTOR VALIDATION REQUIRED", "FIX THE SYSTEM OR DON'T PAY") and add a Spanish version, at minimum for the home and about pages.

**Why:** Reviewed live during The Groves Coffee House prospect call prep. The site targets a serious B2B/SaaS buyer in English with gatekeeping copy, while the actual current pipeline is local operator-run businesses (medspas, restaurants, a print shop, a coffee house) — many Spanish-speaking. Gatekeeping language is the wrong signal during a capitalization phase, not a filtering phase. Sending the current site to a prospect like Andrea (Groves) would undercut the call instead of supporting it.

**Alternatives considered:** Niching down immediately per Nate Herk's framework. Rejected for now — capitalization takes priority over narrowing; the underlying framework already works across verticals (medspa, restaurant, print shop), so proof-by-example solves "adapts to anyone" without diluting positioning. Vertical subdomains/landing pages deferred to `backlog.md` as a later step once volume justifies the split.

**Owner:** Alex Guajardo.

## 2026-09-17 - Retiro y reconstrucción de la skill prospect-audit

**Decision:** Desinstalar temporalmente la skill `prospect-audit` de los árboles activos (`.agents/skills` y `.claude/skills`), removiendo sus dependencias en `AGENTS.md`, `CLAUDE.md`, y `references/skill-routing.md`, y archivando sus artefactos en `archives/prospect-audit-wip/`. El documento maestro de conocimiento se preserva intacto en `F:\EmpathoKnowledge\frameworks\ai-prospect-audit-framework-healthcare-food-services-us.md`.

**Why:** La implementación inicial de la skill no proporcionaba una experiencia de ejecución consistente entre diferentes modelos (Codex, Claude, Antigravity), generando confusión en el flujo operativo. Se retira del runtime activo para ser reconstruida de forma limpia, modular y verdaderamente escalable en una sesión dedicada.

**Alternatives considered:** Dejar la skill activa e iterar en caliente. Rechazado porque genera fricción y colisiones con el comportamiento de los agentes.

**Owner:** Alex Guajardo.

## 2026-09-17 - Certificación Oficial de la Biblia Comercial de 8 Fases (Sally SSOT)

**Decision:** Codificar, consolidar y certificar oficialmente el Sistema Comercial de 8 Fases de EmpathoAI como la biblia de ejecución en campo (`F:\EmpathoKnowledge\EMPATHOAI_COMMERCIAL_MASTER_SYSTEM_SSOT.md` y `F:\EmpathoKnowledge\frameworks\playbook-comercial-0*.md`). 

**Why:** Auditoría clínica y ciega completada por Sally (Directora Comercial en NotebookLM) sobre la literatura científica de Brian Tracy, Neil Rackham, Alex Hormozi, Alex Dey, Dan Lok, Zig Ziglar y Chris Voss. El sistema fue certificado formalmente como 100% hermético e impecable tras incorporar: (1) ciclo de inconformidad y cuentas huérfanas, (2) rutina de reinicio mental de 120s y escudo anti-precio telefónico, (3) candado innegociable de decisores y transición obligatoria SPIN a Necesidad Explícita, (4) propuesta lógica 10:1 con silencio estratégico y cierre de hoja de pedido, (5) discriminación condición vs. objeción, colchón emocional y ruptura acelerada a día 14, (6) cobro en vivo por pasarela dual (tarjeta instantánea <$5k / autorización corporativa >$5k) y escudo anti-buyer's remorse, (7) extracción de referidos guiada por categorías y pre-encuadre mutuo, y (8) retención <2% churn y tablero de velocidad de ventas ($SV = \frac{N \times V \times LCR}{T}$).

**Alternatives considered:** Mantener frameworks comerciales dispersos o resúmenes teóricos sin guiones verbatim. Rechazado porque dejaba cabos sueltos, fugas de margen y debilidad en la ejecución ante objeciones en frío.

**Owner:** Alex Guajardo & Sally (Directora Comercial).

## 2026-09-17 - Adopción de la Doctrina de Auditoría Adversarial y Neutralidad de Prompts

**Decision:** Institucionalizar la Regla de Espacio de Trabajo `.agents/rules/adversarial-auditing-and-prompt-neutrality.md` y la referencia `references/adversarial-auditing-doctrine.md`.

**Why:** Durante la certificación del sistema comercial con Sally (NotebookLM), se demostró empíricamente que: (1) las evaluaciones de una sola pasada o un solo prompt caen en complacencia y validación superficial, requiriendo presión adversarial reiterada hasta agotar observaciones; (2) inducir o sesgar a la IA con terminología forzada o mención de parches contamina el oráculo y destruye la objetividad, requiriendo prompts 100% limpios y ciegos; (3) todo sistema declarado hermético debe ser sometido al test de condiciones de frontera (anti-patrones) para evitar la falacia de universalidad.

**Alternatives considered:** Confiar en evaluaciones de un solo paso o permitir prompts inductivos. Rechazado porque genera falsos positivos, sesgo de confirmación y desalineación con la literatura base.

**Owner:** Alex Guajardo.


