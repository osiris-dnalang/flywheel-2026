# Flywheel 2026 — proposal package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22863245.svg)](https://doi.org/10.5281/zenodo.22863245)

Submission package for the BlueQubit Quantum Flywheel open call (2026).

- `PROPOSAL.md` — the proposal (Track 2 with a Track-1 hardware component and a Track-3-adjacent seed)
- `PREREGISTRATION.md` — binding criteria for the hardware aims, committed before any job
- `FORM_ANSWERS.md` — prepared answers for the application form
- `PROPOSAL.html` — rendered copy for upload (`python build.py`)
- `experiments/osiris_advantage_marrakesh/` — Pre-registered hardware demonstration on IBM Heron r2 (`ibm_marrakesh`): bipartite-staggered DD achieves **+30.5%** coherence retention over bare idle ($P(+) = 0.8998$ vs $0.5945$) and **+6.5%** over textbook simultaneous DD ($0.8998$ vs $0.8342$) at $T = 32\ \mu\text{s}$ across an 8-qubit chain under real spectator $ZZ$ crosstalk.

Companion code, hardware datasets, and publications:
- [dnalang-core](https://github.com/osiris-dnalang/dnalang-core) · [organism_sim](https://github.com/osiris-dnalang/organism_sim) · [bridge](https://github.com/osiris-dnalang/bridge)
- Hardware Dataset (ibm_marrakesh): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23045494.svg)](https://doi.org/10.5281/zenodo.23045494)
- Previous Heron r2 Dataset: [10.5281/zenodo.22870287](https://doi.org/10.5281/zenodo.22870287)
- Code Snapshot: [10.5281/zenodo.22862567](https://doi.org/10.5281/zenodo.22862567)
