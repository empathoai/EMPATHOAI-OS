# Rule: Adversarial Auditing & Prompt Neutrality Doctrine

## 1. THE ZERO-COMPLACENCY MANDATE (NO SINGLE-PASS CERTIFICATION)
- Never accept a single prompt or single-pass evaluation as proof of system completeness or hermetic integrity.
- AI models (internal and external) naturally exhibit agreeableness bias. To achieve military-grade rigor, you must:
  1. Push the evaluator to its absolute limits.
  2. Specifically demand line-by-line verification, vulnerability detection, and explicit identification of leaks.
  3. Loop the audit cycle iteratively until the evaluator issues a zero-observation verdict grounded in facts.

## 2. THE PROMPT NEUTRALITY PRINCIPLE (NEVER CONTAMINATE THE ORACLE)
- When querying an external or internal knowledge base (e.g., NotebookLM, domain experts, external evaluators):
  - **PROHIBITED:** Injecting agency buzzwords, leading questions, preconceived frameworks, or patch-talk (*"Here are the 5 patches I applied, validate them"*). This biases the model, inducing confirmation bias or defensive hallucination.
  - **MANDATORY:** Formulate clean, neutral, and blind prompts (*"Audit this document end-to-end against your knowledge base with zero complacency and issue your clinical verdict"*).
  - Let the knowledge engine extract truth independently from its sources, without feeding it the answers.

## 3. THE BOUNDARY CONDITION TEST (THE ANTI-PATTERN FILTER)
- Immediately after any system or framework is certified as "complete", the agent MUST execute the Boundary Stress-Test:
  - *"Does this apply universally to any niche or scenario, or where does it break?"*
  - Identify where the system is 100% lethal (its native ICP) and where it is an operational anti-pattern (where it breaks, destroys unit economics, or violates compliance).
  - A framework that claims to work for everything works for nothing. Always document and enforce the boundary conditions.
