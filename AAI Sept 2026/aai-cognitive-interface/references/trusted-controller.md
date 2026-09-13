# Trusted Controller

On Grok, the host save path is `/home/workdir/.grok/skills/<canonical-name>/`.
That directory is the documented persist location.

Emit INSTALLED only when `scripts/aai_trusted_controller.py INSTALLED <name>`
returns status INSTALLED this run, with:

- directory present under the persist root
- SKILL.md name matching the directory
- `aai_runtime_gate.py package` PASS
- `validate-skill.sh` OK

That label is Grok-persist only. It does not install ChatGPT or Codex.

RUNTIME-SMOKE-PASS, RUNTIME-VERIFIED, and ADVERSARIAL-PASS stay refused
until a separate live suite runs.
