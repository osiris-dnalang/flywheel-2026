# Flywheel 2026 — proposal package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22863245.svg)](https://doi.org/10.5281/zenodo.22863245)

Submission package for the BlueQubit Quantum Flywheel open call (2026).

- `PROPOSAL.md` — the proposal (Track 2 with a Track-1 hardware component and a Track-3-adjacent seed)
- `PREREGISTRATION.md` — binding criteria for the hardware aims, committed before any job
- `FORM_ANSWERS.md` — prepared answers for the application form
- `PROPOSAL.html` — rendered copy for upload (`python build.py`)
- `experiments/osiris_advantage_marrakesh/` — Pre-registered dynamical-decoupling (DD) hardware run on IBM Heron r2 (`ibm_marrakesh`), one job, one 8-qubit chain: bipartite-staggered DD retains $P(+) = 0.8998$ at $T = 32\ \mu\text{s}$ against $0.8342$ for textbook simultaneous DD (+6.5 percentage points) under real spectator $ZZ$ crosstalk. Textbook DD itself recovers most of the gap to bare idle ($0.5945$), so the comparison that matters is the +6.5. This is a coherence-retention result, not a quantum-advantage claim; the directory and file names keep the original wording because renaming would break the hash-anchored record.

Companion code, hardware datasets, and publications:
- [dnalang-core](https://github.com/osiris-dnalang/dnalang-core) · [organism_sim](https://github.com/osiris-dnalang/organism_sim) · [bridge](https://github.com/osiris-dnalang/bridge)
- Hardware Dataset (ibm_marrakesh): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23045494.svg)](https://doi.org/10.5281/zenodo.23045494)
- Previous Heron r2 Dataset: [10.5281/zenodo.22870287](https://doi.org/10.5281/zenodo.22870287)
- Code Snapshot: [10.5281/zenodo.22862567](https://doi.org/10.5281/zenodo.22862567)
