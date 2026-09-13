# Grok Host Binding

This family runs on Grok. ChatGPT, Codex, API, and Atlas are foreign hosts.

## What this host exposes

| Capability | This workspace |
| --- | --- |
| Skill persist path | `/home/workdir/.grok/skills/<name>/` |
| Skill format check | `/root/.grok/skills/skill-creator/scripts/validate-skill.sh` |
| Files | sandbox read/write under `/home/workdir` |
| Web | `web_search`, `browse_page` |
| X | keyword, semantic, user, thread tools |
| Connected | Figma, GitHub, Voice, Automations |
| Bundled skills | docx, pdf, pptx, xlsx, ffmpeg, skill-creator |
| Chat history search | NOT EXPOSED |
| ChatGPT memory / export-learning | NOT A SOURCE |
| OpenAI telemetry | UNAVAILABLE |

Discover the current turn's tools before use. Inventory files are not this turn's tool list.

## Status on Grok

| Label | Evidence required |
| --- | --- |
| DRAFTED | Content exists |
| STATIC-PASS | `python3 scripts/aai_runtime_gate.py package <dir>` returns PASS |
| GROK-PRESENT | Skill directory exists at `/home/workdir/.grok/skills/<canonical-name>/` and `validate-skill.sh` prints OK |
| SAVED | Durable write returned a path in this run |
| INSTALLED | Refused unless a trusted live controller plus host-echoed save path exist |
| RUNTIME-* | Refused without live controller |

GROK-PRESENT is not INSTALLED. It is path-plus-format evidence on this host.

## Load rule

Load `aai-cognitive-interface` first on every Grok turn that uses this family. Domain skills supply methods only.

## Product customize layer (Krass decision, 2026-09-05)

grok.com Settings → Customize is a product prompt layer. It is not the skill persist path.

Controlling setup on this account:

- Response style: Comprehensive.
- Custom Agent Name: unused.
- Custom Agent Instructions: empty.
- Custody and method: skills under `/home/workdir/.grok/skills/`.

Do not paste AAI, domain skill bodies, matter facts, or tool inventories into that Instructions box. Do not treat a named Custom Agent as proof that AAI loaded.

## Adaptation vs memory

Do not use ChatGPT memory, model weights, or an export dump as the world model. Adapt per `adaptation.md`.
