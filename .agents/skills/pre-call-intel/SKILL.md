---
name: pre-call-intel
description: Conduct rapid pre-contact account due diligence, verify legal standing and operational licensure, isolate the Ultimate Decision Maker (UDM), enforce the 4-criteria prequalification filter, and produce the 1-page Pre-Contact Intelligence Brief before initiating contact.
---

# Pre-Call Intel

Conduct an express pre-contact account due diligence (15-20 minutes) and produce an actionable 1-page Pre-Contact Intelligence Brief before reaching out to or meeting a prospect.

## Operating Doctrine & Epistemic Boundaries

- Core mechanism: Account Due Diligence -> Prequalification -> UDM Isolation -> Pattern-Interrupt Hook (Doctor of Sales posture).
- Theoretical Foundations: Brian Tracy (The Psychology of Selling, Advanced Selling Strategies), Alex Dey (The Sales Cycle, 4-Criteria Prequalification), Neil Rackham (SPIN Selling), Dan Lok, Alex Hormozi.
- **Epistemic Rule (Facts vs. Hypotheses):**
  * **Verified Facts:** Public registry filings (Sunbiz / Secretary of State), medical/facility licenses (DOH, AHCA, NPI), public pricing, visible web/routing defects, ad library campaigns, and verbatim customer reviews. Cite exact tools and document numbers.
  * **Calibration Hypotheses:** Internal sales volume, transaction frequency, fee percentages, and total COI figures. **NEVER assert unverified internal figures as confirmed business facts.** Frame all economic models as diagnostic calibration brackets (Conservative vs. Moderate scenarios) used to probe during discovery.
- **Mandatory Output Language Rule (100% English Invariant):**
  Regardless of the operator's prompt language, the prospect's native language, country, or location (whether in China, Latin America, Europe, or the US), **the final Pre-Contact Intelligence Brief and all saved audit files MUST be written 100% in professional technical English.**
