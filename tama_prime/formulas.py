import math
from sympy import primerange

primes = list(primerange(2, 20000))

def P_sub(n):
    return math.floor(n * (math.log(n) + math.log(math.log(n)) - 1) + 1)

def P_sub_cont(x):
    return x * (math.log(x) + math.log(math.log(x)) - 1) + 1

def delta(n):
    return primes[n-1] - P_sub(n)

def T_prime(n):
    return P_sub(n) + delta(n)

def C_ansatz(x, a0, a1):
    return a0 + a1/x

def T_field(x, a0, a1):
    return P_sub_cont(x) + C_ansatz(x, a0, a1)

def T_slope(x, a0=0, a1=0):
    return math.log(x) + math.log(math.log(x)) + 1/math.log(x) - a1/(x*x)
