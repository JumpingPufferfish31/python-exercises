from math import floor, sqrt

from utils.maths.prime import is_prime
from utils.typing import Nullable


def solution() -> None:
    """
    A solution to Project Euler problem 3
    https://projecteuler.net/problem=3

    Find the largest prime factor of the number 600_851_475_143.
    """
    print(largest_prime_factor(600_851_475_143))

def largest_prime_factor(n: int) -> Nullable[int]:
    has_largest = False
    largest = 0
    if n % 2 == 0:
        largest = 2
        has_largest = True
    head = 3
    lte_bound = floor(sqrt(n))
    while head <= lte_bound:
        if n % head == 0:
            pair = n // head
            if is_prime(pair):
                return pair
            if is_prime(head):
                largest = head
                has_largest = True
        head += 2
    if not has_largest:
        return None
    return largest

def test_solution() -> None:
    assert largest_prime_factor(1) is None
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(13_195) == 29
    assert largest_prime_factor(600_851_475_143) == 6857