- **Mandatory File Persistence Logic:**
  Every execution of this skill MUST save the generated brief to disk before completing:
  * **Brief Destination Path:** `F:\EMPATHOAI_OS\audits\YYYY-MM-DD_<business-slug>_pre-call-audit.md` (e.g. `audits/2026-09-17_the-groves-coffee-house_pre-call-audit.md`).
  * **Raw Tool Evidence / Scrape Directory:** `F:\EMPATHOAI_OS\audits\prospect-audits\<business-slug>-YYYY-MM-DD\` (stores raw review JSONs/CSVs retrieved from Composio/Apify for forensic traceability).
  * **Client Promotion (SSOT):** When a prospect converts to an active deal or client, promote the brief to `F:\EmpathoKnowledge\clients\<business-slug>\`.

---

## Tool Boundaries & Execution Protocol

Execute data collection across two distinct paths:

### Path A: Public Surfaces & Deep Extraction (Direct Tools & Composio MCP)
- Targets: Public websites, landing pages, Google Maps listings, Meta Ad Library, Google Ads Transparency, state corporate registries (Sunbiz), and professional licensing boards.
- Mandatory Tool Routing:
  * **Native extraction tools (`search_web`, `read_url_content`):** Use for state corporate registries (e.g. `sunbiz.org`), medical licensing boards (e.g. Florida DOH MQA search, AHCA facility search, NPPES NPI Registry), and ad transparency checks.
  * **Composio MCP Tools (`COMPOSIO_SEARCH_TOOLS`, `COMPOSIO_MULTI_EXECUTE_TOOL`):**
    - **MANDATORY FOR REVIEWS:** When extracting Google Maps reviews, reputation sentiment, and owner response rate, execute the active Apify toolkit (e.g. Google Maps Reviews Scraper actor) if web snippets yield fewer than 10 reviews.
    - Use Firecrawl for deep page scraping, clean markdown conversion, and site mapping.

### Path B: Authenticated Channels (Active Operator Browser Session)
- Targets: Instagram (DMs, recent comments, engagement cadence), Facebook Pages, WhatsApp Web.
- Rule: Do not attempt cold scraping on login-gated networks. Prompt the operator:
  > *Please open the target prospect's Instagram/Facebook/WhatsApp in your active browser session so I can inspect live responses and recent interactions.*

---

## Execution Steps

### Step 1: Legal Entity, Regulatory Licensure & UDM Due Diligence (MANDATORY FIRST GATE)
Before inspecting websites or marketing assets, establish legal standing, ownership, and regulatory status via official registries:
1. **Corporate State Registry (e.g. Florida Sunbiz / Secretary of State):**
   - Active Legal Entity Name & Document / Filing Number.
   - Corporate Status: Active vs. Inactive / Dissolved / Delinquent.
   - Registered Agent & Managing Members / Officers: Extract exact full legal names and titles of owners, directors, or general partners.
   - Principal & Mailing Address: Verify corporate headquarters and operational address history.
2. **Regulatory Licensure & Compliance (Mandatory for Clinics, Healthcare & Licensed Trades):**
   - Medical Director / Practitioner Licensure (e.g. Florida DOH / MQA): Practitioner full legal name, License #, profession, license status (Clear/Active vs. Disciplinary sanctions/malpractice).
   - Facility Licensing (e.g. AHCA Health Care Clinic License): Facility license #, inspection status.
   - National Provider Identifier (NPPES NPI Registry): Type 1 (Individual) and Type 2 (Organization).
3. **Isolate the Ultimate Decision Maker (UDM):** Confirm the identified contact is the Owner / Principal Partner / Medical Director with contract and bank signature authority (not a receptionist or intermediate manager).

### Step 2: Financial Solvency & Operational Infrastructure Audit
1. Audit operational capacity: Count physical facilities, active treatment rooms, practitioner chairs, and estimated payroll.
2. Audit active paid acquisition: Check Meta Ad Library and Google Ads Transparency to verify whether the business allocates commercial budget for paid traffic.

### Step 3: Commercial Offer Surface & Empirical Ticket / AOV Proxy
1. Identify primary offer surface (service menu, treatment catalog, pricing tiers, quote flow).
2. Extract 2-3 Hero Offers with exact live prices.
3. Calculate empirical basket / AOV proxy based on observed combinations.

### Step 4: Digital Capture, Conversion Leaks & Customer Voice
1. Audit conversion paths: Form complexity, mobile performance, routing between locations/services.
2. Customer Voice (Composio MCP Enforced): Extract at least 2 verbatim positive review quotes (Dominant Buying Motive) and 2-3 verbatim negative review quotes (Operational Friction) with dates and locations.

### Step 5: The 4-Criteria Prequalification Filter
Evaluate the account against the 4 inalienable criteria:
1. **Need:** Verified operational friction or conversion leak in current acquisition flow.
2. **Usage Capacity:** Verified infrastructure and staff to absorb EmpathoAI systems.
3. **Money:** Proven financial solvency, active ad spend, and premium ticket.
4. **Desire / Power:** Direct access to verified UDM with contract signature power.
*Decision:* Discard account immediately if any criterion fails.

### Step 6: Cost of Inaction (COI) Diagnostic Calibration
Construct two calibration brackets based on empirical AOV:
- Standard Formula: \text{Monthly COI} = (\text{Exposed Demand} \times \text{Friction Leak \%}) \times \text{Conversion Rate} \times \text{AOV Proxy}
- Brackets: Conservative Scenario vs. Moderate Scenario.

### Step 7: 30-Second Pattern-Interrupt Opening Hook & Clinical Trigger Questions
1. **Craft the 30-Second Opening Script (Brian Tracy):** Focus exclusively on selling the 10-minute diagnostic session by calling out the specific audited leak.
2. **Prepare 3 Clinical Opening Questions:** Agenda Close, Grounded Implication with real quotes/facts, and COI Calibration Probe.

---

## Pre-Contact Intelligence Brief Template (1-Page Artifact)

```markdown
================================================================================
                    PRE-CONTACT INTELLIGENCE BRIEF (EMPATHOAI)
================================================================================

1. ACCOUNT GENERAL DATA
--------------------------------------------------------------------------------
• Brand / Operating Name: [Trade Name / DBA]
• Legal Corporate Entity & Doc #: [Registered Name & Document # from SOS / Sunbiz]
• Sector / Vertical: [ ] Medical / Aesthetic Clinic  [ ] B2B Services  [ ] Multi-Location Chain
• Active Footprint / Locations: [Count and addresses of operational facilities]
• Primary URL & Digital Channels: [Website, booking portals, active social handles]

2. LEGAL & FINANCIAL DUE DILIGENCE
--------------------------------------------------------------------------------
• Operating & Health Licenses: [ ] Active & Verified  [ ] Deficient / Expired  [ ] N/A
  - Licensing Body & License #: [e.g. Florida DOH License # / AHCA Clinic #]
