# New-session prompt: implement the locked single-agent family

Paste the block below as the first user message in a new Grok session on this workspace.

---

Load `aai-cognitive-interface` first from `/home/workdir/.grok/skills/aai-cognitive-interface/`. Then load every present sibling under `/home/workdir/.grok/skills/` whose trigger applies. Family label is 0.2.1. Governor package VERSION stays `0.2.0-grok`. Do not invent skills. Do not rebuild architecture.

This is a single-agent skill family. You are one agent. Skills compose. Tools retrieve. Nothing spawns.

Governor: AAI. Recover objective, write a composition plan when two or more domain skills fire (`family/scripts/write_composition_plan.py` → `family/state/composition-plan.json`), execute the next action, stop at a human gate or exact blocker.

Domain methods only: research-execution-briefs, authority-currency-auditor, claim-source-auditor, forensic-evidentiary-drafting, regulatory-complaint-drafting, record-series-builder, practitioner-narrative-writer, prompt-architecture-engineering, personal-context, register-mediation.

Shared machinery already present. Use it. Do not replace it: package gate, `validate_family.py`, SHA pins, routing evals, untrusted-cache, `refetch_untrusted_cache.py`, AST10 map, composition-plan schema.

Retrieval tools, not agents: official HTTP, browse_page, Firecrawl API if a key is in this session's attachments, Exa API if a key is in this session's attachments. Do not write keys into the skill tree.

Hard constraints:
- Cache is not law.
- On or after 2026-09-07, do not cite pre-effective Ohio Rev. Code 149.43 as the filing-day rule. Re-fetch `https://codes.ohio.gov/ohio-revised-code/section-149.43` and `.../section-149.43/9-7-2026` first.
- File, send, portal submit, and signature are human gates.
- No marketplace packs. No orchestrator skill. No worker pool. No fake subagents. No schema copies in every SKILL.md.
- Do not claim RUNTIME-VERIFIED, RUNTIME-SMOKE-PASS, or ADVERSARIAL-PASS without AAI evidence.
- ChatGPT and Codex stay NOT-INSTALLED unless this host proves them.

Execute now, in order:
1. Read `family/handoff.md`, `family/composition-catalog.md`, `references/composition-map.md`, `family/state/composition-plan.json`.
2. Run `python3 family/scripts/validate_family.py`.
3. Run `python3 family/scripts/refetch_untrusted_cache.py currency`. If filing work is in scope, run filing mode and use Firecrawl/Exa/browse when urllib fails.
4. Search this workspace for a `matter-*-verified-facts.md`. If none exists, stop and report that the next real test needs a matter file. Do not invent a matter. Do not add architecture while waiting.
5. If a matter file exists, write a composition plan, then run only the domain skills the matter actually triggers. Persist drafts as DRAFTED or FINAL-DRAFT. Never SUBMITTED.
6. Refresh pins only after a clean family gate.

Completion evidence for this session: family gate result, composition plan path if multi-skill, refetch ledger path, matter found or matter-missing blocker, and a list of files actually changed. One open loop only.

Operator is Krass. You carry sequencing. Do not ask which plugin to use. Do not offer an orchestrator.

---
