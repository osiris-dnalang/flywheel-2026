# Pre-registration — Flywheel 2026 proposal, Aims 1 and 3

This file is committed and Zenodo-versioned before any hardware job is submitted. Changes after
that point are amendments and must be listed in §Amendments with a date and reason.

## Aim 1 — K₈ τ-sweep

**Source protocol:** Zenodo record 17918774, file `k8_preregistration.py`,
SHA-256 `12df8918eaa88ec02cde1cf51b32a1568e9878aff2fbd34ee168a3665c143b5c`. All grid, shot,
repeat, statistic and decision-rule parameters are taken from that file unchanged.

**Amendment A1 (pre-declared, before first job):** `BACKENDS_REQUIRED = ["ibm_brisbane",
"ibm_kyoto", "ibm_osaka"]` are retired. Substitute three currently available IBM Heron backends,
named here at the time of the first job: ______ , ______ , ______ (to be filled and committed in
the same commit as the first ledger row). `MIN_BACKENDS_FOR_ACCEPTANCE = 2` is unchanged.

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

**Oracle and target:** post-shock oracle = best verified survival across all arms with 2× the
per-arm budget under the new hash; target = oracle − 0.01.

**Criteria (binding):**
- C1: `organism-structural` reaches the target in fewer hardware evaluations than **both**
  `organism-plain` and `ga-continued` on ≥ 4 of 5 shocks → the structural layer helps on
  hardware. Otherwise it is declared redundant on hardware (matching the simulation result).
- C2 (exploratory, reported not judged): controller-family vs GA-family re-convergence.
- C3 (gate): any evolved winner must beat staggered XY4×2 in the same job to be reported as a
  winner at all.
- Power: if fewer than 5 calibration boundaries occur in the program term, the result is
  reported as underpowered; the bar is not lowered.

**Tuning discipline:** controller triggers are fixed to the values selected on simulation
tuning seeds 100–104 (`bridge/results/tier4/tier4_tuning_seeds100-104.json`). Nothing is
re-tuned on hardware data.

## Amendments

(none yet)
