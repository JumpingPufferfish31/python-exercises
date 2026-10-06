def solution() -> None:
    """
    A solution to Project Euler problem 2
    https://projecteuler.net/problem=2

    Find the sum of even-valued terms in the Fibonacci sequence whose values do not exceed four million.
    Take the Fibbonacci sequence to begin with 1 and 2.
    """
    print(sum_of_even_fibonacci_lt(4_000_000))

def sum_of_even_fibonacci_lt(upper_bound: int) -> int:
    # The first even term e(1) = f(2) = 2, the 2nd even term e(2) = f(5) = 8.
    # By induction, e(n) = f(3n-1) for n >= 1
    # e(n) = f(3n-2) + f(3n-3)
    #      = f(3n-3) + f(3n-4) + f(3n-4) + f(3n-5)             expanding both terms again
    #      = 2f(3n-4) + f(3n-4) + f(3n-5) + f(3n-6) + f(3n-7)  group f(3n-4)'s and expanding the rest
    #      = 4f(3n-4) + f(3n-7)                                combine f(3n-5) + f(3n-6) and group f(3n-4)'s
    #      = 4f(3(n-1)-1) + f(3(n-2)-1)
    #      = 4e(n-1) + e(n-2)
    if upper_bound < 2:
        return 0
    if upper_bound < 8:
        return 2
    total = 2
    head = 8
    prev = 2
    while head < upper_bound:
        total += head
        tmp = head
        head = (4 * head) + prev
        prev = tmp
    return total

def test_solution() -> None:
    assert sum_of_even_fibonacci_lt(0) == 0
    assert sum_of_even_fibonacci_lt(8) == 2
    assert sum_of_even_fibonacci_lt(10) == 10
    assert sum_of_even_fibonacci_lt(4_000_000) == 4_613_732
