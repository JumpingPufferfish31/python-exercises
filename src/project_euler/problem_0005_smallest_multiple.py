from utils.maths.prime import list_primes_lte


def solution() -> None:
    """
    A solution to Project Euler problem 5
    https://projecteuler.net/problem=5

    Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
    An integer n is evenly divisible by an integer m if n is divisible by m with no remainder.
    """
    print(smallest_int_evenly_divisible_up_to_lte(20))

def smallest_int_evenly_divisible_up_to_lte(upper_bound: int) -> int:
    # Corresponds to the least common multiple.
    # Which corresponds to the product of the largest prime powers of each prime in the prime factorisation of each number lte upper bound.
    # https://en.wikipedia.org/wiki/Least_common_multiple#Using_prime_factorization
    prime_factors = list_primes_lte(upper_bound)
    largest_prime_powers = {prime: 0 for prime in prime_factors}
    for n in range(2, upper_bound + 1):
        remaining = n
        for factor in prime_factors:
            power = 0
            while remaining % factor == 0:
                power += 1
                remaining //= factor
            if power > largest_prime_powers[factor]:
                largest_prime_powers[factor] = power
    lcm = 1
    for prime, power in largest_prime_powers.items():
        lcm *= prime**power
    return lcm

def test_solution() -> None:
    assert smallest_int_evenly_divisible_up_to_lte(10) == 2_520
    assert smallest_int_evenly_divisible_up_to_lte(20) == 232_792_560
