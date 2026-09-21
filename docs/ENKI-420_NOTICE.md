# Notice for `ENKI-420/dnalang-downloads-mega-release` (to be placed at the top of that README)

> **Status (2026-09-21): superseded; do not cite.**
>
> This December-2025 collection describes itself as "IBM Quantum Validated." It is not. Its
> only "hardware" value is a hardcoded constant (`BELL_FIDELITY = 0.869`), its "quantum"
> probabilities are drawn from `np.random.dirichlet`, and it carries the constants
> (θ_lock = 51.843°, Λ_Φ, Φ = 0.7734) that the author later refuted on IBM hardware
> ([Zenodo 18781261](https://zenodo.org/records/18781261), 2026-02) and traced to sampling
> artifacts (erratum on [19656600](https://zenodo.org/records/19656600); audit in
> [22862567](https://doi.org/10.5281/zenodo.22862567)). It contains no tests.
>
> The rebuilt, tested, pre-registered successors are at
> [github.com/osiris-dnalang](https://github.com/osiris-dnalang):
> `dnalang-core` (compiler, Aer/IBM backends, ledger), `organism_sim` (rule-evolving agents),
> `bridge` (controller over the DD search space), with every result — positive and negative —
> and its criterion on disk. This repository is kept for the record only.

*Push from the ENKI-420 account; the osiris-dnalang credentials on this machine cannot
write to it. Consider also `gh repo archive ENKI-420/dnalang-downloads-mega-release`.*
