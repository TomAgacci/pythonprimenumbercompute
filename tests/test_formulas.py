from tama_prime.formulas import P_sub, T_prime

def test_substandard_prime():
    assert P_sub(10) > 0

def test_tama_prime():
    assert T_prime(5) > 0
