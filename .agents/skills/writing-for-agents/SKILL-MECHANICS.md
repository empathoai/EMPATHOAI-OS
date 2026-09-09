# Skill mechanics

The skill-specific branch of `writing-for-agents`: what changes when the document is a skill (frontmatter, invocation choice, and router skills). Everything else about writing it is the universal reference in `SKILL.md`.

## Invocation

A **model-invoked** skill keeps a `description`, so the agent can fire it autonomously and other skills can reach it. Its description is an always-loaded context pointer, so write it with concise, distinct trigger branches.

A **user-invoked** skill sets `disable-model-invocation: true`; only the human can invoke it. Use this when autonomous discovery is not wanted.

Pick model-invocation when the agent must reach the skill on its own or another skill must reach it. Pick user-invocation when it should fire only by explicit human request.

## Router skills

When user-invoked skills multiply beyond what the human can remember, use one router skill that names the others and when to reach for each. A router can point the human to skills but cannot autonomously fire user-invoked skills.
