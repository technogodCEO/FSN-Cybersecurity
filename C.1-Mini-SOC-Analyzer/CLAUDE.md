# Mini SOC Log Analyzer — Project Context

## What this is
A capstone project for a high-school Summer Cybersecurity Course (see `../Context/` for the
course guide and slide-derived doc). Category C1 from the capstone guide: "Mini SOC Log
Analyzer" — analyze fake login logs, score suspicious accounts, produce a ranked report.
Everything uses fake/sample data only — no real systems, accounts, or attacks (course safety
rule).

User is an experienced developer, rusty on Python, prefers statically-typed languages and
**camelCase over snake_case** (a deliberate choice, not a mistake — code and dict keys use
camelCase throughout; module-level constants stay `UPPER_SNAKE_CASE`, which is normal even in
camelCase codebases). User writes most of the code themselves; Claude's role has been design
discussion, filling in specific functions on request, code review/linting, and testing —
not autonomous implementation.

Repo convention: this is meant to be one repo with a subfolder per capstone project if more
get built later (this folder, `C.1-Mini-SOC-Analyzer/`, is the first one).

## Architecture
- **`main.py`** — ingestion + scoring only. Reads a CSV from stdin (`python main.py < file.csv`,
  or `python main.py < file.csv` works in bash; PowerShell needs `Get-Content file | python main.py`
  since PowerShell doesn't support `<` redirection). Wrapped in `main()` behind
  `if __name__ == "__main__":` so the module is safely importable without side effects.
  Handles a UTF-8 BOM automatically (`sys.stdin.reconfigure(encoding="utf-8-sig")`) — needed
  because PowerShell's `>` redirection writes UTF-8-with-BOM by default, which otherwise breaks
  `csv.DictReader`'s header parsing (`KeyError: 'time'` is the symptom if this regresses).
- **`report.py`** — presentation/classification only: `riskTier()`, the tier thresholds, and
  `generateReport()`, which ranks users by score descending and writes both to console and to
  `soc_report.md` (overwritten each run — no persistence across runs, by design).
- **`specs.md`** — the authoritative scoring spec: CSV schema, all rule conditions/points,
  classification thresholds, the data model, and a Notes section documenting real bugs found
  and fixed (see below). Keep this in sync with `main.py` if rules change.
- **`tests/`** — manual test corpus (not an automated framework): one CSV per rule in
  isolation, dedup-reasons test, two regression tests for the bugs below, the capstone guide's
  own sample data, and a generated large-scale dataset. `tests/README.md` documents expected
  output for each file — run `python main.py < tests/<file>.csv` and compare by eye.
- **`sampleData/`** — a copy of the large-sample generator for producing ad-hoc manual-report
  datasets. `python sampleData/generate_large_sample.py <seed> > output.csv` (seed is an
  optional CLI arg via `sys.argv`, defaults to 42; deterministic per seed).

## Scoring model (see specs.md for full detail)
Per-row rules: failed login (+2), unknown location (+3), unusual time 00:00–05:00 — **no
event-type restriction, fires on any row in that window** (+2), password reset started (+5).
Pattern rules: brute-force streak, 3+ failed logins within 10 min (+6, fires once per streak
via a `lastStreakTriggerTime` marker, not by clearing history), reset-after-fail, 1+ failed
login within 15 min before a reset (+5). Tiers: 0 No Risk / 1–4 Low / 5–14 Medium / 15–24 High
/ 25+ Critical.

There **was** a rule 7 ("location change within 12 hours," +4) — removed after scale-testing
against ~200 synthetic users showed it flagged normal incidental location variance as
suspicious, drowning real attackers in false positives. Rule 2 (unknown location) was judged
sufficient without it. If someone suggests re-adding location-change detection, revisit this
history first.

## Bugs found and fixed (don't reintroduce)
1. **Destructive pruning**: an earlier version of the failed-login-timestamp list was pruned
   down to whatever window a given rule check used (10 min for brute-force, 15 min for
   reset-after-fail). Since the rules use different windows, whichever rule ran first with the
   narrower window permanently deleted data a later, wider-window rule still needed. Fixed by
   only ever trimming to the *largest* window in use, and having each rule count matching
   entries in a read-only pass instead of mutating the shared list.
2. **Streak-clear vs. marker**: originally, triggering a brute-force streak cleared the entire
   failed-login history (to stop it re-firing every row), which had the same destructive-loss
   problem for a later reset-after-fail check. Fixed with a `lastStreakTriggerTime` marker
   instead — advances forward on each new streak trigger, never destroys history.
3. **UTF-8 BOM**: see above.

Both bugs 1 and 2 have dedicated regression tests in `tests/` (`regression_prune_bug.csv`,
`regression_streak_then_reset.csv`) with notes on exactly what output would indicate they'd
come back.

## Status
Code, spec, and manual test corpus are all in sync and passing (`ruff check` clean, all manual
test cases match documented expected output, large-scale test shows clean separation between
seeded attackers and benign noise). **Remaining work: the class presentation** — 5–7 minutes
covering Problem → Who's affected → Why it matters → Recommended controls → Lessons learned,
plus one required visual (poster/diagram/slide/table/checklist), per the course's presentation
structure (`../Context/strongcapstone.md`). Not yet started as of this writing.
