# Pre-registered adversarial replication on NISQ hardware: closing the K₈ τ-sweep, stress-testing entropy-suppression claims, and testing an auditable evolutionary controller against real calibration drift

**BlueQubit Quantum Flywheel — Open Call 2026**
**Primary track:** 2 — Breaking quantum advantage claims. **Hardware component:** Track 1 (IBM QPU). **Seed component:** Track 3-adjacent (AI for error *suppression*: evolutionary dynamical-decoupling search; not QEC codes — stated plainly).
**Applicant:** Devin Phillip Davis, independent researcher (Agile Defense Systems LLC), osiris.dnalang@gmail.com
**Code and data:** github.com/osiris-dnalang — `dnalang-core`, `organism_sim`, `bridge` (Apache-2.0); snapshot DOI [10.5281/zenodo.22862567](https://doi.org/10.5281/zenodo.22862567)
**Program term requested:** 3 months. **Resources requested:** IBM Heron QPU time (~75 min total, itemised in §5), AWS CPU (16–32 cores), modest GPU, AI tokens (offline use only, §5).

---

## 1. Executive summary

Between December 2025 and April 2026 I published, under my own name, a series of NISQ "advantage-flavoured" claims on Zenodo: a Bell-fidelity revival at τ₀ = φ⁸ ≈ 47 µs (the "K₈" effect), a 10⁶× error-suppression factor, a 136-bit "negentropy gap" on 156 qubits, and a family of numerological constants (θ_lock = 51.843°, a φ⁸ ZZ period). In February 2026 I ran an informal single-backend version of my own pre-registered test and refuted four of those claims on `ibm_fez` (record [18781261](https://zenodo.org/records/18781261)). In September 2026 I audited all 60 records, traced every headline claim to a specific artifact (plug-in entropy on 10⁶ shots; a τ-phase that was `unix_timestamp mod 46 µs`; a "correction" pass invisible in the measurement basis), filed errata ([19656600](https://zenodo.org/records/19656600)), refuted the last live physics claim on hardware (ΔF = +0.002 ± 0.006 vs the claimed +0.053, job `dannuhgpqrnc73991ntg`, dataset [22855102](https://zenodo.org/records/22855102)), and rebuilt the software from scratch with no constants and no claims ([22862567](https://doi.org/10.5281/zenodo.22862567)).

One item is unfinished: **the K₈ pre-registration ([17918774](https://zenodo.org/records/17918774), SHA-256 `12df8918…c143b5c`, uploaded 2025-12-13) has never been executed as written.** It specifies a coarse + fine τ grid, 8192/16384 shots, 3/5 repeats, ≥ 2 of 3 backends, 5σ discovery / 3σ evidence thresholds, and binding decision rules. Its named backends (`ibm_brisbane`, `ibm_kyoto`, `ibm_osaka`) are retired. The informal February run predicts a null. **Aim 1 executes the protocol exactly as pre-registered on current Heron backends, under a pre-declared amendment for the backend substitution, and publishes the outcome whichever way it falls.** A pre-registered 5σ-powered null closing a public claim is a citable result; a positive would be far more interesting and would be reported with the same procedure.

**Aim 2** applies adversarial classical analysis (Track 2's own methods) to my two largest datasets — the 156-qubit / 10⁶-shot "negentropy gap" ([19656600](https://zenodo.org/records/19656600)) and the 1,430-circuit "entropy suppression" set ([19505907](https://zenodo.org/records/19505907)) — with coverage-adjusted entropy estimators (Miller–Madow, NSB, Chao–Shen) and Clifford / tensor-network simulation of the "torsion-lock" circuits, to establish quantitatively that the reported gaps are sampling artifacts reproducible without a quantum computer. Deliverable: a methods note, *How not to fool yourself with plug-in entropy on 10⁶ shots*, with notebooks that regenerate every figure.

**Aim 3** (seed) tests the one open question in the rebuilt stack that cannot be answered in simulation. `dnalang-core` is a genome language for evolvable programs with a GA over dynamical-decoupling sequences; on 2026-09-20 it matched — and did not beat — the textbook ZZ-aware staggered XY4×2 on an 8-qubit `ibm_fez` chain (0.946 / 0.888 / 0.795 survival at 8 / 16 / 32 µs, jobs `dano3qtr…`, `dano4gop…`, `dano5dtr…`). `organism_sim` is a deterministic rule-evolving controller whose only measured advantage, across six pre-registered experiments, is *local topological self-repair after a silent link failure* (30/30 seeds, half the latency of a centralized monitor, zero false alarms) — and which measurably adds nothing on concept drift or on simulated calibration drift. Aim 3 pre-registers the hardware version of that last test: evolutionary DD search with and without the controller's structural layer, against **real** calibration drift on Heron, judged by re-convergence time after `calibration_hash` changes. The criterion is written in §4 before any job is submitted. Whatever it shows becomes the seventh row of a public scorecard that currently reads two PASS, four FAIL.

**Why this proposal fits the Flywheel.** The program's reviewers, by its own design, break claims. This is a proposal from someone whose public record for the last seven months is breaking his own — with hash-verified pre-registration, hash-chained execution ledgers, JSON-Schema-validated provenance, CI guards, and negative results kept on disk and cited. The expected outputs are exactly the program's: preprints, open repositories, and reproducible benchmark data, produced to the same standard whether the answer is yes or no.

## 2. Background and honest prior record

| Record | Date | What it claimed | Status now |
|---|---|---|---|
| [17918774](https://zenodo.org/records/17918774) | 2025-12-13 | Pre-registration of the K₈ τ-sweep (SHA-256 verified) | **Never executed as specified** — Aim 1 |
| [18209071](https://zenodo.org/records/18209071) | 2026-01-10 | 10⁶× error suppression | Self-refuted; headline number was placeholder JSON |
| [18781261](https://zenodo.org/records/18781261) | 2026-02-26 | Informal τ-sweep and 9 other experiments | Refutes K₈ revival (T1 artifact, R² = 0.976), φ⁸ ZZ period, θ_lock, the 10⁶× claim; also contains the real results (teleportation F = 0.773, GHZ-18) |
| [19656600](https://zenodo.org/records/19656600) | 2026-04-19 | 136-bit negentropy gap on 156 qubits | Artifact: 156 − log₂(10⁶ shots); all 10⁶ shots unique; erratum filed 2026-09-20 — Aim 2 |
| [19505907](https://zenodo.org/records/19505907) | 2026-04-11 | Entropy suppression in 1,430 circuits | Same estimator; Aim 2 |
| [19864030](https://zenodo.org/records/19864030) | 2026-04-28 | W₂ distributional-robustness metric | Sound; reused as an objective in Aim 3 |
| [22855102](https://zenodo.org/records/22855102) | 2026-09-20 | Four `ibm_fez` jobs: tetrahedral-correction null, staggered DD | Hardware, controlled, this month |
| [22862567](https://doi.org/10.5281/zenodo.22862567) | 2026-09-20 | Rebuilt stack + six pre-registered results | Snapshot cited throughout |

Full audit: `docs/HONEST_ASSESSMENT.md` and `docs/FLYWHEEL_ASSESSMENT.md` in the applicant's working tree (to be published with the proposal). Records marked `legal`, `duplicate-file`, `superseded`, `self-refuted` or `artifact-confirmed` in the machine-readable index `publications.json` are not cited as evidence anywhere in this proposal.

## 3. Aims, methods and pre-registered criteria

### Aim 1 — Execute the K₈ pre-registration as written (Track 2 via Track 1 hardware)

**Protocol (from record 17918774, unchanged):** Bell-state preparation on a fixed qubit pair; idle τ; Bell-fidelity readout. Phase 1 coarse τ grid of 24 points over 0–100 µs (analysis window 20–80 µs) at 8192 shots × 3 repeats; Phase 2 fine grid ±10 µs around the Phase-1 extremum at 0.5 µs steps, 16384 shots × 5 repeats. Revival statistic: z = (F_peak − F_dip)/√(σ²_peak + σ²_dip). **Decision rules (binding, verbatim):** H1 confirmed iff |τ_r − 47| < 5 µs, z ≥ 5.0 combined across backends, and the revival replicates on ≥ 2 of 3 backends; H0 iff monotonic decay on all backends, or |τ_r − 47| > 10 µs, or fewer than 2 backends show a revival; 3.0 ≤ z < 5.0 → extend shots/repeats as specified.

**Pre-declared amendment (the only one):** the named backends are retired; the run uses three current Heron backends (e.g. `ibm_fez`, `ibm_torino`, `ibm_marrakesh`), chosen and recorded in the ledger *before* the first job, with the qubit pair selected by the same criterion on each (highest T2 pair in the calibration snapshot). Every job's `calibration_hash` and circuit hash are written to the `dnalang` write-ahead ledger before submission; raw counts are published with the record.

**Expected outcome and its value:** the February informal run gives H0 (decay fits T1; no revival). A pre-registered, three-backend, 5σ-powered null closes a public claim with a citation; the community gets a worked example of a complete pre-registration → execution → publication cycle on a NISQ device, including a retired-backend amendment handled correctly.

### Aim 2 — Adversarial classical re-analysis of the entropy-suppression datasets (Track 2)

**Data:** the raw 10⁶-shot bitstrings from 19656600 (156 qubits, `ibm_kingston`) and the 1,430-circuit counts from 19505907 — already public.
**Methods:** (i) recompute every reported entropy with plug-in, Miller–Madow, Chao–Shen and NSB estimators and report the coverage (fraction of observed mass in singletons; for 19656600 all 10⁶ shots are unique, so coverage ≈ 0); (ii) show the "gap" equals `n_qubits − log₂(shots)` analytically and numerically; (iii) reproduce the "torsion-lock" circuits (Clifford + RZ layers) classically — stabilizer simulation where Clifford, tensor-network (MPS/PEPS via BlueQubit's GPU simulator) where not — and show the measured marginals are reproduced without hardware; (iv) bootstrap confidence intervals throughout.
**Deliverable:** methods note + notebooks that regenerate every figure from the public records; a PR to the two Zenodo records adding the re-analysis as a linked erratum.
**Criterion:** the note is complete when every entropy figure in the two records has a coverage-adjusted counterpart and a classical reproduction with stated CI; no hardware is used.

### Aim 3 — Evolutionary DD search against real calibration drift, with and without the controller layer (Track 3-adjacent seed)

**What exists.** `dnalang-core`: genome language → circuit IR → Aer/IBM; GA over a DD space (K slots × {I, X, Y} per sublattice × offset) with parity screening; hash-chained ledger. `bridge`: an `organism_sim` LCS controller over that space whose fitness is measured under a physics-faithful simulated environment (quasi-static dephasing + static ZZ as exact unitaries, reproducing the `ibm_fez` ordering); joined provenance on `(genome_key, calibration_hash)`. Pre-registered simulation results already on disk: the controller ties the GA at equal budget (0.9763 vs 0.9758 verified survival, staggered XY4 0.9705); under a *simulated* calibration shock, the controller's structural layer fails to beat the plain controller (1/5 seeds), while both re-converge 2–3× faster than the population GA (11–14 vs 30–38 evaluations, exploratory).

**Hardware protocol.** Chain of 8 qubits on one Heron backend (the `ibm_fez` chain used on 2026-09-20 if available). Objective: mean |+⟩ survival at T ∈ {16, 32} µs, plus the W₂ robustness metric (19864030) as a secondary. Four arms, identical evaluation budgets, interleaved in the same jobs so they see the same drift: `ga-continued`, `ga-restarted`, `organism-plain`, `organism-structural`. Drift is *real*: arms run across calibration boundaries; every job records `calibration_hash`; a "shock" is a change of hash. Surrogate screening before every hardware child (the pipeline lesson from 2026-09-20).
**Pre-registered criterion (binding):** C1 — `organism-structural` re-converges (post-shock best within 0.01 of the post-shock oracle, oracle = pooled best across arms with 2× budget) in fewer hardware evaluations than **both** `organism-plain` and `ga-continued` on ≥ 4 of 5 shocks; else the structural layer is declared redundant on hardware, as it was in simulation, and the result is published as such. C2 (secondary, exploratory): whether the controller family re-converges faster than the GA family, as in simulation. C3: all evolved winners must beat staggered XY4×2 on the same job to count at all.
**Deliverable:** hardware ledgers, the seventh scorecard row, and a short report either way.

## 4. Methodology that applies to all three aims

- **Pre-registration:** criteria are written and committed (git + Zenodo) before the first job; tuning, where any, is confined to designated seeds/backends disjoint from evaluation; nothing is re-tuned on evaluation data; all outcomes are published.
- **Provenance:** every hardware job is preceded by a ledger row (circuit hash, `calibration_hash`, layout, shots); every controller decision is a hash-chained telemetry row; both rows validate against public JSON Schemas and join on `(genome_key, calibration_hash)`.
- **Reproducibility:** seeded, deterministic simulation; CI guards with a latency budget and a regression benchmark on every push; raw counts published with each record under CC-BY; code under Apache-2.0.
- **AI use:** frontier assistants are used *outside* the execution loop only — for code review and for drafting from a deterministic scaffold that injects commit hashes, the scorecard and the constraints (`organism_sim.cli ask "scaffold: …"`). No model is in any control or analysis path; every number in every report is regenerated by a script.

## 5. Resources requested and how they are used

| Resource | Aim | Estimate | Basis |
|---|---|---|---|
| IBM Heron QPU | 1 | 3 backends × (coarse 24 τ × 3 rep × 8192 + fine 41 τ × 5 rep × 16384) = 3 × 3.95 M shots ≈ **3 × 20 min** | 2026-09-20 jobs: 26 QPU-s for 84 × 1024-shot circuits ≈ 0.31 s per 1024 shots incl. overhead |
| IBM Heron QPU | 3 | 5 shocks × 4 arms × ~30 evaluations × 2 T × 1024 shots ≈ 1.2 M shots ≈ **7 min**, plus baselines ≈ 2 min | same |
| AWS CPU (16–32 cores) | 2, 3 | ~200 core-hours | estimator bootstraps; Aer surrogate screening (0.05 s/eval) |
| AWS / BlueQubit GPU | 2 | ~40 GPU-hours | MPS/PEPS reproduction of 156-qubit circuits |
| AI tokens | all | small | offline drafting/review only |

Total QPU request ≈ 70–75 minutes across the term — small by design; the value is in the protocol, not the volume.

## 6. Timeline (3 months)

| Weeks | Work |
|---|---|
| 1–2 | Commit Aim-1 backend amendment and Aim-3 criteria (this document + `PREREGISTRATION.md`, Zenodo-versioned); Aim-2 estimator notebooks on the public data; surrogate calibration for Aim 3 |
| 3–5 | Aim 1 coarse phase on three backends; Aim 2 classical reproductions on GPU |
| 6–8 | Aim 1 fine phase; Aim 3 hardware runs across ≥ 5 calibration boundaries |
| 9–10 | Analysis strictly per the pre-registered rules; methods note draft |
| 11–12 | Preprint(s), Zenodo records with raw data, repository releases, scorecard update; errata cross-links on 19656600 / 19505907 |

## 7. Deliverables

1. **Preprint:** *Closing a pre-registered NISQ claim: the K₈ τ-sweep executed as written* (result either way) — with raw counts.
2. **Methods note + notebooks:** *How not to fool yourself with plug-in entropy on 10⁶ shots* — linked as errata to the two source records.
3. **Report + ledgers:** evolutionary DD under real calibration drift, four arms, pre-registered verdict; `bridge` release.
4. **Repositories** (already public, Apache-2.0): `dnalang-core`, `organism_sim`, `bridge` — tagged releases at each milestone; **benchmark data** (CC-BY) on Zenodo under the existing concept DOI 10.5281/zenodo.22862566.

## 8. Risks

- *Backend availability / queue:* three-backend replication may degrade to two — already the pre-registered minimum. Layouts and hashes are logged so any substitution is visible.
- *Drift too slow for Aim 3 in the window:* fewer than five calibration boundaries → report the shocks observed and state that C1 could not be evaluated at the pre-registered power; do not lower the bar.
- *Single investigator:* mitigated by the fact that every step is scripted, hash-chained and public; a reviewer can re-run any figure.
- *Outcome risk:* none — nulls are deliverables here.

## 9. Team

Devin Phillip Davis — independent; ~300 IBM Quantum jobs since 2025; author of the records above including the self-refutations. No institutional overhead. Open to a BlueQubit- or IBM-side collaborator on Aim 2's tensor-network reproduction.
