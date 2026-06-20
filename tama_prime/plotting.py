"""
plotting.py — Visualization tools for the Tama Prime System
-----------------------------------------------------------

Provides:
- Slope and field plotting
- Comparison with true primes
"""

import matplotlib.pyplot as plt
from .formulas import P_sub_cont, T_field, primes


def plot_slopes(N: int, a0: float = 0, a1: float = 0):
    """
    Plot Substandard Potential, Tama Field, and true primes.

    Parameters
    ----------
    N : int
        Maximum n-value to plot.
    a0 : float
        Correction parameter.
    a1 : float
        Correction parameter.
    """
    xs = list(range(5, N + 1))
    P_vals = [P_sub_cont(x) for x in xs]
    T_vals = [T_field(x, a0, a1) for x in xs]
    primes_vals = [primes[x - 1] for x in xs]

    plt.figure(figsize=(10, 6))
    plt.plot(xs, P_vals, label="Substandard Potential", linewidth=2)
    plt.plot(xs, T_vals, label="Tama Field", linewidth=2)
    plt.plot(xs, primes_vals, label="True Primes", linewidth=2)
    plt.legend()
    plt.xlabel("n")
    plt.ylabel("Value")
    plt.title("Tama Prime System Slopes")
    plt.grid(True)
    plt.show()
