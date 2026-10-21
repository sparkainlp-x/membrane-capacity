"""Demo: capacity curves for the holographic membrane.

Two regimes, both seeded, one-shot projection as the classifier:

  sigma = 0.15 (light noise): random-pattern classification barely
      degrades -- its capacity is far above N.
  sigma = 0.30 (heavy noise): a real breakdown curve appears; P90
      (accuracy >= 0.90) becomes measurable.

200 seeded trials per cell (100 for P=1024, same seeds).

Run: python demo.py
"""

from capacity import accuracy, p90, mean_pair_overlap, theory_overlap

GRIDS = {0.15: [64, 256, 1024],          # light noise: push P high
         0.30: [4, 8, 16, 32, 64, 128, 256, 512, 1024]}  # heavy: pin P90

print("one-shot projection as classifier; crosstalk floor ~ 1/sqrt(N)\n")
for n in (64, 128):
    print(f"N = {n} oscillators "
          f"(crosstalk floor theory {theory_overlap(n):.4f}, "
          f"measured {mean_pair_overlap(n, 64):.4f})")
    for sigma, plist in GRIDS.items():
        curve = [(p, accuracy(n, p, sigma,
                              trials=100 if p >= 1024 else 200))
                 for p in plist]
        cells = "  ".join(f"P={p}: {a:.3f}" for p, a in curve)
        c = p90(curve)
        note = f"P90={c}" if c else "P90 " + (
            f">{plist[-1]}" if curve[-1][1] >= 0.90 else f"<{plist[0]}")
        print(f"  sigma={sigma}: {cells}\n           {note}")
    print()

print("RESULT: light noise -> capacity >> N; heavy noise -> measurable P90.")
print("Classification capacity is NOT Hopfield recall capacity (see DESIGN.md).")
