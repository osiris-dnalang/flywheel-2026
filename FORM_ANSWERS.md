# Application form — prepared answers

The Flywheel form is a Google Form behind sign-in; its exact fields could not be read
programmatically. These blocks are prepared for the fields such forms usually have; paste the
matching one and trim to any stated limit. Every number traces to a file cited in PROPOSAL.md.

**Name / affiliation / email:** Devin Phillip Davis — independent researcher, Agile Defense
Systems LLC — osiris.dnalang@gmail.com

**Track:** 2 (Breaking quantum advantage claims), with a Track-1 hardware component (IBM QPU)
and a Track-3-adjacent seed (AI for error *suppression*, not QEC codes).

**Title:** Pre-registered adversarial replication on NISQ hardware: closing the K₈ τ-sweep,
stress-testing entropy-suppression claims, and testing an auditable evolutionary controller
against real calibration drift.

**Abstract (≈ 200 words):**
Between Dec 2025 and Apr 2026 I published NISQ "advantage-flavoured" claims (a Bell-fidelity
revival at τ₀ = φ⁸ ≈ 47 µs, 10⁶× error suppression, a 136-bit entropy gap on 156 qubits).
I have since refuted four of them on IBM hardware myself (Zenodo 18781261), traced the rest to
specific sampling artifacts, filed errata, and rebuilt the software from scratch with no
constants (10.5281/zenodo.22862567). One item remains: a hash-verified pre-registration of the
decisive τ-sweep (17918774) that has never been executed as written. Aim 1 runs it exactly as
pre-registered on three Heron backends under a single pre-declared backend amendment and
publishes the result either way (a 5σ-powered null closes a public claim). Aim 2 applies
coverage-adjusted entropy estimators and tensor-network reproduction to my two largest datasets
to show the reported gaps are classically reproducible. Aim 3 pre-registers a hardware test of
whether an auditable rule-evolving controller — which in six pre-registered simulation
experiments helped only on silent link failure and never on drift — helps evolutionary
dynamical-decoupling search against *real* calibration drift. All jobs are preceded by
hash-chained ledger rows; all outcomes are published. Requested: ≈ 75 min Heron time, modest
AWS CPU/GPU, offline AI use only.

**Links:** github.com/osiris-dnalang/{dnalang-core, organism_sim, bridge} ·
code DOI 10.5281/zenodo.22862567 · proposal DOI 10.5281/zenodo.22863245 · github.com/osiris-dnalang/flywheel-2026

**Compute needs:** IBM Heron QPU ≈ 75 min total (itemised in PROPOSAL.md §5); AWS 16–32-core
CPU ≈ 200 core-h; GPU ≈ 40 h for 156-qubit MPS/PEPS reproduction; AI tokens: small, offline.

**Deliverables:** preprint (Aim 1), methods note + notebooks linked as errata (Aim 2), report
+ ledgers + repository release (Aim 3), raw counts on Zenodo (CC-BY), code Apache-2.0.

**Why us / track record (short):** the applicant's public record for seven months is
breaking his own claims with pre-registration, hash-chained ledgers and published negative
results; the rebuilt stack ships with a six-row scorecard reading two PASS, four FAIL, every
row with its criterion stated before the run and its data on disk.

**Team size:** 1 (open to a partner on tensor-network reproduction).
