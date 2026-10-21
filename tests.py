"""Tests for membrane-capacity. Run: python tests.py"""

from capacity import (normalize, rand_pattern, noisy, overlap,
                      HolographicMembrane, trial, accuracy,
                      mean_pair_overlap, theory_overlap, p90)
import random


def test_patterns_normalized():
    rng = random.Random(0)
    for _ in range(10):
        p = rand_pattern(32, rng)
        assert abs(sum(abs(c) ** 2 for c in p) - 1.0) < 1e-12


def test_small_load_near_perfect():
    # Light load: recognition should be essentially perfect.
    assert accuracy(64, 4, sigma=0.15, trials=50) >= 0.98


def test_deterministic():
    assert accuracy(64, 8, sigma=0.15, trials=50, seed0=3) == \
        accuracy(64, 8, sigma=0.15, trials=50, seed0=3)


def test_crosstalk_floor_matches_theory():
    for n in (32, 128):
        m = mean_pair_overlap(n, 200, seed=1)
        t = theory_overlap(n)
        assert 0.5 * t < m < 1.5 * t, (n, m, t)


def test_accuracy_degrades_with_load():
    light = accuracy(64, 4, sigma=0.30, trials=50)
    heavy = accuracy(64, 256, sigma=0.30, trials=50)
    assert heavy < light


def test_p90_picks_threshold():
    assert p90([(4, 1.0), (8, 0.95), (16, 0.85)]) == 8
    assert p90([(4, 0.5)]) is None


if __name__ == "__main__":
    for name, fn in sorted(
            [(k, v) for k, v in globals().items() if k.startswith("test_")]):
        fn()
        print(f"PASS {name}")
    print("all tests passed")
