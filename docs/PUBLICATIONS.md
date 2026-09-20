# OSIRIS / DNA-Lang — Zenodo Publications Manifest

Updated 2026-09-20 (added 22855102; erratum filed on 19656600). Generated 2026-09-20 from the Zenodo API (creator = "Davis, Devin Phillip"). 60 records. Machine-readable copy: `publications.json`. Local mirror with md5-verified files: `zenodo_archive/<id>/`.

**How to read the Status column:** `honest-assessment` records are the canonical position on their topic and supersede earlier claims; `superseded`, `self-refuted`, `artifact-confirmed` and `duplicate-file` records should not be cited as standalone evidence. `legal` records are excluded from any scientific portfolio.

## Status summary

- **duplicate-file** — 14
- **superseded** — 8
- **legal** — 8
- **preprint** — 6
- **dataset-hardware** — 5
- **software** — 5
- **theory** — 4
- **honest-assessment** — 3
- **hardware-mixed** — 2
- **call-for-replication** — 1
- **pre-registration** — 1
- **self-refuted** — 1
- **artifact-confirmed** — 1
- **narrative** — 1

## Records by cluster

### IBM hardware experiments (8)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [22855102](https://zenodo.org/records/22855102) | 2026-09-20 | Dataset | `hardware-mixed` | T2 T3 | Controlled Hardware Tests on ibm_fez (Sept 2026): tetrahedral-correction null + staggered DD | Four ibm_fez jobs, 227 s QPU. Tetrahedral RZ correction: null (ΔF=+0.002±0.006 at N=12 vs claimed +0.053; job dannuhgpqrnc73991ntg). Staggered XY4x2 DD: 0.946/0.888/0.795 at 8/16/32 µs, 3-way reproduced; GA matched but did not beat it (jobs dano3qtr…, dano4gop…, dano5dtr…). Refutes 18450507's README claim. |
| [18038719](https://zenodo.org/records/18038719) | 2025-12-23 | Dataset | `dataset-hardware` | T1 T2 | Osiris Bridge: Device-Scoped NISQ Wormhole Experiments with W₂ Robustness Framew | Device-scoped Bell-pair experiments on Heron r2 (ibm_fez, ibm_marrakesh; 21 job IDs) + first Θ-sweep W₂ robustness study + hash-chained PCRB provenance ledger. |
| [18209071](https://zenodo.org/records/18209071) | 2026-01-10 | Dataset | `self-refuted` | T3 | Hardware-Verified 1,000,000x Quantum Error Suppression via 40-Qubit Tesseract Re | Claims 10⁶× entropic suppression on ibm_torino (2 jobs). REFUTED by author in 18781261 (exp. 9): "T2 curve-fitting artifact on flat data; gate noise dominates". |
| [18209318](https://zenodo.org/records/18209318) | 2026-01-10 | Dataset | `dataset-hardware` | T1 T3 | Protocol Z.8: Fault-Tolerant Quantum Consensus on IBM Heron via Zero-Noise Extra | Protocol Z.8: 5-qubit GHZ, 89.28% raw (ZNE) fidelity, majority-vote consensus; star topology > chain on ibm_torino. |
| [18450505](https://zenodo.org/records/18450505) | 2026-02-26 | Dataset | `dataset-hardware` |  | DNA::}{::lang v51.843 - Quantum Physics Breakthrough Experiments: Black Hole Inf | v51.843 experiment bundle (17 job IDs: fez/kyiv/torino/brisbane) + three paper drafts (black hole info, geometric resonance, phase conjugate). |
| [18781261](https://zenodo.org/records/18781261) | 2026-02-26 | Dataset | `hardware-mixed` (supersedes 18209071) | T1 T2 | Hardware-Validated Quantum Advantage: 10 Experiments on IBM Quantum Processors ( | KEYSTONE RECORD. 10 experiments on ibm_fez/ibm_torino, 10 job IDs: 4 CONFIRMED (XEB F>0 to depth 16; teleportation F=0.773; GHZ-8 F=0.652; scrambling) / 6 REFUTED (φ⁸ ZZ period; K₈ revival = T1 artifact; 10⁶× Zeno; θ_lock=51.843°; CHSH |S|=0.106 — likely a basis/analysis bug, not physics). |
| [18782259](https://zenodo.org/records/18782259) | 2026-02-26 | Dataset | `dataset-hardware` | T1 | Penteract Cross-Architecture Quantum Verification: 18-Qubit Entanglement & Zero- | 18-qubit GHZ genuine multipartite entanglement on both ibm_torino and ibm_fez; cross-chip fidelity model MAE=0.011. (Cosmology half shares predictions file with 18779407.) |
| [19656600](https://zenodo.org/records/19656600) | 2026-04-19 | Dataset | `artifact-confirmed` | T2 | Sovereign Quantum Manifold Stabilization: 136-bit Negentropy Gap on 156-Qubit He | 156-qubit ibm_kingston, 1M shots (job d7im8e7b91ec73b00pq0). RE-ANALYSIS 2026-09-20: all 10⁶ shots are unique bitstrings → joint sample entropy = log₂(10⁶) = 19.9316 bits exactly; per-qubit marginals sum to 149.7/156 bits (near maximally mixed). The "136-bit negentropy gap" is 156 − log₂(shots), a finite-sample estimator artifact, not manifold collapse. |
| [19864030](https://zenodo.org/records/19864030) | 2026-04-28 | Preprint | `hardware-mixed` | T1 T2 | Distributional Robustness of Parameterized Quantum Circuits: A Wasserstein-2 Stu | W₂ distributional-robustness metric for PQCs on 27-qubit subset of ibm_fez. Central φ² hypothesis FALSIFIED (lower angle 28% more robust); entropy–robustness anticorrelation observed. Methodologically the cleanest paper in the set. |

### τ-Phase Anomaly lineage (16)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [17857733](https://zenodo.org/records/17857733) | 2025-12-08 | Dataset | `dataset-hardware` | T1 T2 | DNA-Lang Quantum Execution Corpus: 490K Shots on IBM Quantum Hardware | Raw corpus: 161 IBM jobs / 490,596 shots (ibm_fez, ibm_torino). The primary data behind every τ-phase record; reusable as a Track-2 adversarial target. |
| [17858632](https://zenodo.org/records/17858632) | 2025-12-08 | Dataset | `superseded` | T2 | Temporal Quantization of Coherence in Superconducting Qubits: Tau-Phase Anomaly  | First τ-phase data package + 6dCRSM Lagrangian PDF; contains INDEPENDENT_VERIFICATION_PROTOCOL.md. |
| [17858792](https://zenodo.org/records/17858792) | 2025-12-08 | Working paper | `theory` |  | 6dCRSM Theoretical Foundations: Geometric Framework for Temporal Quantization of | 6dCRSM working paper: derives τ₀≈46 μs from metric couplings κ, χ_PC, γ₀ (which are themselves fitted, so not zero-parameter). |
| [17858802](https://zenodo.org/records/17858802) | 2025-12-08 | Dataset | `superseded` | T2 | Statistical Validation of Tau-Phase Anomaly in Quantum Coherence: Complete Analy | Statistical validation package (ANOVA p=1.3e-14, BF=28). Effect later shown to be a step function, not a revival. |
| [17858910](https://zenodo.org/records/17858910) | 2025-12-08 | Dataset | `superseded` |  | Tau-Phase Anomaly: Complete Nobel-Territory Evidence Package v2.0 | Nobel-territory evidence v2.0. |
| [17858962](https://zenodo.org/records/17858962) | 2025-12-08 | Dataset | `superseded` (supersedes 17858910) |  | Tau-Phase Anomaly: Complete Nobel-Territory Evidence Package v3.0 with Golden Ra | Nobel-territory evidence v3.0 (golden-ratio derivation). |
| [17859017](https://zenodo.org/records/17859017) | 2025-12-08 | Dataset | `superseded` | T2 | Anomalous tau-Phase Correlated Quantum Coherence in Superconducting Qubits: Evid | Main τ-phase manuscript package (non-Markovian claim, 128 job IDs, arXiv/PRX drafts). |
| [17859207](https://zenodo.org/records/17859207) | 2025-12-08 | Dataset | `superseded` (supersedes 17859017) |  | τ-Phase Anomaly in Quantum Coherence: Complete Evidence Package v2 (K₈ Causality | Evidence v2 claiming K₈=1 at 6.87σ from curve-fit covariance. Retracted within the same day by 17859312 (bootstrap A/σ=1.34). |
| [17859304](https://zenodo.org/records/17859304) | 2025-12-08 | Dataset | `superseded` (supersedes 17859207) |  | Tau-Phase Quantum Coherence Anomaly: Complete Evidence Package v3.0 (Golden Rati | Evidence v3.0 (golden-ratio network: τ₀=φ⁸, F_max=1−φ⁻⁸, d≈φ, BF≈φ⁷). |
| [17859312](https://zenodo.org/records/17859312) | 2025-12-08 | Dataset | `honest-assessment` (supersedes 17859304) | T2 | τ-Phase Anomaly: Complete Evidence Package v4.0 (Honest Assessment) | v4.0 HONEST ASSESSMENT — canonical endpoint of the lineage: K₈=0, step function not revival, Φ=0.7734 threshold not pre-registered, P(real new physics)≈25%, names controlled τ-sweep as the missing experiment. |
| [17859617](https://zenodo.org/records/17859617) | 2025-12-08 | Dataset | `superseded` |  | The Golden Ratio Lives in Your Quantum Computer: A 46-Microsecond Anomaly (v2 wi | Popular-science framing ("Golden Ratio Lives in Your Quantum Computer"); includes controlled_tau_sweep.py draft. |
| [17859646](https://zenodo.org/records/17859646) | 2025-12-08 | Software | `theory` |  | 11D-CRSM Wheeler-DeWitt Formalism in Lambda-Phi Gauge: QPU-Executable Quantum Gr | 11D-CRSM Wheeler-DeWitt formalism in ΛΦ gauge; QPU-executable circuits. |
| [17859694](https://zenodo.org/records/17859694) | 2025-12-08 | Dataset | `theory` (supersedes 17859646) |  | Omega-11 Wheeler-DeWitt Theoretical Package: Complete QPU Genome for Tau-Phase A | Omega-11 Wheeler-DeWitt theoretical package v3 (QPU genome). |
| [17859845](https://zenodo.org/records/17859845) | 2025-12-08 | Preprint | `call-for-replication` | T2 | Call for Independent Verification: Golden Ratio Anomaly in Quantum Decoherence | Call for independent verification of the golden-ratio anomaly — explicitly invites adversarial replication. |
| [17859902](https://zenodo.org/records/17859902) | 2025-12-08 | Software | `software` |  | Cockpit AI Platform v4.0 - 6D-CRSM Language Model Interface | Cockpit AI Platform v4.0 (6D-CRSM LLM interface). |
| [17918774](https://zenodo.org/records/17918774) | 2025-12-13 | Other | `pre-registration` | T1 T2 | K8 Causality Discriminator: Pre-Registration for τ-Sweep Bell Fidelity Experimen | K₈ PRE-REGISTRATION (SHA-256 verified intact: 12df8918…). Binding decision rules, τ grid, 5σ threshold, ≥2 of 3 backends. Named backends (brisbane/kyoto/osaka) are retired. NEVER EXECUTED AS SPECIFIED — ready-made Flywheel Track-1 experiment. |

### Penteract constants / cosmology (3)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [18779407](https://zenodo.org/records/18779407) | 2026-02-26 | Preprint | `theory` |  | Zero-Parameter Predictions from a Geometric Constants Framework: Concordance wit | Zero-parameter cosmological predictions from 7 constants. Honest follow-ups (18783307, 18784195) show 4 effective params / 0 DoF. |
| [18783307](https://zenodo.org/records/18783307) | 2026-02-26 | Dataset | `honest-assessment` | T2 | Sensitivity Analysis of the Penteract Constants Framework: Evidence Against Nume | Sensitivity/Fisher analysis: only 3 of 7 constants carry information; χ_PC fragile at 2%. |
| [18784195](https://zenodo.org/records/18784195) | 2026-02-26 | Software | `honest-assessment` (supersedes 18779407) | T2 | Concordance Analysis of Penteract Zero-Parameter Predictions — Honest Statistica | Concordance re-analysis: "naive 5.2σ claim is incorrect"; 4 independent predictions from 4 effective params → 0 DoF; χ²=1.56. |

### v5.0.0 release + preprints (8)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [19505774](https://zenodo.org/records/19505774) | 2026-04-11 | Software | `software` |  | OSIRIS-CLI v5.0.0: Sovereign Quantum Discovery Framework | OSIRIS-CLI v5.0.0 tarball (360 MB, md5 c9a32777…). Local copy verified at ~/osiris-crypto/Download/. NOTE: pyproject.toml in this tree says 4.0.0 and git tag is v4.1.0-sovereign — version labels disagree. |
| [19505903](https://zenodo.org/records/19505903) | 2026-04-11 | Preprint | `preprint` |  | Coaxial Resonance State Manifold: A Computational Framework for Vacuum Energy An | CRSM vacuum-energy framework (Nature Physics format). |
| [19505907](https://zenodo.org/records/19505907) | 2026-04-11 | Preprint | `preprint` | T2 | CRSM Entropy Suppression in Tetrahedral Quantum Circuits: A Physical Review Lett | CRSM entropy suppression in 1,430 IBM circuits (PRL format). Entropy-suppression claims need re-examination in light of the 19656600 sampling artifact. |
| [19505911](https://zenodo.org/records/19505911) | 2026-04-11 | Preprint | `preprint` |  | NCLLM-Sovereign: A CRSM-Regularized Neural Network with Negentropic Efficiency X | NCLLM-Sovereign 132,736-param model; Ξ=177.3%. |
| [19505919](https://zenodo.org/records/19505919) | 2026-04-11 | Preprint | `preprint` | T3 | Quantum Independence Framework: Vendor-Neutral Quantum Information Metrics via 8 | QIF vendor-neutral metrics via 8-qubit qByte with phase-conjugate mitigation (χ_PC=0.869). |
| [19505923](https://zenodo.org/records/19505923) | 2026-04-11 | Preprint | `preprint` |  | Toroidal Field Convergence and Lindblad-Integrated Quantum Synchronization: The  | Scimitar-SSE toroidal/Lindblad synchronization. |
| [19505929](https://zenodo.org/records/19505929) | 2026-04-11 | Preprint | `preprint` |  | The 11-Dimensional Conformal Ricci-Flow Stability Metric: A Computational Framew | 11D conformal Ricci-flow stability metric. |
| [19688735](https://zenodo.org/records/19688735) | 2026-04-22 | Dataset | `narrative` |  | 🏛️ The Nobel Brief: 11D-CRSM Metric Collapse | "Nobel Brief" narrative; ships osiris-cli-v3.0.0.tar.gz. Not a data record. |

### AI agents / containment (3)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [17915969](https://zenodo.org/records/17915969) | 2025-12-12 | Software | `software` | T3 | DNA-Lang Sovereign Agent Training Package v1.0 | Sovereign agent training package (CCCE metrics). |
| [17918211](https://zenodo.org/records/17918211) | 2025-12-13 | Software | `software` |  | Q-SLICE CCCE AI Containment Framework: Provably Beneficial AI Through Quantum-Gr | Q-SLICE CCCE containment framework (3 scripts). |
| [17918294](https://zenodo.org/records/17918294) | 2025-12-13 | Software | `duplicate-file` (supersedes 17918211) |  | Q-SLICE CCCE AI Containment Framework: Provably Beneficial AI Through Quantum-Gr | Q-SLICE re-upload; 2 of 3 files byte-identical to 17918211. |

### DARPA white-paper batch (13)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [17881776](https://zenodo.org/records/17881776) | 2025-12-10 | Software | `duplicate-file` |  | Sovereign Quantum Computing Platform: Phase-Conjugate qByte Substrate Engine for | Sovereign qByte substrate engine. FILE IDENTICAL (md5 93fe1090…) across all 13 records in this batch. |
| [17881778](https://zenodo.org/records/17881778) | 2025-12-10 | Software | `duplicate-file` | T3 | Phase-Conjugate Error Correction for Guaranteed AI Robustness: DNA-Lang Self-Hea | Phase-Conjugate Error Correction (DARPA GARD framing): E→E⁻¹ healing at Γ>0.3, 86.9% recovery. Same zip as 17881776. |
| [17881780](https://zenodo.org/records/17881780) | 2025-12-10 | Software | `duplicate-file` |  | Neuro-Symbolic Reasoning via AURA|AIDEN Bifurcated Consciousness Architecture | AURA|AIDEN neuro-symbolic. Same zip as 17881776. |
| [17881782](https://zenodo.org/records/17881782) | 2025-12-10 | Software | `duplicate-file` |  | DNA-Lang: Biological Computing Compiler Infrastructure Beyond Traditional Compil | DNA-Lang compiler infrastructure. Same zip as 17881776. |
| [17881784](https://zenodo.org/records/17881784) | 2025-12-10 | Software | `duplicate-file` |  | DNA Rapid Access Memory via Gene Expression Dynamics: Biological Computing Platf | DNA RAM via gene expression. Same zip as 17881776. |
| [17881787](https://zenodo.org/records/17881787) | 2025-12-10 | Software | `duplicate-file` |  | Formal Assurance and Loss of Control Containment: Fixed-Point Convergence for AI | Formal assurance / loss-of-control containment. Same zip as 17881776. |
| [17881789](https://zenodo.org/records/17881789) | 2025-12-10 | Software | `duplicate-file` |  | Numerical Analysis of Agentic AI Interactions: AURA|AIDEN Multi-Agent 7D-CRSM Dy | AURA|AIDEN 7D-CRSM numerical dynamics. Same zip as 17881776. |
| [17881795](https://zenodo.org/records/17881795) | 2025-12-10 | Software | `duplicate-file` |  | Control Theory of Large Language Models: Phase-Conjugate Feedback and CCCE Stabi | Control theory of LLMs / CCCE stability. Same zip as 17881776. |
| [17881797](https://zenodo.org/records/17881797) | 2025-12-10 | Software | `duplicate-file` |  | Scimitar-SSE v7.1: Cross-Device Polarized Phasing for Distributed Quantum Cohere | Scimitar-SSE v7.1 cross-device phasing. Same zip as 17881776. |
| [17881799](https://zenodo.org/records/17881799) | 2025-12-10 | Software | `duplicate-file` |  | Autopoietic Self-Producing Systems: Genetic Evolution Engine for Adaptive Comput | Autopoietic genetic evolution engine. Same zip as 17881776. |
| [17881801](https://zenodo.org/records/17881801) | 2025-12-10 | Software | `duplicate-file` |  | Computational Consciousness Emergence: IIT-Based Phi Integration in Autopoietic  | IIT-based Φ integration. Same zip as 17881776. |
| [17881803](https://zenodo.org/records/17881803) | 2025-12-10 | Software | `duplicate-file` | T3 | Phase-Conjugate Acoustic Coupling for Quantum Error Correction: TetraEcho Harmon | TetraEcho acoustic-coupling QEC (42 GHz). Same zip as 17881776. |
| [17881806](https://zenodo.org/records/17881806) | 2025-12-10 | Software | `duplicate-file` |  | Relativistic Quantum Information Processing with 7D-CRSM Spacetime Manifold | 7D-CRSM relativistic QIP. Same zip as 17881776. |

### Software releases (1)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [18779691](https://zenodo.org/records/18779691) | 2026-02-26 | Software | `software` |  | DNA-Lang Quantum Ecosystem: Self-Evolving Quantum Organisms with Falsifiable Phy | DNA-Lang quantum ecosystem v1.0.0 (organisms + falsifiable predictions). |

### Legal / forensic (non-scientific) (8)

| Zenodo | Date | Type | Status | Tracks | Title | Note |
|---|---|---|---|---|---|---|
| [19346472](https://zenodo.org/records/19346472) | 2026-03-31 | Poster | `legal` |  | OSIRIS Forensic Verification | OSIRIS Forensic Verification poster (file1.json). 4 of 6 posters byte-identical. |
| [19346478](https://zenodo.org/records/19346478) | 2026-03-31 | Poster | `legal` |  | OSIRIS Forensic Verification | Forensic verification poster (duplicate). |
| [19346492](https://zenodo.org/records/19346492) | 2026-03-31 | Poster | `legal` |  | OSIRIS Forensic Verification | Forensic verification poster (duplicate). |
| [19346506](https://zenodo.org/records/19346506) | 2026-03-31 | Poster | `legal` |  | OSIRIS Forensic Verification | Forensic verification poster (duplicate). |
| [19346512](https://zenodo.org/records/19346512) | 2026-03-31 | Poster | `legal` |  | OSIRIS Forensic Verification | Forensic verification poster. |
| [19346592](https://zenodo.org/records/19346592) | 2026-03-31 | Poster | `legal` |  | OSIRIS Forensic Verification | OSIRIS_EVIDENCE_9HUP5.json. |
| [19355533](https://zenodo.org/records/19355533) | 2026-03-01 | Annotation collection | `legal` |  | Quantum Forensic Audit: Seniority of ADS-LLC 11D-CRSM Constants vs. D-Wave Inc.  | IP seniority audit vs D-Wave / Geometric Foundation (9 job IDs, ibm_kingston). |
| [19482796](https://zenodo.org/records/19482796) | 2026-04-09 | Report | `legal` |  | Forensic Intellectual Property Analysis: SAEONYX Entity Appropriation and Deriva | IP appropriation report (SAEONYX). Names private individuals — exclude from any scientific portfolio. |

## Lineage: τ-phase anomaly claim → self-refutation

```
17857733 corpus (490K shots)
   └─ 17858632 / 17858802 / 17859017   first evidence packages, p=1.3e-14 (ANOVA)
        └─ 17859207  v2: "K₈ = 1 at 6.87σ" (curve-fit covariance)
             └─ 17859304  v3.0: golden-ratio network (τ₀=φ⁸, F_max=1−φ⁻⁸)
                  └─ 17859312  v4.0 HONEST: K₈ = 0 (bootstrap 1.34σ), step-function, threshold not pre-registered
                       └─ 17918774  K₈ PRE-REGISTRATION (2025-12-13, SHA-256 verified) — never run as specified
                            └─ 18781261  (2026-02-26) informal τ-sweep on ibm_fez: K₈ revival REFUTED (T1 artifact),
                                          φ⁸ ZZ period REFUTED, θ_lock REFUTED, 10⁶× Zeno (18209071) REFUTED
                                 └─ 19505907 / 19656600 / 19688735 (Apr 2026) still build on θ_lock, τ₀=φ⁸, χ_PC  ← inconsistency
```

## Flywheel track mapping

**T1 — Quantum advantage on NISQ hardware:** [17857733](https://zenodo.org/records/17857733), [17918774](https://zenodo.org/records/17918774), [18038719](https://zenodo.org/records/18038719), [18209318](https://zenodo.org/records/18209318), [18781261](https://zenodo.org/records/18781261), [18782259](https://zenodo.org/records/18782259), [19864030](https://zenodo.org/records/19864030)
**T2 — Breaking quantum advantage claims:** [17857733](https://zenodo.org/records/17857733), [17858632](https://zenodo.org/records/17858632), [17858802](https://zenodo.org/records/17858802), [17859017](https://zenodo.org/records/17859017), [17859312](https://zenodo.org/records/17859312), [17859845](https://zenodo.org/records/17859845), [17918774](https://zenodo.org/records/17918774), [18038719](https://zenodo.org/records/18038719), [18781261](https://zenodo.org/records/18781261), [18783307](https://zenodo.org/records/18783307), [18784195](https://zenodo.org/records/18784195), [19505907](https://zenodo.org/records/19505907), [19656600](https://zenodo.org/records/19656600), [19864030](https://zenodo.org/records/19864030)
**T3 — AI for error correction:** [17881778](https://zenodo.org/records/17881778), [17881803](https://zenodo.org/records/17881803), [17915969](https://zenodo.org/records/17915969), [18209071](https://zenodo.org/records/18209071), [18209318](https://zenodo.org/records/18209318), [19505919](https://zenodo.org/records/19505919)

See `docs/FLYWHEEL_ASSESSMENT.md` for the proposal-fit analysis.
