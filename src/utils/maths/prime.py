def is_prime(n: int) -> bool:
    # All primes > 3 can be written as 6k+-1 for some positive k
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True

    factor = 5
    while factor * factor <= n:
        if n % factor == 0 or n % (factor + 2) == 0:
            return False
        factor += 6
    return True

def list_primes_lte(upper_bound: int) -> list[int]:
    # Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # With improvements:
    #  - Starting from p**2
    #  - Ending when p**2 > n
    #  - Going by odd p
    # If we still need to optimise further, see "wheel factorization"
    # or Euler's sieve.
    num_odds = (upper_bound // 2) - ((upper_bound + 1) % 2)
    primes_sieve = [True] * num_odds

    odd = 3
    while odd**2 <= upper_bound:
        odd_index = (odd // 2) - 1
        if primes_sieve[odd_index]:
            head = odd**2
            while head <= upper_bound:
                if head % 2 == 1:
                    head_index = (head // 2) - 1
                    primes_sieve[head_index] = False
                head += odd
        odd += 2

    primes = []
    if upper_bound >= 2:
        primes.append(2)
    primes.extend([(2 * i) + 3 for i, prime_index in enumerate(primes_sieve) if prime_index])
    return primes

def nth_prime(n: int) -> int:
    # Find results on upper bounds for nth prime if we need to optimise further.
    upper_bound = 2
    candidates = [2]
    while len(candidates) < n:
        upper_bound *= 2
        candidates = list_primes_lte(upper_bound)
    return candidates[n - 1]
