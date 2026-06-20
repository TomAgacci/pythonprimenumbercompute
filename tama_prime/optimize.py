"""
optimize.py — Energy minimization for the Tama Prime System
-----------------------------------------------------------

Provides:
- Energy functional
- Grid-search minimizer
"""

from .formulas import T_field, primes


def energy(a0: float, a1: float, N: int) -> float:
    """
    Energy functional measuring deviation from true primes.

    Parameters
    ----------
    a0 : float
        Correction parameter.
    a1 : float
        Correction parameter.
    N : int
        Number of primes to include.

    Returns
    -------
    float
        Sum of squared errors.
    """
    total = 0
    for n in range(5, N + 1):
        Tn = T_field(n, a0, a1)
        pn = primes[n - 1]
        total += (Tn - pn) ** 2
    return total


def minimize_energy(N: int, a0_range=(-5, 5), a1_range=(-5, 5), steps=200):
    """
    Simple grid-search minimizer for (a0, a1).

    Parameters
    ----------
    N : int
        Number of primes to fit.
    a0_range : tuple
        Range for a0.
    a1_range : tuple
        Range for a1.
    steps : int
        Resolution of the grid.

    Returns
    -------
    ((float, float), float)
        Best (a0, a1) and the corresponding energy.
    """
    best = (None, float("inf"))
    a0_min, a0_max = a0_range
    a1_min, a1_max = a1_range

    for i in range(steps):
        a0 = a0_min + (a0_max - a0_min) * i / steps
        for j in range(steps):
            a1 = a1_min + (a1_max - a1_min) * j / steps
            E = energy(a0, a1, N)
            if E < best[1]:
                best = ((a0, a1), E)

    return best
