# Membrane Capacity

**Live demo:** [Holographic Thoughts — Shatterpoint](https://sparkainlp-x.github.io/holographic-thoughts/) (interactive browser view; synthetic, classical simulation; measured numbers are in this repo)

Membrane Capacity is a reproducible, seeded Python study of pattern
capacity in a complex outer-product holographic-memory **model**. At
low probe noise, one-shot classification remains perfect well beyond
the memory dimension; measured crosstalk closely tracks the
theoretical √(π/4N) floor. Results are synthetic and do not yet
validate a physical holographic device.

**What this claims:** capacity behaviour of a synthetic complex
outer-product memory model under one-shot projection classification.
It does **not** claim that a physical holographic membrane has been
demonstrated or validated.

Seeded capacity sweep: random patterns, noisy probes, one-shot
projection (argmax |⟨p|probe⟩|) as the classifier. Stdlib-only
Python. AGPL-3.0.

## Measured in this repo (SYNTHETIC — seeded simulation, output of `demo.py`)

- Crosstalk floor vs theory √(π/4N): N = 64 → 0.1102 vs 0.1108
  (0.5% off); N = 128 → 0.0802 vs 0.0783 (2.4% off)
- σ = 0.15: accuracy 1.000 at P = 64, 256, 1024 for N = 64; for
  N = 128, 1.000 to P = 256 and 0.990 at P = 1024 (P90 ≥ 1024 for
  both). Classification capacity far above N for random patterns
  at low noise
- σ = 0.30: graceful breakdown (N = 64: 0.910 at P = 4 → 0.230 at
  P = 1024; N = 128: 0.925 → 0.330). P90 = 4, the smallest grid
  point tested, so the true P90 lies between 4 and 8; the grid is
  not fine enough to pin it more precisely
- 6/6 tests pass

**Uncertainty.** These are single seeded runs of `demo.py`: the accuracies and the crosstalk-floor comparison come from one random draw per grid point, with no repeats and no interval. The "0.5% off" and "2.4% off" gaps to theory are single-draw differences, not estimates of bias, and differences of that size should not be read as agreement or disagreement with the theory. Quantifying the spread needs repeated seeds, which would be a new experiment and is not done here.

All numbers are SYNTHETIC: random patterns, fixed seeds, no
physical hardware. **No physical membrane was run or validated.**

## Run it

```bash
python tests.py   # 6 tests
python demo.py    # the capacity curves (~1–4 min)
```

## Honest limits

- **No physical validation.** Everything here is a classical
  software simulation of a complex outer-product memory. Nothing
  was measured on a physical holographic device.
- **Random patterns are the best case** (near-orthogonal by
  construction). Correlated families have lower capacity; see
  [`correlated-capacity`](https://github.com/sparkainlp-x/correlated-capacity)
  for that bound.
- **At σ = 0.30, P90 is only bounded between 4 and 8** — the
  measured grid point is P90 = 4, and the next point fails the
  0.90 threshold.
- **One-shot projection only.** Iterated recall is excluded (per
  the recall-drift finding); a capacity under iteration would be
  a different quantity.
- The 0.90 threshold defining P90 is a reporting choice. Full
  account in `DESIGN.md`.

## Acknowledgements

Mun Seok Lee is acknowledged for discussion only. We cannot verify any specific contribution to this repository, and no file here is known to derive from a package received under his name. He is not an author of this release, and no endorsement of this code or its conclusions is implied.
