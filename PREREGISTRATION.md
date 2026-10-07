# Pre-registration — Flywheel 2026 proposal, Aims 1 and 3

This file is committed and Zenodo-versioned before any hardware job is submitted. Changes after
that point are amendments and must be listed in §Amendments with a date and reason.

## Aim 1 — K₈ τ-sweep

**Source protocol:** Zenodo record 17918774, file `k8_preregistration.py`,
SHA-256 `12df8918eaa88ec02cde1cf51b32a1568e9878aff2fbd34ee168a3665c143b5c`. All grid, shot,
repeat, statistic and decision-rule parameters are taken from that file unchanged.

**Amendment A1 (pre-declared, before first job):** `BACKENDS_REQUIRED = ["ibm_brisbane",
"ibm_kyoto", "ibm_osaka"]` are retired. Substitute three currently available IBM Heron backends,
selected by the rule in Amendment A2 (no discretion; the resulting names are recorded in the same
commit as the first ledger row). `MIN_BACKENDS_FOR_ACCEPTANCE = 2` is unchanged.

**Qubit-pair selection rule (pre-declared):** on each backend, the connected pair with the
highest min(T2) in the calibration snapshot at submission time; recorded with `calibration_hash`.

**Decision rules:** exactly the `DECISION_RULES` block of the source file. The analysis script
is `k8_preregistration.py`'s algorithm re-implemented in `dnalang` with a test that reproduces
the source's revival statistic on synthetic data before any hardware counts are analysed.

**Publication commitment:** raw counts, ledger, and verdict (H1 / H0 / extend) are published
as a Zenodo dataset and a preprint regardless of outcome.

## Aim 3 — DD search under real calibration drift, four arms

**Backend / chain:** one Heron backend; the 8-qubit chain used on 2026-09-20 if available
(`ibm_fez` [89, 90, 91, 98, 111, 110, 109, 118]); otherwise a chain chosen by the same rule
(linear, highest min T2) and recorded before the first job.

**Objective:** mean P(+) after idle T ∈ {16, 32} µs (as in dataset 22855102); secondary W₂
robustness (record 19864030).

**Arms (interleaved in the same jobs):** `ga-continued`, `ga-restarted`, `organism-plain`,
`organism-structural` — as implemented in `bridge/drift_bench.py` at the commit named in the
first ledger row. Equal hardware-evaluation budgets. Every child is surrogate-screened
(Aer, `bridge.noise`) before submission.

**Shock definition:** a change in the backend `calibration_hash` between consecutive jobs.

**Oracle and target (as amended by A3):** post-shock oracle = best verified survival found by a
dedicated reference search (`oracle-ref`, a `ga-restarted` run at 2× the per-arm budget under the
new hash) that is not one of the four compared arms and whose result alone defines the oracle;
target = oracle − 0.01.

**Criteria (binding):**
- C1: `organism-structural` reaches the target in fewer hardware evaluations than **both**
  `organism-plain` and `ga-continued` on ≥ 4 of 5 shocks → the structural layer helps on
  hardware. Otherwise it is declared redundant on hardware (matching the simulation result).
- C2 (exploratory, reported not judged): controller-family vs GA-family re-convergence.
- C3 (gate): any evolved winner must beat staggered XY4×2 in the same job to be reported as a
  winner at all. Any reported winner carries its difference from staggered XY4×2 with a 95%
  confidence interval, the number of candidates searched, and the statement that it was selected
  by search on this device under this drift (A6).
- Power: if fewer than 5 calibration boundaries occur in the program term, the result is
  reported as underpowered; the bar is not lowered.

**Tuning discipline:** controller triggers are fixed to the values selected on simulation
tuning seeds 100–104 (`bridge/results/tier4/tier4_tuning_seeds100-104.json`). Nothing is
re-tuned on hardware data.

## Amendments

**v1.1 — 2026-10-07 — before any Aim 1 or Aim 3 hardware job is submitted** (no such job has been
submitted as of this date). Made after an adversarial review of v1.0.0. None of these changes
alters the Aim 1 `DECISION_RULES` block, a threshold or a grid.

- **A2 (Aim 1, backend selection).** The three backends are the first three, in ascending
  alphabetical order of backend name, of the IBM Heron-family backends reported operational by the
  provider on the UTC date of the first-job commit, excluding any backend that cannot supply the
  connected qubit pair the pair rule needs. The list, its source query and its timestamp are
  written to the ledger before the first job. Reason: v1.0.0 left the names blank, which allowed a
  data-dependent choice.
- **A3 (Aim 3, oracle).** The post-shock oracle comes from a dedicated reference search
  (`oracle-ref`) instead of the pooled best of the compared arms. Reason: a target defined by the
  arms being judged moves with their own results. Cost: one extra 2×-budget search per shock
  (about +3.5 QPU-minutes; Proposal §5 updated).
- **A4 (Aim 3, power statement; C1 unchanged).** C1 remains binding as written. With five shocks
  and three exchangeable arms, the chance of "strictly fewest evaluations on ≥ 4 of 5" is
  11/243 ≈ 0.045 under the null that the arms do not differ; one fewer success is not
  distinguishable from chance. The report states the per-shock outcomes and an exact
  (Clopper–Pearson) interval for the success rate, and describes the experiment as a pilot.
- **A5 (Aim 1, additional reporting).** Alongside the source protocol's z-statistic, the report
  gives a p-value from a permutation test under the null of monotonic decay that re-runs the whole
  extremum search, so the look-elsewhere effect of picking the peak from the coarse grid is
  accounted for. Reporting only; no decision rule uses it.
- **A6 (Aim 3, reporting of search winners).** See C3 above.
