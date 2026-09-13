# ORC 149.43 time-sensitive flag

Checked: 2026-09-06
Source: https://codes.ohio.gov/ohio-revised-code/section-149.43
Route: live HTTP 200 this session

Official page states a new version of Section 149.43 takes effect September 7, 2026.
Exa independently returned https://codes.ohio.gov/ohio-revised-code/section-149.43/9-7-2026
(House Bill 31, 136th General Assembly).

HARD CONSTRAINT, operator-confirmed 2026-09-06:
- Cache is not law.
- On or after 2026-09-07, do not cite the pre-effective 149.43 text as the filing-day rule.
- Re-fetch https://codes.ohio.gov/ohio-revised-code/section-149.43 and the 9-7-2026 version before any 149.43 use on or after that date.
- If the fetch fails, leave the citation UNRESOLVED. Do not fall back to cache.
