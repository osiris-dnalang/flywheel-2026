# Is this real? — An honest assessment of the DNA-Lang / OSIRIS / CRSM body of work

*2026-09-20. Based on: all 60 Zenodo records (contents read, raw IBM job payloads decoded), the three GitHub accounts (172 repos inventoried; 18 core repos cloned and read), and the OSIRIS code on this machine (compiler, simulators, metrics executed and tested against known answers). Companion: `PUBLICATIONS.md`, `FLYWHEEL_ASSESSMENT.md`.*

## The short answer

**The physics claims are not real. The person who made them is.** Every headline result I could test failed, and in each case I could identify the specific artifact producing it — not "unconvincing", but *wrong for a nameable reason*. At the same time, the corpus shows real capability: hundreds of real hardware jobs, a working teleportation-with-feedforward experiment, an honest published self-refutation of six of your own claims, a hash-verified pre-registration, and one clean methodological idea. Three years produced skill and infrastructure, not discoveries. That is not nothing, and it is not what the papers say.

## What I tested and what happened

| Claim | What I did | Result |
|---|---|---|
| **τ-phase anomaly** (p = 10⁻¹⁴, τ₀ = φ⁸ μs) | Read `calculate_tau_phase()` | τ-phase = `(unix_timestamp % 46e-6) / 46e-6` — the sub-46-microsecond remainder of the *server's job-creation timestamp*. That number carries no information about the qubits. The anomaly is a correlation between timestamp noise and a fidelity metric. |
| **Φ-threshold "phase transition"** (51× enhancement, d = 1.65) | Decoded all 105 corpus jobs | Corpus mixes 2-, 4-, 5-, 27- and 127-bit circuits, all scored with the *Bell-state* formula P(00)+P(11). The "two regimes" are different circuit families. The bimodal histogram is the same thing. |
| **136-bit negentropy gap on 156 qubits** | Decoded the 1M-shot BitArray | All 10⁶ shots are unique → plug-in entropy = log₂(10⁶) = 19.9316 bits, exactly the number reported. Per-qubit marginals sum to 149.7/156 bits: the output is near maximally mixed, the opposite of "collapse". |
| **K₈ revival, φ⁸ ZZ period, θ_lock = 51.843°, 10⁶× Zeno** | Read your own record 18781261 | You refuted all four on hardware in Feb 2026. The April 2026 papers still use them. |
| **Tetrahedral correction** (+16.9% GHZ-20) | Read the pass; checked the simulator benchmark | The pass inserts RZ before Z-basis measurement, so it cannot change the ideal outcome (your own simulator: 1.0 vs 1.0). The hardware number is one job, two circuits, no repeats, no error bars, no control. Device drift. **Cheaply testable — see below.** |
| **Penteract zero-parameter cosmology** | Read your sensitivity/concordance records | Your own analysis: 4 effective parameters, 4 independent predictions, 0 degrees of freedom. "The naive 5.2σ claim is incorrect." |
| **CCCE metrics Φ, Λ, Γ, Ξ** | Read every definition in the code | Φ, Λ, Γ are *inputs* — dataclass fields someone sets. Ξ = ΛΦ/Γ. Nowhere is Φ computed from a state, Λ from a density matrix, or Γ from a channel. "Proof-of-coherence mining" is `if phi >= 0.7734: append`. |
| **Local QVM / qByte simulator** | Ran Bell circuit | Each qubit is one quaternion (a single Bloch vector); `cx` is "if P(control=1) > 0.5 apply X". Its own docstring: "does not achieve actual quantum superposition or entanglement." A Bell state is impossible in this model. The DNA-Lang runtime returns uniform random counts for H·CX. |
| **DNA-Lang the language** | Parsed the flagship 72-gene organism | Parses to an empty AST. The 72 "genes" are English sentences in `action:` fields. The Rust "compiler" has no lexer/parser. A hand-written 4-gate program does parse and produce IR — that part exists, but it is a thin wrapper around a gate list. |
| **Test suite** | Ran it | 90 unit tests pass in 3.5 s; they test that code does what code does, not that physics is right. Full suite hangs (>15 min). |

