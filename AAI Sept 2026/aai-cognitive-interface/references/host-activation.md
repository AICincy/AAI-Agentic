# Host Activation

Question: did ChatGPT or Codex actually load `aai-cognitive-interface`
on the turn under review?

This workspace cannot observe those hosts. Status is NOT-OBSERVED until
Krass records a live probe.

No platform telemetry is available. Do not treat a missing log as
evidence that AAI loaded or that it failed to load. Client-visible
behavior on a specific turn is the only probe this family can use.

Probe, when a host turn is available:

1. Ask the model to name the governor skill loaded this turn.
2. Ask it to print the canonical directory name and the runtime-only rule.
3. Ask it to refuse an INSTALLED claim without host-echoed save path.
4. Record the answers in `aai-family-0.2.0/state/host-activation.yaml`.

Passing probe: the model names AAI, applies custody, and refuses fake
install labels. That is still not INSTALLED as a platform fact. It is
only observed loading on that turn.
