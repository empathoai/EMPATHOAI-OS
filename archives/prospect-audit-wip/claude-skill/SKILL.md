---
name: prospect-audit
description: Audit an external business or prospect for commercial, digital, operational, local-search, content, and compliance friction. Trigger for prospect audits, client evaluations, competitor checks, or a business website/social/Maps URL. Distinct from /audit, which audits this internal AIOS.
---

# Prospect Audit

Use this skill for an external business. The authoritative procedure, taxonomy,
formulas, compliance gates, and report structure live in the central framework:

F:\EmpathoKnowledge\frameworks\ai-prospect-audit-framework-healthcare-food-services-us.md

## Execution

1. Read the relevant sections of the central framework before starting.
2. Identify the business, niche, city, state, official channels, and audit date.
3. Use Alex's live browser session as the primary route for websites, social
   profiles, Ads Library, Maps, booking flows, and authenticated surfaces.
4. Ask Alex to open or sign in to a missing surface. Never request, copy, or
   store passwords, cookies, tokens, or MFA codes.
5. Use fetch only as supplemental evidence. Do not make visual, layout,
   navigation, creative, profile, or customer-journey conclusions from fetch alone.
6. Keep the audit read-only. Do not submit forms, send messages, create
   bookings, click reactions, change settings, or alter campaigns without
   explicit authorization.
7. Record URL, identity, date/time, visible state, and evidence for every
   material finding. Mark unavailable evidence UNKNOWN or REQUIRES HUMAN REVIEW.
8. Track every phase as PASS, PARTIAL, BLOCKED, or NOT RUN. Never infer PASS
   from a polished narrative.
9. Before declaring COMPLETE, create the manifest from
   `F:\EMPATHOAI_OS\references\prospect-audit-manifest.template.json` and run
   `powershell -File F:\EMPATHOAI_OS\scripts\validate-prospect-audit-manifest.ps1
   -ManifestPath <path> -AsJson`. A nonzero exit or `can_complete=false` blocks
   completion.

10. Run the business-intelligence path, not channel inventory: reconstruct
    `evidence -> demand source -> winning product/occasion -> promise -> break
    -> root-cause hypothesis -> commercial impact -> discovery question`.
11. For food-service prospects, open every accessible ordering provider
    visibly (DoorDash, Uber Eats, Grubhub, Postmates/Order Online and relevant
    aggregators). Capture each provider's visible rating, volume, hours, menu,
    featured/most-ordered items, prices, offers, add-ons, reviews and friction.
    Compare the same products against the official menu. Never infer a winner
    from a grid or a name alone.
12. Code reviews as episodes: request/occasion -> expectation -> received
    experience -> failure point -> consequence -> owner recovery -> falsifiable
    operational hypothesis. Keywords and star counts are supporting signals,
    not the intelligence output.
13. Build competitors by occasion and substitute, with product hero, price,
    proof volume, convenience, offer, promise, objection and why the prospect
    wins/loses. A list of competitor names is not a matrix.

## Required checks

Apply the framework's phases for:

- organization and public-record validation, including Sunbiz for Florida;
- brand, SERP, website/CRO, speed-to-lead, Maps/GEO, and operational leakage;
- Instagram/Facebook deep content review using individual posts/Reels;
- Google Maps review download/review intelligence and analysis of 1–4 star
  complaints, owner responses, recurrence, and operational themes;
- Meta Ad Library searches by exact Instagram and Facebook usernames before
  any broad discovery search;
- vertical-specific compliance, licensing, permits, claims, privacy, and ADA risks.
- platform-level product and demand intelligence across all accessible ordering
  providers, plus an occasion-by-competitor evidence matrix;

Do not confuse a social handle, brand name, DBA/fictitious name, legal entity,
license, permit, or location. Do not select a similar entity without exact
evidence.

Translate verified findings into internal question paths:
evidence -> observed pattern -> impact hypothesis -> exploratory question ->
answer branch -> disconfirming question -> transition. Do not reveal the
diagnosis to the prospect or treat an untested hypothesis as fact.

## Completion gate

The audit is complete only when the report follows the central framework and
contains:

- the three critical bleeds in Observation -> Evidence -> Business Impact ->
  Compliance Risk -> Recommended Action format;
- an evidence-based organic content critique, including sample, mix, objectives,
  visible performance patterns, gaps, funnel role, and priority experiments;
- review intelligence based on the complete available scraper dataset, or a
  documented partial-coverage limitation, with separate 1–4 star themes;
- exact-identity Ads Library status: ACTIVE ADS VERIFIED, NO ADS FOUND UNDER
  VERIFIED IDENTITIES, or UNRESOLVED;
- explicit separation of OBSERVED, INFERRED, UNKNOWN, and REQUIRES HUMAN REVIEW;
- a phase/evidence manifest with artifacts, coverage, limitations, and statuses;
- no unsupported claims, invented metrics, or conclusions based only on profile
  inventory.
- platform menus, featured/most-ordered items, offers, ratings and provider
  reviews are captured when accessible, and each material finding is tied to a
  product, occasion, failure mode, root-cause hypothesis and next question.

If any mandatory artifact is missing, the result is PARTIAL or BLOCKED, never
COMPLETE. Run an independent/adversarial final check when practical.

Do not save prospect material to clients/ or the central SSOT unless Alex
explicitly authorizes persistence.
