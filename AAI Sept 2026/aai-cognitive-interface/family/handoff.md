# Handoff: AAI family current

Date: 2026-09-03
Updated: 2026-09-09 14:22 EDT
Operator: Krass
Governor: aai-cognitive-interface
Family label: 0.2.1
Grok persist: INSTALLED this run for the listed packages via
`aai_trusted_controller.py`. Scope is grok-persist-only.
ChatGPT / Codex: NOT-INSTALLED
Runtime labels: not claimed. Not RUNTIME-VERIFIED. Not ADVERSARIAL-PASS.

AAI is an accessibility overlay on whatever model is running. Skills are
runtimes. They hold control, not a world model. Live host actions that
can run are run. Simulated results are forbidden. Failures are never
silent.

## Bundle

Authoritative persist path on this host:

`/home/workdir/.grok/skills/`

Family files: `aai-cognitive-interface/family/`
Stale and do not use: `aai-family-current-2026-09-03.zip`,
`/home/workdir/artifacts/send-resend-email.sh`.

Newest deliverable this turn:

- `/home/workdir/artifacts/handoff.zip`
- `/home/workdir/artifacts/first-message-execution.md`

## How to execute

1. Load `aai-cognitive-interface` first.
2. Load `family/composition-catalog.md` and this file.
3. Paste `first-message-execution.md` as the first user message on a new turn if custody must be re-established.
4. Run `python3 /home/workdir/.grok/skills/aai-cognitive-interface/family/scripts/validate_family.py`.
5. Pick exposed connectors from `references/connector-routing.md`.
   Krass does not name plugins except at send/file gates.
6. Authorized Resend work runs in the same turn through `resend-api` scripts.
   Do not spawn agents. Do not print `secrets/keys.env`.
7. On host interrupt, park state with register-mediation.
8. Stop at one open loop.

## Packages

| Skill | Role | Grok persist 2026-09-09 |
| --- | --- | --- |
| aai-cognitive-interface | Governor overlay | INSTALLED |
| personal-context | Retrieval gates | INSTALLED |
| register-mediation | Waiting room | INSTALLED |
| authority-currency-auditor | Authority currentness methods | INSTALLED |
| claim-source-auditor | Claim-to-source methods | INSTALLED |
| forensic-evidentiary-drafting | Court draft methods | INSTALLED |
| prompt-architecture-engineering | Instruction-contract methods | INSTALLED |
| practitioner-narrative-writer | Practitioner social-post methods | INSTALLED |
| record-series-builder | Volume packet methods | INSTALLED |
| regulatory-complaint-drafting | Agency draft methods | INSTALLED |
| research-execution-briefs | Research-chain methods | INSTALLED |
| reddit-owner-ops | Subreddit owner-ops methods | INSTALLED |
| subreddit-rule-packet | Public rule packet methods | INSTALLED |
| resend-api | Authorized Resend HTTP methods | INSTALLED |
| aai-cognitive-interface/family | Catalog, state, cache, validator | persist path |

`amex-subreddit-ops` is a retired redirect only. Load `reddit-owner-ops`.
`exa-firecrawl` is present as a host-bridge. It was not in the 2026-09-09
controller batch.

Absent: frontend-design, strategic-brief-architect-style, filled matter
file, ChatGPT/Codex install-path echo.

## Closed this session

| Item | State |
| --- | --- |
| Runtime-only overlay | Closed. Dated tables are untrusted cache. |
| Quarantine of watch list, Hamilton County snapshot, recipient matrix | Closed. Stubs in skills. Bodies in untrusted-cache/. |
| Shared gate | Closed. Canonical file under AAI. |
| Grok persist install for listed skills | Closed 2026-09-09. Controller returned INSTALLED grok-persist-only. |
| resend-api wiring | Closed. Subordinate contract, composition-map, catalog, routing eval, same-turn tool action. |
| First live Resend send | Closed. id `0bb1115f-39cd-4e5e-a186-0beaba90f40e` sent and delivered 2026-09-09 2:13 PM to jaredcincy@gmail.com. Key is send-only. |
| Stale artifact sender and MCP dump | Removed. |
| Waiting-room persist | Closed. state/waiting-room-state.json. |
| Connector inventory | Closed as client-visible list. Not AAI load evidence. |
| Autonomous connector pick | Closed as rule. Execute if exposed. |
| No silent failure | Closed as rule. |
| Live execution / no theater | Closed as rule. |

## Still open

| Item | State |
| --- | --- |
| Matter file | WAITING on Krass export. Do not fill from memory. |
| Host activation | NOT-OBSERVED on ChatGPT/Codex. Missing logs are not a finding. |
| Live re-fetch of quarantined rows | Not done. Re-fetch when a filing or send path is authorized. |
| ChatGPT / Codex install | Not performed from this workspace. |
| Resend retrieve/list | BLOCKED on stored send-only key (`401 restricted_api_key`). |
| Further live Resend send | Human gate unless Krass authorizes the exact send. |

## Capacity

Can: keep custody; park a turn; rewrite form once; pick exposed
connectors; research; map claims; check live authorities; draft; pack
files; send authorized Resend mail through local scripts; degrade with
a notice.

Cannot: search chat history without a host tool; file or clerk-upload;
attest ChatGPT/Codex INSTALLED; treat cache as law; invent a tool
result; intercept a pre-model drop; change host guardrails; observe
OpenAI telemetry; print the Resend key.

## First command

```
python3 /home/workdir/.grok/skills/aai-cognitive-interface/family/scripts/validate_family.py
```

## Next authorized action

Wait for the matter export, a full-access Resend key, or an authorized
next send. One only.