• Corporate Standing & Public Litigation: [ ] Clear / Active  [ ] Material Risk Detected
• Active Paid Acquisition (Meta / Google Ads): [ ] High Spend  [ ] Moderate  [ ] Zero
• Observed Service / Treatment Ticket: $[Hero Offer Price] (AOV Proxy: $[AOV])
• High-Ticket Solvency Rating: [ ] Qualified  [ ] Questionable  [ ] Disqualified

3. ULTIMATE DECISION MAKER (UDM) & STRUCTURE
--------------------------------------------------------------------------------
• Ultimate Decision Maker (UDM): [Full Legal Name from Corporate Registry / Sunbiz]
• Exact Executive Title: [Owner / Founder / CEO / Medical Director]
• Buyer Personality Profile (Tracy / Dey):
  [ ] Director / Driver (Focused on ROI, speed, and bottom-line outcomes)
  [ ] Thinker / Analytical (Focused on evidence, data integrity, and compliance)
  [ ] Relater / Expressive (Focused on prestige, vision, and team impact)
• Direct Contact Channel: [Direct phone, email, LinkedIn, or personal line]
• Gatekeeper / Front Desk Protocol: [Reception contact and bypass notes]

4. THE 4-CRITERIA PREQUALIFICATION GATE
--------------------------------------------------------------------------------
[ ] 1. NEED: Verified operational bottleneck or conversion leakage in current flow.
[ ] 2. USAGE CAPACITY: Verified staff and infrastructure to operate EmpathoAI systems.
[ ] 3. MONEY: Proven financial solvency, active ad spend, and premium pricing.
[ ] 4. DESIRE / POWER: Direct verified access to UDM with sole contract signature power.
--> ACCOUNT STATUS: [ ] QUALIFIED FOR OUTREACH   [ ] DISCARDED / UNQUALIFIED SUSPECT

5. 30-SECOND PATTERN-INTERRUPT HOOK (BRIAN TRACY PROTOCOL)
--------------------------------------------------------------------------------
• Specific Operational Leak Detected:
  [Specific friction point, e.g., routing error, slow WhatsApp response, compliance gap]
• Verbatim 30-Second Opening Script (Selling the 10-Minute Diagnostic Session Only):
  "[Prospect Name], Alex Guajardo with EmpathoAI. Calling you directly because I audited
  your patient/customer acquisition flow across [Locations] and identified a specific
  conversion leak redirecting qualified demand to competitors. I am not calling to sell
  you software or marketing today; I only want to share a 10-minute diagnostic showing
  how to plug that revenue tax. You be the sole judge of whether it makes sense.
  Would you be open to reviewing this today at 4:00 PM or tomorrow at 10:00 AM?"

6. VALUE ANCHOR ARCHITECTURE (POINT A -> GAP -> POINT B)
--------------------------------------------------------------------------------
• Point A (Current Reality): [Manual handling, slow response latency, or cross-routing bleed]
• The Gap (Cost of Inaction): $[Conservative] to $[Moderate] / month in uncaptured revenue
• Point B (Prescribed Outcome): Autonomous high-converting capture infrastructure with 10:1 ROI
================================================================================
```

---

## MANDATORY PRE-COMPLETION VERIFICATION CHECKLIST

Every agent MUST verify and check off every item below before delivering the brief:

- [ ] **100% Technical English Language Enforced:** Brief, ledgers, and notes written strictly in technical English.
- [ ] **Artifact Persisted to Disk:** Saved to `F:\EMPATHOAI_OS\audits\YYYY-MM-DD_<business-slug>_pre-call-audit.md` before completion.
- [ ] **Corporate Entity & Licensure Verified First:** State registry (Sunbiz / SOS) and professional licensure (DOH, AHCA, NPI) verified with official document numbers.
- [ ] **Ultimate Decision Maker (UDM) Isolated:** Full legal name and verified executive title extracted from public registries.
- [ ] **All 4 Prequalification Criteria Evaluated:** Need, Usage Capacity, Money, and Power explicitly scored.
- [ ] **Economic Metric Grounded:** Empirical pricing and ticket proxy verified from public surfaces.
- [ ] **30-Second Opening Hook Written Verbatim:** Tailored to the UDM selling solely the 10-minute diagnostic meeting.

---

## Canonical References

- Master Research Playbook: F:\EmpathoKnowledge\frameworks\playbook-comercial-01-pre-call-research.md
- Discovery Call Playbook: F:\EmpathoKnowledge\frameworks\playbook-comercial-02-discovery-call-script.md
- Operating Sales Pointer: F:\EMPATHOAI_OS\references\sales-system.md
