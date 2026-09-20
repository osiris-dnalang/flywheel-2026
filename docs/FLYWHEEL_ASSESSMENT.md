# BlueQubit Quantum Flywheel — Portfolio Assessment

*Prepared 2026-09-20 from a full read of all 60 Zenodo records (creator "Davis, Devin Phillip"), the two local zips, and re-analysis of raw IBM job payloads. Companion files: `PUBLICATIONS.md`, `publications.json`, `zenodo_archive/CROSSREF_BACKUP.md`.*

## What the program is

$150K (BlueQubit + AWS + IBM), 3 months, 4–5-week open call. Three tracks:

1. **Quantum advantage on NISQ hardware** — push devices toward classically intractable results.
2. **Breaking quantum advantage claims** — adversarial classical simulation (tensor networks, heuristics).
3. **AI for error correction** — discover/evaluate QEC codes with AI.

Teams get IBM QPU time, AWS GPU/CPU, frontier AI assistants, BlueQubit's GPU simulator. Expected output: **preprints, repos, reproducible benchmark data**. The reviewers are, by the program's own design, Track-2 people — they break claims for a living.

## What the portfolio actually is (facts first)

| | Count | Notes |
|---|---|---|
| Zenodo records | 60 | 40 in the original paste + 20 found via creator search |
| Records with real IBM job IDs | 21 | backends: fez, torino, kingston, marrakesh, nazca, brisbane, kyoto, osaka, kyiv |
| Distinct hardware-data records that stand on their own | 5 | 17857733, 18038719, 18209318, 18450505, 18782259 |
| Records whose payload is byte-identical to another record | 14 | 13× `qbyte_substrate_engine_darpa.zip`, 1× Q-SLICE re-upload, 4× forensic posters |
| Records that are earlier versions of a lineage | 8 | τ-phase v1→v4 chain |
| Author self-critiques ("honest assessment") | 3 | 17859312, 18783307, 18784195 |
| Legal / forensic (non-scientific) | 8 | must be excluded from any proposal |
| Local zips containing publishable data | 0 | backup is a `.venv` + synthetic sandbox; production-main is a web app |

### The τ-phase arc, in one paragraph

Dec 8 2025: 490K shots on ibm_fez/torino, ANOVA p = 1.3×10⁻¹⁴ that fidelity depends on τ-phase; golden-ratio numerology (τ₀ = φ⁸ μs, F_max = 1−φ⁻⁸). Same day, v2 claims a 6.87σ revival (K₈ = 1) from curve-fit covariance; v4.0 retracts it (bootstrap 1.34σ, step function, threshold not pre-registered) and estimates P(new physics) ≈ 25%. Dec 13: a hash-verified **pre-registration** of the decisive τ-sweep (5σ, ≥2 of 3 backends, binding decision rules). Feb 26 2026 (record 18781261): an informal single-backend version of that sweep **refutes** the revival (T1 artifact, R² = 0.976), the φ⁸ ZZ period (CV = 123%), θ_lock = 51.843° (z = −1.0) and the earlier 10⁶× Zeno claim (18209071). April 2026 records (v5.0.0 preprints, 156-qubit "world record", "Nobel Brief") nevertheless continue to use θ_lock, τ₀ = φ⁸ and χ_PC as if the February refutations had not happened.

### Findings from re-analysis that a reviewer will also make

1. **19656600 — "136-bit negentropy gap" is a sampling artifact.** Decoding the raw `BitArray` (1,000,000 × 156 bits): every shot is a unique bitstring, so the plug-in joint entropy is exactly log₂(10⁶) = 19.9316 bits — the number in the abstract. Per-qubit marginal entropies sum to 149.7 of 156 bits: the output is *near maximally mixed*, the opposite of "manifold collapse". This is the headline of the `osiris-cli` README. It must be withdrawn or re-framed before any submission; it is the first thing a tensor-network reviewer will check.
2. **18781261 CHSH |S| = 0.106** on ibm_fez is not a physics result — IBM Heron devices routinely give |S| ≈ 2.5. This is almost certainly a basis-rotation or correlator-sign bug in `physics_frontier.py`. It should be fixed and re-run, not reported as "not found".
3. **13 records, one file.** The Dec-10 batch is a single 580 KB zip deposited 13 times under different titles. Reviewers who open two of them will discount the whole DOI count.
4. **Version labels disagree**: Zenodo says v5.0.0 (Apr 11), then v4.1 (Apr 19–22); `pyproject.toml` and `CITATION.cff` say 4.0.0; git tag is `v4.1.0-sovereign`.
5. **The local backup contains fabricated benchmark output** (`random.uniform(0.54, 0.58) × 1.169`, labelled "LOCKED"). It has not been published, and it must stay that way.

## What is genuinely strong

