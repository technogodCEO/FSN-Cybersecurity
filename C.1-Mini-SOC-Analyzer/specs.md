# Mini SOC Log Analyzer — Scoring Spec

Rule-based scoring engine (no ML/AI) — every input value maps to a fixed point value below.

## Input CSV Schema

| Column | Type | Expected values |
| :---- | :---- | :---- |
| `time` | string, `HH:MM` (24hr) | `00:00`–`23:59` |
| `user` | string | e.g. `student01` |
| `location` | string | `School` or `Unknown` |
| `event` | string | `login`, `password_reset` |
| `result` | string | `success`, `failed`, `started` |

## Scoring Rules

### Per-Row Rules

Each row is checked against all rules below independently; points stack (a row can trigger more than one rule).

| # | Rule | Condition | Points |
| :---- | :---- | :---- | :---- |
| 1 | Failed login | `event == login` and `result == failed` | +2 |
| 2 | Unknown location | `location == Unknown` | +3 |
| 3 | Unusual time | `time` between `00:00` and `05:00` (inclusive) | +2 |
| 4 | Password reset started | `event == password_reset` and `result == started` | +5 |

### Multi-Row (Pattern) Rules

These look across a user's rows together, not just one row at a time. Since the CSV has no date column, all rows are treated as occurring on the same day; times are compared directly as `HH:MM`. Each pattern rule fires **at most once per matching occurrence** and adds its bonus on top of whatever per-row points already applied.

| # | Rule | Condition | Bonus |
| :---- | :---- | :---- | :---- |
| 5 | Brute-force streak | 3+ failed logins (rule 1) for the same user, all falling within any 10-minute span | +6 (once per streak found) |
| 6 | Reset after failed login(s) | A `password_reset`/`started` row for a user, with 1+ failed logins for that same user in the 15 minutes immediately before it | +5 (once per qualifying reset) |

A user's total score = sum of all per-row points (rules 1–4) + all triggered pattern bonuses (rules 5–6).

There was previously a rule 7 ("location change in short window": +4 for two rows with differing `location` within 12 hours). It was removed after scale testing against ~200 synthetic users showed it produced heavy false positives — normal incidental location variation (e.g. a student occasionally on mobile data vs. school wifi) was enough to push otherwise-benign users into High/Critical tiers alongside real attackers, since the rule had no lower bound on frequency and no real travel-time reasoning. Rule 2 (unknown location, still a flat +3 per row) is considered sufficient signal for that risk without the extra noise.

## Data Model

Per-user streaming state, built incrementally as time-sorted rows are processed:

```python
userSusScores = {
    "student01": {
        "totalScore": 0,
        "reasons": [],                # list of triggered reason strings, deduped by upgrade-to-"multiple" rather than repeated
        "failedLoginTimes": [],       # recent failed-login timestamps (minutes since midnight), trimmed to the largest window in use
        "lastStreakTriggerTime": None, # last failed-login time already counted toward a scored brute-force streak
    }
}
```

`reasons` starts empty; the first occurrence of a rule appends its plain-language label (e.g. `"failed login attempt"`), and a second occurrence removes that entry and replaces it with a `"multiple <reason>s"` version instead of appending a duplicate. `failedLoginTimes` is never destructively pruned to a rule-specific window (that caused a real bug — see Notes) — it's only trimmed to the widest window any rule needs, and individual rules count matching entries in a read-only pass.

## Classification Thresholds

| Total score | Classification |
| :---- | :---- |
| 0 | No Risk |
| 1–4 | Low |
| 5–14 | Medium |
| 15-24 | High |
| 25+ | Critical |

*(Tentative — flat thresholds chosen for simplicity; revisit if dataset size/shape makes percentile-based cutoffs a better fit.)*

## Notes

- Pattern rules (5–6) require a user's rows to be sorted by `time` before evaluation, since they compare each row against others for the same user.
- Pattern rules are score increases, not automatic flags — a triggered pattern just adds points like any other rule; classification still depends on the user's total score crossing a threshold.
- A single set of rows can trigger a pattern rule more than once if there are multiple qualifying occurrences (e.g. two separate brute-force streaks) — each occurrence adds its bonus separately.
- Unrecognized/malformed values (unexpected `event`, `result`, or unparsable `time`) should not silently crash the engine — decide during implementation whether to skip the row, log a warning, or raise.
- An earlier implementation pruned `failedLoginTimes` down to whatever window a given rule check happened to use (e.g. 10 minutes for the brute-force check). Since rules 5 and 6 use different window sizes, this destroyed entries a wider-window rule still needed. Fixed by only ever trimming to the *largest* window across all rules, and having each rule count matching entries non-destructively instead of mutating the shared list.
