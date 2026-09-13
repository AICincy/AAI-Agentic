# AST10 control map

Family label: 0.2.1
Source taxonomy: OWASP Agentic Skills Top 10 v1.0
This map is governance. It is not a security certification.

| ID | Risk | Family control already in force | Gap left |
| --- | --- | --- | --- |
| AST01 | Malicious Skills | No marketplace ingest. Only persist-path skills under `/home/workdir/.grok/skills`. | No cryptographic signature on packages |
| AST02 | Supply Chain Compromise | Foreign skill trees stay out. Pattern copy only after review | No registry transparency log |
| AST03 | Over-Privileged Skills | Skills are methods. Send, file, and spawn stay gated. No invented workers | Host tools still have shell and browser |
| AST04 | Insecure Metadata | Frontmatter limited to name and description. AAI gate rejects extra keys and bad YAML | Host may still parse other files |
| AST05 | Untrusted External Instructions | Dated tables live in `untrusted-cache/`. Stubs forbid operative use | Fetch can fail. Then DECISION-GATED |
| AST06 | Weak Isolation | One chat agent. No fake multi-agent | This host is not a container |
| AST07 | Update Drift | `pin_inventory.py` SHA256 pins after a clean family gate | Pins are not immutable publish artifacts |
| AST08 | Poor Scanning | `aai_runtime_gate.py`, `validate-skill.sh`, `validate_family.py`, `routing_eval.py` | No semantic malware scan |
| AST09 | No Governance | Composition-map, catalog, handoff, VERSION, audit trail hook | ChatGPT/Codex remain NOT-OBSERVED |
| AST10 | Cross-Platform Reuse | AAI contract required on every personal skill. Grok Build extras not copied | Same folder name as Grok Build can confuse operators |

Rule: a cache hit is never the authority answer.