- **Self-adversarial track record.** Three honest-assessment records and one hardware record that refutes six of the author's own claims (18781261). That is *exactly* the Track-2 disposition the program is funding, and it is rare.
- **A hash-verified pre-registration that has never been run** (17918774). Reviewers love pre-registration; the program can fund the run.
- **Clean, reproducible hardware results** with job IDs: 8-qubit and 18-qubit GHZ witnesses across two Heron chips (18781261, 18782259), teleportation F = 0.773 with mid-circuit feed-forward, XEB to depth 16, 5-qubit ZNE+majority-vote GHZ (18209318), device-scoped Bell pairs with a hash-chained provenance ledger (18038719).
- **The W₂ robustness metric** (19864030) is a real methodological contribution: hardware-native, reference-free, and the paper falsifies its own motivating hypothesis. This is the best-written record in the set.
- **A working local stack**: pure-NumPy simulator, DNA-Lang compiler, 9-agent swarm, decoders, PCRB error-correction module, Zenodo publishing pipeline. Infrastructure for "AI for QEC" already exists in `osiris.decoders`, `osiris.defense`, `osiris.discovery`.

## Track fit and recommendation

**Do not propose on Track 1 as "quantum advantage".** The confirmed results (GHZ-18, teleportation, XEB F>0) are solid NISQ demonstrations but not advantage claims, and the advantage-flavoured claims in the portfolio (10⁶× suppression, 136-bit gap, θ_lock, φ⁸) have all failed or are artifacts.

**Propose on Track 2, with a Track-1 hardware component.** Concretely:

> **"Pre-registered adversarial replication: closing the K₈ τ-sweep and stress-testing NISQ entropy-suppression claims."**
>
> *Aim 1 (hardware, IBM time):* Execute the Dec-2025 pre-registered K₈ protocol as written — coarse + fine τ grid, 8192/16384 shots, ≥2 Heron backends (substituting current backends for the retired brisbane/kyoto/osaka, documented as a pre-declared amendment). Publish the result whichever way it falls. Prior informal evidence (18781261) predicts a null; a pre-registered null with 5σ power is a publishable, citable closure of a public claim.
>
> *Aim 2 (classical, AWS/BlueQubit GPU):* Adversarial re-analysis of the author's own 156-qubit and 1,430-circuit "entropy suppression" datasets (19656600, 19505907) with proper entropy estimators (Miller–Madow, NSB, coverage-adjusted) and tensor-network / Clifford+T simulation of the 51.843° torsion-lock circuits to show the outputs are classically reproducible. Deliverable: a "how to not fool yourself with plug-in entropy on 10⁶ shots" methods note plus reproducible notebooks.
>
> *Aim 3 (Track-3 seed, optional):* Apply the W₂ robustness metric (19864030) as an objective for evolutionary search over small stabilizer codes / dynamical-decoupling sequences using `osiris.discovery` + `osiris.decoders`, with hardware validation of the top-k on IBM. Modest, honest scope.

Why this wins: it turns the portfolio's liability (public claims that failed) into the asset the program is explicitly buying (people who break claims, including their own), it needs exactly the resources on offer (QPU time + GPU simulation), and every deliverable is a preprint + repo + benchmark dataset.

## Required clean-up before submitting (in order)

1. **Add an erratum/version note to 19656600** re-framing the 19.93-bit figure as the sampling ceiling, and remove "world record" from the `osiris-cli` README. Do this *before* anyone else finds it.
2. **Consolidate the 13 duplicate DARPA records** into one concept DOI (Zenodo lets you add a "is identical to" relation); stop citing them as 13 works.
3. **Mark 18209071 as superseded by 18781261** in its Zenodo metadata (`isSupplementedBy` / `isObsoletedBy`).
4. **Fix the CHSH analysis bug** and re-run on hardware (cheap: 4 circuits) so the "not found" row becomes a normal |S| > 2 Bell violation.
5. **Unify the version string** (pyproject, CITATION.cff, git tag, Zenodo) — pick one.
6. **Exclude the 8 legal/forensic records and the "Nobel Brief" from the proposal** — cite `PUBLICATIONS.md` status `honest-assessment`, `hardware-mixed`, `dataset-hardware`, `pre-registration` records only.
7. **Delete or clearly label the synthetic scripts** in `dnalang_osiris_backup.zip` (`longevity_tau_sweep.sh`, `dna_benchmark_runner.sh`, the injected-anomaly branch of `osiris_falsification.py`).

## What I did not verify

- The physics content of the theory records (6dCRSM, 11D Wheeler–DeWitt, Penteract) beyond the author's own sensitivity/concordance analyses.
- Whether the 10 job IDs in 18781261 resolve on IBM's side (requires the account).
- The 360 MB v5.0.0 tarball contents (md5-verified against Zenodo only).
