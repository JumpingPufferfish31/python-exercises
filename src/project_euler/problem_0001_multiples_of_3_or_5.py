def solution() -> None:
    """
    A solution to Project Euler problem 1
    https://projecteuler.net/problem=1

    Find the sum of all the multiples of 3 or 5 below 1_000.
    """
    print(sum_of_multiples_lt([3, 5], 1000))

def sum_of_multiples_lt(multiples: list[int], upper_bound: int) -> int:
    total = 0
    for i in range(upper_bound):
        if any(i % m == 0 for m in multiples):
            total += i
    return total

def test_solution() -> None:
    assert sum_of_multiples_lt([3, 5], 10) == 23
    assert sum_of_multiples_lt([3, 5], 1000) == 233168
