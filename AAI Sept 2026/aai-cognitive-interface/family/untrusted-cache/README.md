# Untrusted cache

Dated tables removed from domain runtimes on 2026-09-03.

These files are search hints only. They are not current law, local rule,
or recipient truth. Re-fetch a live primary source before use.

Before currency or filing work, run:

```
python3 family/scripts/refetch_untrusted_cache.py currency
python3 family/scripts/refetch_untrusted_cache.py filing
```

If the script returns DECISION-GATED, stop. Do not use the cache row as
the answer. See also references/ast10-control-map.md.
