# Membrane Capacity

**Live demo:** [Holographic Thoughts — Shatterpoint](https://sparkainlp-x.github.io/holographic-thoughts/) (interactive browser view; synthetic, classical simulation; measured numbers are in this repo)

**How many patterns can a complex holographic memory hold before
recognition breaks?**

Seeded capacity sweep for the outer-product holographic membrane:
random patterns, noisy probes, one-shot projection as the
classifier. Stdlib-only Python. AGPL-3.0.

## Verified (SYNTHETIC — seeded simulation, output of `demo.py`)

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

All numbers are SYNTHETIC: random patterns, fixed seeds, no
physical hardware (UNRUN on any physical membrane).

## Run it

```bash
python tests.py   # 6 tests
python demo.py    # the capacity curves (~1–4 min)
```

## Honest limits

Random patterns are the easy case (best-case bound); the 0.90
threshold defining P90 is a reporting choice; one-shot projection
only (iterated recall excluded per the drift finding). Full
account in `DESIGN.md`.

## Acknowledgements

Thanks to Mun Seok Lee for discussions and contributions.
