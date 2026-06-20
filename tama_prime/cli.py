#!/usr/bin/env python3
"""
Tama Prime System — CLI Interface
---------------------------------
Provides:
- Formula evaluation
- Plotting (matplotlib)
- Energy minimization for correction parameters
- Command-line interface

Author: Maximillian + Copilot
"""

import argparse
import math
import matplotlib.pyplot as plt
from sympy import primerange

# ---------------------------------------------------------
# Prime data
# ---------------------------------------------------------
primes = list(primerange(2, 20000))  # enough for n up to ~2262


# ---------------------------------------------------------
# Substandard Prime Formula
# ---------------------------------------------------------
def P_sub(n):
    return math.floor(n * (math.log(n) + math.log(math.log(n)) - 1) + 1)


# Continuous version (no floor)
def P_sub_cont(x):
    return x * (math.log(x) + math.log(math.log(x)) - 1) + 1


# ---------------------------------------------------------
# Correction term Δ(n)
# ---------------------------------------------------------
def delta(n):
    return primes[n - 1] - P_sub(n)


# ---------------------------------------------------------
# Tama Prime Formula (exact by definition)
# ---------------------------------------------------------
def T_prime(n):
    return P_sub(n) + delta(n)


# ---------------------------------------------------------
# Correction ansatz C(x) = a0 + a1/x
# ---------------------------------------------------------
def C_ansatz(x, a0, a1):
    return a0 + a1 / x


# ---------------------------------------------------------
# Tama Field T(x)
# ---------------------------------------------------------
def T_field(x, a0, a1):
    return P_sub_cont(x) + C_ansatz(x, a0, a1)


# ---------------------------------------------------------
# Tama Slope dT/dx
# ---------------------------------------------------------
def T_slope(x, a0=0, a1=0):
    return (
        math.log(x)
        + math.log(math.log(x))
        + 1 / math.log(x)
        - a1 / (x * x)
    )


# ---------------------------------------------------------
# Energy functional for minimization
# ---------------------------------------------------------
def energy(a0, a1, N):
    total = 0
    for n in range(5, N + 1):  # start at 5 to avoid ln ln issues
        Tn = T_field(n, a0, a1)
        pn = primes[n - 1]
        total += (Tn - pn) ** 2
    return total


# ---------------------------------------------------------
# Simple grid search minimizer (robust + dependency-free)
# ---------------------------------------------------------
def minimize_energy(N, a0_range=(-5, 5), a1_range=(-5, 5), steps=200):
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


# ---------------------------------------------------------
# Plotting
# ---------------------------------------------------------
def plot_slopes(N, a0=0, a1=0):
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


# ---------------------------------------------------------
# CLI Interface
# ---------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Tama Prime System CLI")
    parser.add_argument("mode", choices=["compute", "plot", "optimize"],
                        help="Mode: compute a value, plot slopes, or optimize correction parameters.")
    parser.add_argument("--formula", type=str,
                        choices=["P_sub", "P_sub_cont", "delta", "T_prime", "T_field", "T_slope"],
                        help="Formula to compute (compute mode only).")
    parser.add_argument("--n", type=float, help="Input value n or x.")
    parser.add_argument("--N", type=int, default=100, help="Range for plotting or optimization.")
    parser.add_argument("--a0", type=float, default=0, help="Correction parameter a0.")
    parser.add_argument("--a1", type=float, default=0, help="Correction parameter a1.")

    args = parser.parse_args()

    # -------------------------
    # Compute mode
    # -------------------------
    if args.mode == "compute":
        if args.formula is None or args.n is None:
            print("Error: compute mode requires --formula and --n")
            return

        if args.formula == "P_sub":
            print(P_sub(int(args.n)))
        elif args.formula == "P_sub_cont":
            print(P_sub_cont(args.n))
        elif args.formula == "delta":
            print(delta(int(args.n)))
        elif args.formula == "T_prime":
            print(T_prime(int(args.n)))
        elif args.formula == "T_field":
            print(T_field(args.n, args.a0, args.a1))
        elif args.formula == "T_slope":
            print(T_slope(args.n, args.a0, args.a1))

    # -------------------------
    # Plot mode
    # -------------------------
    elif args.mode == "plot":
        plot_slopes(args.N, args.a0, args.a1)

    # -------------------------
    # Optimization mode
    # -------------------------
    elif args.mode == "optimize":
        print(f"Optimizing a0, a1 for first {args.N} primes...")
        (a0, a1), E = minimize_energy(args.N)
        print(f"Optimal a0 = {a0}")
        print(f"Optimal a1 = {a1}")
        print(f"Energy = {E}")


if __name__ == "__main__":
    main()
