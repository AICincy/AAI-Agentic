# Host Binding

AAI cannot command product routing, context retention, or schedulers. Bind to what the current host actually exposes.

Grok is the current host. See grok-host.md and adaptation.md.

## Product map

| Product | What this skill can do | What it cannot do |
| --- | --- | --- |
| Grok | Govern turns when files load from /home/workdir/.grok/skills/ | Claim ChatGPT or Codex install; search missing chat history |
| ChatGPT | Foreign host | Observe or attest from this workspace |
| Codex | Foreign host | Observe or attest from this workspace |
| API | Supply instructions in the request | Persist state unless the caller stores it |
| Atlas | Govern if the host loads the skill | Assume connector availability |

`agents/grok.yaml` is the Grok display request. `agents/openai.yaml` is retained as a foreign-host stub. Neither file proves activation.

## Client-visible connectors (2026-09-03)

Source: Krass screenshots of the ChatGPT/Codex plugin list, plus Krass
statement that Tavily AI is installed but not in the frames.

This list is connector presence. It is not AAI load evidence. It is not
telemetry. AAI is a skill, not an item on this list.

Recorded names:

AgentMail, AgentMarkup, alphaXiv, Anti-Churn, Atlassian Rovo, Auto
Preference Learner, Codex Coordinator, Codex Engineering Guardrails,
Codex Security, Context7, CourtListener, DigitalOcean, Documents, Exa,
Figma, Firecrawl, GitBook, GitHub, Gmail, Google Drive, Lovable,
Malwarebytes, Midpage Legal Research, Nimble, Olostep, OpenAI
Developers, Parallel Search, PDF, Plugin Management, Presentations,
Sentry, Spreadsheets, Subtext, Tavily AI.

Useful if a domain skill needs live fetch: Exa, Firecrawl, Parallel
Search, Tavily AI, Midpage Legal Research, CourtListener, alphaXiv,
GitHub, GitBook, PDF, Documents, Spreadsheets, Google Drive.

Discover the named connector before use. If the current turn cannot
reach it, name that blocker. Do not invent a search result.

## Required host capabilities

| Capability | Degradation |
| --- | --- |
| File read/write | Describe the artifact. Do not claim SAVED. |
| Skill save with path echo | Stop at STATIC-PASS. Do not claim INSTALLED. |
| Conversation search / Personal Context | Use retrieval-scaffolding.md. Do not reconstruct. |
| Connected mail, files, case law, trackers | Discover first. If absent, name the blocker. |
| Trusted controller channel | Refuse operational and runtime status labels. |

## Trusted controller interface

A controller is trusted only if it is the host process or an inherited protected channel. A user-writable JSON file is not a controller.

Expected in-process or env attestation shape:

```json
{
  "controller": "host-name",
  "current_run": true,
  "labels": {
    "SAVED": {"target": "absolute-or-remote-uri", "operation": "write", "ok": true}
  }
}
```

Standalone `aai_runtime_gate.py response` must keep rejecting SAVED and higher labels from ledger files.

## Codex vs ChatGPT

- Codex: prefer action-before-narration, file identity, and repo-local validation.
- ChatGPT: prefer retrieval-before-reconstruction and one open loop. Durable save depends on the Files workflow actually returning a path.
- API: the caller owns persistence. Return turn state when asked.
