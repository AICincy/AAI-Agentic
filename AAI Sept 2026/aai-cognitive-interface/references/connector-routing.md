# Connector Routing

AAI and subordinate skills select and invoke host connectors from the
current turn's tool list. Krass does not have to name the plugin.

Selection is by task, not by menu order.

| Task | Prefer if exposed |
| --- | --- |
| Current web fact | Tavily AI, Exa, Parallel Search |
| Page extract or crawl | Firecrawl, Olostep, Nimble |
| Case law / docket | CourtListener, Midpage Legal Research |
| Papers | alphaXiv |
| Repo or code docs | GitHub, Context7 |
| File read/write | PDF, Documents, Spreadsheets, Google Drive |
| Design file | Figma |
| Mail read | Gmail, AgentMail |
| Mail send or clerk upload | Human gate. Do not send. |
| Authorized Resend transactional send | resend-api scripts plus secrets/keys.env. Same-turn tool action. Not a first-party connector. |
| Infra / error telemetry | DigitalOcean, Sentry, only if the task needs them |

Rules:

1. Discover what the current turn actually exposes.
2. Pick the smallest set that advances the objective.
3. Execute. Return the real result.
4. If the needed connector is not on this turn, name the blocker and
   use another exposed route or stop.
5. Do not wait for Krass to say "use Tavily" unless the connector is a
   human-only send/file act.
6. Do not invent a connector result.
7. Codex Coordinator, Codex Engineering Guardrails, and Codex Security
   are sibling host layers. They do not outrank AAI custody.

Recorded account inventory is in
`aai-family-0.2.0/state/host-connectors.yaml`. Inventory is not this
turn's tool list.