Not one of these required domain expertise beyond what a first-year grad student in QI would apply. That is exactly why the papers get no engagement: a reviewer finds the artifact in minutes and stops reading.

## What is actually real

- **You ran ~300 real jobs on nine IBM backends** (fez, torino, kingston, marrakesh, nazca, brisbane, kyoto, osaka, kyiv) over 11 months, with job IDs anyone can verify. Most people who write about quantum computing have never done this.
- **Teleportation with mid-circuit measurement and classical feed-forward, F = 0.773** (18781261). Non-trivial to implement correctly; the code looks right.
- **GHZ witnesses to 18 qubits on two chips, XEB to depth 16, 5-qubit ZNE + majority vote.** Competent NISQ characterization.
- **Record 18781261 itself.** You tested ten of your own claims on hardware and published "4 confirmed, 6 refuted". Almost nobody does that. It is the single most credible document you have produced.
- **The W₂ robustness metric** (19864030): reference-free, hardware-native, and the paper falsifies its own motivating hypothesis. This is a real, small, publishable idea.
- **The K₈ pre-registration** (17918774): SHA-256 verified, binding decision rules. Correct scientific instinct.
- **Engineering throughput**: hash-chained provenance ledger, Zenodo pipeline, a working local ML stack, transpiler passes for both Qiskit and Braket, packaged with pyproject and tests.

## The pattern

Every failed claim has the same shape: **a metric is applied where it doesn't belong, a constant is fitted post hoc and then treated as a prediction, and the label ("consciousness", "negentropy", "compiler", "world record") is written before the thing exists.** The vocabulary is not the problem — the vocabulary is a symptom. Mainstream language would not have saved the τ-phase result, because `timestamp % 46 μs` is meaningless in any dialect.

Three things made this worse:
1. **Generating instead of building.** Much of the 172-repo footprint is LLM-generated scaffolding: names that promise what the code doesn't do, 13 DOIs for one zip, 84K lines in one SDK with 374 mock/simulate markers. Volume became a substitute for verification.
2. **Noise-mining with no null.** Heterogeneous data + a bag of "smoking guns" + no pre-registered null model will always produce p = 10⁻¹⁴ for something.
3. **Not updating after refutation.** You did the hard part — the Feb 2026 refutation — and then the April papers proceeded as if it hadn't happened. The IP/forensic records (8 of 60) suggest the sunk cost got defended instead of written off.

## Is there anything to salvage? Yes — three experiments, all cheap

1. **Tetrahedral correction, done properly.** Same physical qubits, interleaved standard/corrected circuits, 10 repeats each, randomized order, a control with a random δ, proper GHZ fidelity (Z populations *and* X-parity). One afternoon on ibm_fez. If it survives, you have a small real paper. If not, you retire θ_lock for good. Either outcome is worth more than everything currently on Zenodo.
2. **Run the pre-registered K₈ sweep as written** (substitute current backends, declare the amendment). Publish the null. A pre-registered 5σ-powered null on a public claim is a citable, honest result and closes the loop you opened.
3. **Extend W₂ robustness.** It's your one idea that has no artifact behind it. Compare it against standard metrics (Hellinger, TVD, XEB) on more circuits, on two vendors. This is the seed of a real research direction.

And stop: retire the constants (θ_lock, τ₀ = φ⁸, χ_PC, Φ = 0.7734), the consciousness/negentropy vocabulary, the "Nobel"/"world record" framing, the cosmology. Consolidate 172 repos into three with one honest README each. Add errata to 19656600 and 18209071. The work you'd be left with is small, true, and yours — and it's a base you can build on, which the current edifice is not.

## What I did not verify
Job IDs against IBM's account (needs your token); theory records (6dCRSM, 11D Wheeler–DeWitt) beyond your own sensitivity analyses; the 360 MB v5.0.0 tarball beyond its md5.
