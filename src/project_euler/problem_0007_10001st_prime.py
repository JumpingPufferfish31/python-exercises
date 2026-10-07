from utils.maths.prime import nth_prime


def solution() -> None:
    """
    A solution to Project Euler problem 7
    https://projecteuler.net/problem=7

    Find the 10_001st prime number.
    """
    print(nth_prime(10_001))

def test_solution() -> None:
    assert nth_prime(1) == 2
    assert nth_prime(6) == 13
    assert nth_prime(10_001) == 104_743
