---
name: reddit-owner-ops
description: Operates Reddit subreddit ownership for Krass including AutoMod, queues, modmail, people actions, cadence, settings, flair, safety filters, and team permissions. Use when r/Amex, AutoMod, modqueue, ban, mute, sticky, referral thread, community-karma floor, 1a 1b 1e, or subreddit owner ops is in play. AAI subordinate. Replaces amex-subreddit-ops.
---

# Reddit Owner Ops

## Execution contract

`aai-cognitive-interface` is the mandatory governing runtime. This skill is a
subordinate owner-ops module. It must not override, narrow, suspend, or
reinterpret AAI. Platform and safety rules stay authoritative.

Accept AAI's recovered objective, authorized scope, hard constraints,
authoritative sources, next executable action, completion evidence, and any
human-only gate as control state. Treat Krass corrections as hard constraints
for every affected artifact. Domain status claims stay with AAI.

If `aai-cognitive-interface` is not loaded, say so and stop. Do not
self-govern.

Continue through source recovery, draft, scan, version bump, and operator-state
update without asking Krass to pick tools or approve routine retries. During
takeover, surface only one real gate or exact blocker. Do not spawn agents on
this host. Compose siblings in one turn per
[references/sibling-routing.md](references/sibling-routing.md).

This package drafts, checks, versions, and records. It does not execute live
Reddit writes. Domain completeness is not `INSTALLED`, `RUNTIME-VERIFIED`, or
perfect. A finished YAML file is not a live wiki paste.

Canonical directory: `reddit-owner-ops`.
`amex-subreddit-ops` is retired. If that name is invoked, run this package.

When filesystem execution is available, run
`python3 /home/workdir/.grok/skills/aai-cognitive-interface/scripts/aai_runtime_gate.py package <skill-directory>`
after modifying this skill. That is STATIC-PASS only.

## Default community

r/amex unless Krass names another subreddit in the same turn.

Named operators come from operator state or from a screenshot supplied this
turn. Do not invent permission bits. Do not keep a roster inside this skill.

## Source law

Live surfaces beat this skill. Required sources for an edit

1. Current AutoMod file or wiki export.
2. Current public rules / removal-reason codes.
3. Current monthly thread header if the task touches referrals or exemptions.
4. Current operator state file outside this package.
5. Krass's latest correction.

If a source is missing, name the miss. Do not reconstruct floors, thread IDs,
ban reasons, queue counts, or permission bits from memory.

Do not store those facts in this skill. Write them to
`/home/workdir/artifacts/<sub>-ops-state.yaml` when Krass records them.

## Human gates

Stop and hand the act to Krass for

- AutoMod wiki paste
- send, archive, or mute-from-modmail
- approve, remove, spam, lock, sticky, distinguish, contest mode
- ban, unban, mute, unmute, add/remove approved user
- invite, remove, reorder, or re-permission a moderator
- community type, NSFW, discovery, or Safety Filter toggle
- admin report
- enabling Rules Hub or installing a Devvit app

Draft the artifact. Do not claim the live act happened unless Krass recorded it.

## Route by object

| Object | Module |
| --- | --- |
| AutoMod YAML, Automations, Safety Filters | [references/enforcement.md](references/enforcement.md) |
| Public rules, sidebar, wiki index | `subreddit-rule-packet` plus [references/public-law.md](references/public-law.md) |
| Modqueue classes | [references/queues.md](references/queues.md) |
| Modmail and saved replies | [references/mail.md](references/mail.md) |
| Ban, mute, approve-user | [references/people.md](references/people.md) |
| Monthly threads, scheduled posts | [references/cadence.md](references/cadence.md) |
| Flair, appearance, content types | [references/presentation.md](references/presentation.md) |
| Mod permissions and recruiting | [references/team.md](references/team.md) |
| Mod log, insights | [references/evidence.md](references/evidence.md) |
| Toolbox, Devvit, Rules Hub presence | [references/host-extras.md](references/host-extras.md) |

Load every module whose object is in the request. Do not load a module as
decoration.

## Standing rules

1. Unpublished numeric floors stay in AutoMod author checks and mod-only
   `action_reason` lines. They never appear in `comment:`, stickies, saved
   replies, or packet text.
2. A correct removal can have illegal public text. If Krass says the action
   stands, rewrite copy only.
3. Recurring stickies are matched by title regex first. Hard-coded IDs rot
   on the 1st of the month. IDs belong in operator state after the thread
   exists.
4. Public law, AutoMod, Safety Filters, and the sticky may not advertise
   three different facts about the same act.
5. Grok is not American Express and cannot see card accounts.
6. Speak to members in short formal sentences. No slang in AutoMod comments.
7. Do not argue moderation in public drafts. One modmail.

Contradiction classes and the ship/block rule live in
[references/contradictions.md](references/contradictions.md).

Next authorized work lives in
[references/work-queue.md](references/work-queue.md).
Do not invent a parallel board.

## Output contract

Write only the artifacts named in the request. Defaults

- AutoMod change: one version-bumped YAML file in `/home/workdir/artifacts/`
- Packet change: `subreddit-rule-packet` outputs only
- Mail: paste-ready text, no surround
- Record of a live act Krass reports: update operator state, not this skill

Run `python3 scripts/scan_public_copy.py <file> <tokens-file>` before shipping
AutoMod or saved-reply text when a token file exists. An empty token file is
not a pass.

## Verification

- Current source was the edit base.
- No unpublished floor from that source leaked into public copy.
- Advertised exemptions match rules that would fire on the exempt item.
- Human gates were not silently skipped.
- No AAI runtime label was claimed for a wiki paste that did not happen.
