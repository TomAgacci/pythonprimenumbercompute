"""
formulas.py — Core mathematical engine for the Tama Prime System
----------------------------------------------------------------

Contains:
- Substandard Prime Formula
- Continuous Substandard Potential
- Tama Prime Formula
- Correction ansatz
- Tama Field
- Tama Slope
- Prime data

All functions include docstrings for documentation and IDE support.
"""

import math
from sympy import primerange

# ---------------------------------------------------------
# Prime data
# ---------------------------------------------------------
primes = list(primerange(2, 20000))  # enough for n up to ~2262


# ---------------------------------------------------------
# Substandard Prime Formula
# ---------------------------------------------------------
def P_sub(n: int) -> int:
    """
    Substandard Prime Formula (discrete version).

    Parameters
    ----------
    n : int
        Index of the prime (n >= 2).

    Returns
    -------
    int
        Approximation to the nth prime using:
        floor( n( ln(n) + ln(ln(n)) – 1 ) + 1 )
    """
    return math.floor(n * (math.log(n) + math.log(math.log(n)) - 1) + 1)


def P_sub_cont(x: float) -> float:
    """
    Continuous Substandard Potential (no floor).

    Parameters
    ----------
    x : float
        Continuous input value.

    Returns
    -------
    float
        Smooth approximation to the prime curve.
    """
    return x * (math.log(x) + math.log(math.log(x)) - 1) + 1


# ---------------------------------------------------------
# Correction term Δ(n)
# ---------------------------------------------------------
def delta(n: int) -> int:
    """
    Slope correction term Δ(n) = p_n – P_sub(n).

    Parameters
    ----------
    n : int
        Prime index.

    Returns
    -------
    int
        Difference between true prime and analytic approximation.
    """
    return primes[n - 1] - P_sub(n)


# ---------------------------------------------------------
# Tama Prime Formula
# ---------------------------------------------------------
def T_prime(n: int) -> int:
    """
    Tama Prime Formula (exact by definition).

    Parameters
    ----------
    n : int
        Prime index.

    Returns
    -------
    int
        True prime p_n reconstructed as:
        P_sub(n) + Δ(n)
    """
    return P_sub(n) + delta(n)


# ---------------------------------------------------------
# Correction ansatz C(x)
# ---------------------------------------------------------
def C_ansatz(x: float, a0: float, a1: float) -> float:
    """
    Correction ansatz C(x) = a0 + a1/x.

    Parameters
    ----------
    x : float
        Input value.
    a0 : float
        Constant correction term.
    a1 : float
        1/x correction term.

    Returns
    -------
    float
        Correction field value.
    """
    return a0 + a1 / x


# ---------------------------------------------------------
# Tama Field T(x)
# ---------------------------------------------------------
def T_field(x: float, a0: float, a1: float) -> float:
    """
    Continuous Tama Prime Field.

    Parameters
    ----------
    x : float
        Input value.
    a0 : float
        Correction parameter.
    a1 : float
        Correction parameter.

    Returns
    -------
    float
        Field value T(x) = P_sub_cont(x) + C(x)
    """
    return P_sub_cont(x) + C_ansatz(x, a0, a1)


# ---------------------------------------------------------
# Tama Slope dT/dx
# ---------------------------------------------------------
def T_slope(x: float, a0: float = 0, a1: float = 0) -> float:
    """
    Derivative of the Tama Prime Field.

    Parameters
    ----------
    x : float
        Input value.
    a0 : float
        Correction parameter.
    a1 : float
        Correction parameter.

    Returns
    -------
    float
        dT/dx = ln(x) + ln(ln(x)) + 1/ln(x) - a1/x^2
    """
    return (
        math.log(x)
        + math.log(math.log(x))
        + 1 / math.log(x)
        - a1 / (x * x)
    )
