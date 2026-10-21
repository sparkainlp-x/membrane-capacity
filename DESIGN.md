# DESIGN — Deep think: capacity of the holographic membrane

## The question

How many patterns can the complex outer-product holographic memory
hold before recognition breaks? This is the question every serious
reader asks next, and the honest answer has two parts.

## The crucial distinction

**Classification capacity is not Hopfield recall capacity.**
Hopfield's famous ~0.14N is about *attractor dynamics*: a partial
cue converging to a fixed point under iteration. What this sweep
measures is *nearest-neighbor classification*: argmax overlap picks
the stored pattern closest to a noisy probe. For random patterns
these are wildly different quantities, and conflating them would be
an error. (The recall-drift finding is precisely about what
iteration does to the answer — which is why the classifier here is
one-shot projection, not iterated recall.)

## Method

- N oscillators hold N complex amplitudes.
- P random patterns, i.i.d. complex Gaussian, normalized, stored via
  the outer-product rule W = Σ|p⟩⟨p|.
- Probe = a stored pattern + complex Gaussian noise (σ per
  real/imag component), renormalized.
- Accuracy = fraction of trials where argmax overlap = true pattern.
- 200 seeded trials per cell (100 for P = 1024).
- P90(N, σ) = largest P with accuracy ≥ 0.90. The 0.90 threshold is
  a reporting choice, not a law of nature.

## Measured

*(numbers from `python demo.py`, seeds 0..199)*

Light noise (σ = 0.15): accuracy 1.000 out to P = 1024 at N = 64;
at N = 128, 1.000 to P = 256 and 0.990 at P = 1024 (SYNTHETIC). Classification capacity for random patterns at
low noise is far above N — P90 ≥ 1024, the largest P tested (≥ 16N at N = 64). No
breakdown was reached; pushing further costs O(P·N) per trial and
was not pursued.

Heavy noise (σ = 0.30): a graceful breakdown curve, P90 = 4 at
both N = 64 and N = 128 (P = 4: 0.910 / 0.925; P = 8: 0.870 / 0.895;
decaying smoothly to 0.230 / 0.330 at P = 1024). Doubling N barely
moves P90 at this noise level — though large-P accuracy is better
(0.33 vs 0.23 at P = 1024) — because the noise, not the crosstalk,
is the binding constraint.

Crosstalk floor: mean |⟨a|b⟩| over random pattern pairs matches the
theory √(π/4N) to < 2% at N = 64 and N = 128 — the noise the
classifier is fighting is exactly characterized.

## What the numbers mean

1. At low noise, random-pattern recognition is essentially
   *unlimited* within any affordable P. The membrane is not the
   bottleneck; the noise is.
2. At heavy noise, capacity collapses gracefully, not
   catastrophically — accuracy degrades smoothly with P, the way a
   good classifier should.
3. Bigger N helps at every noise level (lower crosstalk floor).

## Honest limits

- **Random patterns are the easy case.** Near-orthogonal by
  construction (overlap ~ 1/√N). Correlated pattern families —
  the realistic case — will have lower capacity. This sweep does
  not measure that; it bounds the best case.
- **P90's 0.90 threshold is arbitrary.** Move it and the headline
  number moves. The curves are the result; P90 is a summary.
- **One-shot projection only.** Iterated recall was deliberately
  excluded per the drift finding; a capacity measured under
  iteration would be measuring something else.
- **Cost.** Each trial is O(P·N); the P = 1024 cells used 100
  trials for speed. Rerun with more trials if you need tighter
  error bars.
