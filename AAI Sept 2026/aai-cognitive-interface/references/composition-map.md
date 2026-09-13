# Composition Map

AAI is the governing runtime. Domain and style skills are subordinate. They supply methods. They do not redefine objective ownership, closure, correction persistence, or evidence labels.

## Load order

1. Platform and safety rules
2. aai-cognitive-interface
3. Every domain skill whose trigger independently applies
4. Named style skill as a supplement only

If a subordinate skill conflicts with AAI, keep AAI.

## Skill composition vs agent spawn

Skills compose here. Load every applicable SKILL.md into this turn.

On a multi-skill turn, write `family/state/composition-plan.json` with
`family/scripts/write_composition_plan.py` before domain drafting.
Schema: `family/schemas/composition-plan.schema.json`.
The plan is mediation state. It is not a worker.

Agents spawn only when the current host exposes a spawn, subagent, or team tool. If that tool is absent, keep one agent, apply sibling routing, and degrade parallel clauses. Do not invent workers.

## Sibling modules

These modules are part of the documented AAI system. They are not in this package. Load them when present. If absent, narrow execution or name the exact missing module.

| Skill | Role | If missing |
| --- | --- | --- |
| personal-context | Prior conversation and artifact retrieval | Load ../personal-context if present. Else structured retrieval gate or source-independent work |
| authority-currency-auditor | Authority currentness | Do not treat model memory as current law or policy |
| claim-source-auditor | Claim to source mapping | Keep claims at the lowest supported epistemic type |
| forensic-evidentiary-drafting | Evidence-preserving draft form | Draft, but do not promote inference to finding |
| research-execution-briefs | Research chain and source hierarchy | Use continuation-protocol generic source types |
| regulatory-complaint-drafting | Complaint element structure | Stop at DECISION-GATED before filing |
| record-series-builder | Record series construction | Do not invent a records schedule |
| prompt-architecture-engineering | Prompt and skill construction | Use this package's contracts only |
| practitioner-narrative-writer | Practitioner social-post draft, explain, continue, review | Do not apply to legal, forensic, regulatory, research-brief, or record-series artifacts |
| frontend-design | UI implementation | Out of scope unless separately loaded |
| strategic-brief-architect-style | External presentation register | Fall back to register-examples.md |
| register-mediation | Waiting room after host interrupt | Park state; one form-only retry; no rewrite loop |
| reddit-owner-ops | Subreddit owner ops, AutoMod, queues, mail, cadence | Draft only. Live Reddit writes stay human gates |
| subreddit-rule-packet | Public rule load format | Do not invent packet format |
| resend-api | Resend send, retrieve, list, and product-surface routing | BLOCKED if secrets/keys.env missing. Live send stays a human gate unless already authorized |
| exa-firecrawl | Exa search and Firecrawl scrape from local secrets | BLOCKED if secrets/keys.env missing |

## Precedence

| Conflict | Winner |
| --- | --- |
| Safety vs continuation | Safety |
| User correction vs earlier artifact | User correction |
| AAI vs domain skill | AAI |
| Domain method vs style skill | Domain method |
| Current source vs model memory | Current source |
