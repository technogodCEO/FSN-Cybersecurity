# Manual Test Cases

Run each file with `python main.py < tests/<file>.csv` from the project root and compare the
printed report against the expected result below. Point values reference the constants in
`main.py`; thresholds (`LOW_MAX=4`, `MEDIUM_MAX=14`, `HIGH_MAX=24`) are in `report.py`.

## rule1_failed_login.csv
Single failed login, `School` location, midday (isolates rule 1 only).
- **Expected:** `alice` — score **2** — reasons: `failed login attempt` — tier **Low**

## rule2_unknown_location.csv
Single successful login from `Unknown` location, midday (isolates rule 2).
- **Expected:** `bob` — score **3** — reasons: `unknown location login` — tier **Low**

## rule3_unusual_time.csv
Single successful login at 02:00, `School` (isolates rule 3).
- **Expected:** `carol` — score **2** — reasons: `unusual time login` — tier **Low**

Note: rule 3 has no `event`/`result` condition in the spec — it fires on *any* row in the
00:00–05:00 window, not just logins. Worth confirming that's the intended behavior when you
review this one.

## rule4_password_reset.csv
Single password reset (no prior failed logins), midday (isolates rule 4).
- **Expected:** `dave` — score **5** — reasons: `password reset` — tier **Medium**

## rule5_brute_force_streak.csv
Three failed logins at 12:00, 12:03, 12:06 (all within the 10-min window).
- **Expected:** `erin` — score **12** (rule 1 fires ×3 = 6, rule 5 fires once = +6) —
  reasons: `multiple failed login attempts`, `brute force login streak` — tier **Medium**

## rule6_reset_after_fail.csv
One failed login at 12:00, reset at 12:10 (10 min later, within the 15-min window).
- **Expected:** `frank` — score **12** (rule 1 = 2, rule 4 = 5, rule 6 = 5) —
  reasons: `failed login attempt`, `password reset`, `password reset after failed login` —
  tier **Medium**

## dedup_multiple_reasons.csv
Same user, four successful logins from `Unknown`, spread across the morning.
- **Expected:** `henry` — score **12** (rule 2 fires ×4 = 12) —
  reasons: **only** `multiple unknown location logins` (no duplicate/singular entry left
  behind) — tier **Medium**

## regression_prune_bug.csv
Regression test for the destructive-prune bug: failed logins at 00:00 and 00:11 (11 min
apart — outside rule 5's 10-min window from each other, so no streak), then a reset at 00:14.
The reset is 14 min after the *first* failure — within rule 6's 15-min window — so it must
still be counted even though it fell outside rule 5's narrower window three rows earlier.
- **Expected:** `ivan` — score **20** — reasons: `multiple failed login attempts`,
  `multiple unusual time logins`, `password reset`, `password reset after failed login` —
  tier **High**
- **What would fail here if the bug came back:** if `password reset after failed login` is
  missing, the shared `failedLoginTimes` list is being destructively pruned to a
  rule-specific window again instead of only counted non-destructively.

## regression_streak_then_reset.csv
Regression test for the streak-marker fix: three failed logins (00:00, 00:03, 00:06) trigger
the brute-force bonus at the third one, then a reset follows at 00:10.
- **Expected:** `jack` — score **30** (rule 1 ×3 = 6, rule 3 ×4 = 8 — it also fires on the
  00:10 reset row, since rule 3 has no event-type condition — rule 5 = 6, rule 4 = 5,
  rule 6 = 5) — reasons: `multiple failed login attempts`, `multiple unusual time logins`,
  `brute force login streak`, `password reset`, `password reset after failed login` —
  tier **Critical**
- **What would fail here if the bug came back:** if `password reset after failed login` is
  missing, the old behavior (clearing `failedLoginTimes` entirely once a streak fires) has
  come back instead of just advancing the `lastStreakTriggerTime` marker.

## sample_guide_data.csv
The capstone guide's own sample login log (re-ordered to be time-sorted, since the original
appendix lists rows out of chronological order within `student01` — see the "assumes sorted
input" note in `main.py`). Exercises rules 1, 2, 3, 4, and 6 together across two users.
- **Expected:** `student01` — score **22** — tier **High**
- **Expected:** `student04` — score **10** — tier **Medium**
- Report should list `student01` first (ranked descending by score).

## large_sample.csv (generated)
Not hand-written — produced by `tests/generate_large_sample.py` (fixed random seed, so it's
reproducible: rerun the script to regenerate the same file). Simulates ~200 benign users with
random incidental noise (occasional single failed logins, occasional `Unknown` location hits),
plus three deliberately seeded attackers: `brute_force_bob` (rule 5), `reset_after_fail_rita`
(rule 6), and `combo_carla` (both). This is the scale/false-positive check, not a per-rule
correctness check.
- **Expected:** the three seeded attackers should rank at the very top of the report, clearly
  separated from the benign-noise scores below them (at last check: `combo_carla` 64pts,
  `brute_force_bob` 41pts, `reset_after_fail_rita` 23pts, vs. the highest benign-noise score
  sitting well below in the low-to-mid teens).
- **What to watch for:** if a large fraction of benign users start landing in High/Critical
  alongside or above the real attackers, a rule has become too sensitive to normal variation
  at scale (this is exactly what happened with the old rule 7, which is why it was removed —
  see `specs.md`).
