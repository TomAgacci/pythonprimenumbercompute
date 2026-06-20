import math
from sympy import primerange

# -----------------------------
# Substandard Prime Formula
# -----------------------------
def P_sub(n):
    return math.floor(n * (math.log(n) + math.log(math.log(n)) - 1) + 1)

# Continuous version (no floor)
def P_sub_cont(x):
    return x * (math.log(x) + math.log(math.log(x)) - 1) + 1

# Slope correction (requires true primes)
def delta(n, primes):
    return primes[n-1] - P_sub(n)

# Tama Prime Formula (exact by definition)
def T_prime(n, primes):
    return P_sub(n) + delta(n, primes)

# Tama Field with correction ansatz
def T_field(x, a0, a1):
    return P_sub_cont(x) + a0 + a1/x

# Tama slope (derivative)
def T_slope(x, a0=0, a1=0):
    return math.log(x) + math.log(math.log(x)) + 1/math.log(x) - a1/(x*x)

# -----------------------------
# Prime data
# -----------------------------
primes = list(primerange(2, 1000))  # first ~168 primes

# -----------------------------
# Formula selector
# -----------------------------
def compute(formula, n_or_x, **kwargs):
    if formula == "P_sub":
        return P_sub(n_or_x)
    if formula == "P_sub_cont":
        return P_sub_cont(n_or_x)
    if formula == "delta":
        return delta(n_or_x, primes)
    if formula == "T_prime":
        return T_prime(n_or_x, primes)
    if formula == "T_field":
        return T_field(n_or_x, kwargs.get("a0", 0), kwargs.get("a1", 0))
    if formula == "T_slope":
        return T_slope(n_or_x, kwargs.get("a0", 0), kwargs.get("a1", 0))
    if formula == "p_minus_1":
        return primes[n_or_x-1] - 1

    raise ValueError("Unknown formula name.")

# -----------------------------
# Example usage
# -----------------------------
print("P_sub(10) =", compute("P_sub", 10))
print("T_prime(10) =", compute("T_prime", 10))
print("p_n - 1 for n=10 =", compute("p_minus_1", 10))
print("T_field(10, a0=1, a1=2) =", compute("T_field", 10, a0=1, a1=2))
