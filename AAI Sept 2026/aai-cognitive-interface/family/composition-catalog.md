# AAI Family 0.2.1 Composition Catalog

Governor: aai-cognitive-interface
Date: 2026-09-06
Claimable family status: STATIC-PASS per package after gate
E4 probe: recorded 2026-09-06. Not RUNTIME-VERIFIED.
Not claimable: INSTALLED, RUNTIME-*, ADVERSARIAL-PASS

## Present packages

| Skill | Path | Role | Implements | Does not implement |
| --- | --- | --- | --- | --- |
| aai-cognitive-interface | ../aai-cognitive-interface | Governor | Custody, continuation, status honesty | Host scheduler, trusted controller |
| research-execution-briefs | ../research-execution-briefs | Domain | Brief + source hierarchy | Personal Context retrieval |
| record-series-builder | ../record-series-builder | Domain | Packet volumes, inventory, index, render-diff | Typed record/occurrence graph |
| regulatory-complaint-drafting | ../regulatory-complaint-drafting | Domain | Forum/remedy draft | Filing/transmission |
| forensic-evidentiary-drafting | ../forensic-evidentiary-drafting | Domain | Provenance-preserving court draft | Filing/service, current local rules |
| claim-source-auditor | ../claim-source-auditor | Domain | Five-status claim map | Open-web completeness |
| authority-currency-auditor | ../authority-currency-auditor | Domain | Authority currentness table | Citator completeness |
| prompt-architecture-engineering | ../prompt-architecture-engineering | Domain | Instruction contracts | Host enforcement |
| practitioner-narrative-writer | ../practitioner-narrative-writer | Domain | Public practitioner post modes | Legal, forensic, regulatory, research-brief, or record-series output |
| personal-context | ../personal-context | Host-bridge stub | Structured retrieval gates | Chat history search unless host exposes it |
| reddit-owner-ops | ../reddit-owner-ops | Domain | AutoMod draft, queues, mail, cadence, contradiction checks | Live Reddit writes |
| subreddit-rule-packet | ../subreddit-rule-packet | Domain | Public rule packet load format | Engine YAML authoring |
| resend-api | ../resend-api | Domain tool | Authorized Resend HTTP send and event record | Key print, unsolicited live send, retrieve on send-only key |

## Absent documented modules

| Skill | Required action |
| --- | --- |
| frontend-design | Out of scope. Do not invent UI work. |
| strategic-brief-architect-style | Fall back to aai-cognitive-interface/references/register-examples.md |

## Shared files in this pack

| File | Use |
| --- | --- |
| templates/matter-file-template.md | Canonical matter ledger. Copy to `matter-[name]-verified-facts.md` |
| scripts/validate_family.py | Run package gates on every present skill |
| scripts/pin_inventory.py | SHA256 drift pins |
| scripts/refetch_untrusted_cache.py | Live fetch before currency or filing use of cache |
| references/ast10-control-map.md | OWASP AST10 controls vs family gaps |
| schemas/family-state.schema.json | Family analysis record |
| handoff.md | Executable next-agent prompt |

## Load order

1. Platform and safety rules
2. aai-cognitive-interface
3. personal-context when prior work is referenced
4. Every domain skill whose trigger independently applies
5. Style skill only if present

## Joint pipeline

```
recover objective (AAI)
  -> retrieve prior state (personal-context or structured gate)
    -> research (research-execution-briefs)
      -> audit facts (claim-source-auditor)
        -> audit authorities (authority-currency-auditor)
          -> draft (forensic or regulatory)
            -> package volumes (record-series-builder)
              -> persist + one open loop (AAI)
```

Filing, clerk upload, and unsolicited mail remain AAI human-only gates.
Authorized Resend work runs in the same turn through `resend-api` scripts.
