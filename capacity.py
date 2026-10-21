"""Capacity sweep for the complex outer-product holographic memory.

Question: how many random patterns can the membrane store before
one-shot projective recognition breaks down?

Method (all seeded, stdlib only):
  - N oscillators hold N complex amplitudes.
  - P random patterns (i.i.d. complex Gaussian, normalized) stored via
    the outer-product rule.
  - Probe = a stored pattern + complex Gaussian noise (sigma), then
    one-shot project() -- the recommended classifier, per the
    recall-drift finding (iterate and the answer dissolves).
  - Accuracy = fraction of trials where argmax overlap = true pattern.

Capacity P90(N) = largest P with accuracy >= 0.90.
"""

import math
import random


def normalize(v):
    n = math.sqrt(sum(abs(c) ** 2 for c in v))
    return [c / n for c in v]


def rand_pattern(n, rng):
    return normalize([complex(rng.gauss(0, 1), rng.gauss(0, 1))
                      for _ in range(n)])


def noisy(state, sigma, rng):
    return normalize([c + complex(rng.gauss(0, sigma), rng.gauss(0, sigma))
                      for c in state])


def overlap(field, pattern):
    return sum(p.conjugate() * f for p, f in zip(pattern, field))


class HolographicMembrane:
    def __init__(self, patterns):
        self.patterns = [normalize(p) for p in patterns]

    def project(self, field):
        ms = [overlap(field, p) for p in self.patterns]
        tot = sum(abs(m) ** 2 for m in ms)
        probs = [abs(m) ** 2 / tot for m in ms]
        return max(range(len(ms)), key=lambda i: abs(ms[i])), probs


def trial(n, p, sigma, seed):
    """One recognition trial. Returns True iff the correct pattern wins."""
    rng = random.Random(seed)
    patterns = [rand_pattern(n, rng) for _ in range(p)]
    mem = HolographicMembrane(patterns)
    target = rng.randrange(p)
    probe = noisy(patterns[target], sigma, rng)
    winner, _ = mem.project(probe)
    return winner == target


def accuracy(n, p, sigma=0.15, trials=200, seed0=0):
    ok = sum(trial(n, p, sigma, seed0 + i) for i in range(trials))
    return ok / trials


def mean_pair_overlap(n, p, seed=0):
    """Mean |<a|b>| over distinct random pattern pairs (crosstalk floor)."""
    rng = random.Random(seed)
    pats = [rand_pattern(n, rng) for _ in range(p)]
    tot, cnt = 0.0, 0
    for i in range(p):
        for j in range(i + 1, p):
            tot += abs(overlap(pats[i], pats[j]))
            cnt += 1
    return tot / cnt


def theory_overlap(n):
    """E|<a|b>| for random complex unit vectors ~ sqrt(pi / 4N)."""
    return math.sqrt(math.pi / (4 * n))


def capacity_curve(n, p_list, sigma=0.15, trials=200):
    return [(p, accuracy(n, p, sigma, trials)) for p in p_list]


def p90(curve):
    """Largest P on the curve with accuracy >= 0.90 (None if none)."""
    ok = [p for p, a in curve if a >= 0.90]
    return max(ok) if ok else None
