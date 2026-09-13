# Composition plan

Mediation-layer object. Not an agent.

Schema: `family/schemas/composition-plan.schema.json`
Writer: `family/scripts/write_composition_plan.py`
Instance: `family/state/composition-plan.json`

Write a plan at the start of a multi-skill turn. First skill is always `aai-cognitive-interface`.

On this Grok host, `spawn_tool_present` is false. Mode must be `compose-skills`.

Contract lives here and in AAI `references/composition-map.md`.
Do not copy the schema into every domain SKILL.md.
