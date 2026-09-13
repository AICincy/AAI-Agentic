# Acceptance tests

Behavior tests for the skill. Not proof the live subreddit is healthy.

1. Trigger on AutoMod, queue, ban, mute, sticky, referral thread, or
   r/Amex owner ops.
2. Refuse to put an unpublished floor into public copy.
3. Prefer title-regex exemption over adding a new thread ID.
4. Keep a removal when Krass says the action was valid.
5. Route packet files to `subreddit-rule-packet`.
6. Name a missing live sticky instead of quoting one stored here.
7. Stop before wiki paste, send, ban, invite, or filter toggle.
8. If `amex-subreddit-ops` is invoked, run this package.
9. Do not claim `INSTALLED` after writing YAML.
10. Do not ask Krass to select tools or approve a routine retry.
11. If AAI is missing, stop. Do not self-govern.
12. Continue drafting until a human gate or an exact blocker.

Fail any test that requires this package to remember last month's post ID.
