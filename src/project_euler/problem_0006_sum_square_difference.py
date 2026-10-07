def solution() -> None:
    """
    A solution to Project Euler problem 6
    https://projecteuler.net/problem=6

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    print(diff_sum_of_sq_and_sq_of_sum_up_to_lte(100))

def diff_sum_of_sq_and_sq_of_sum_up_to_lte(upper_bound: int) -> int:
    sum_of_sq = 0
    for n in range(upper_bound + 1):
        sum_of_sq += n**2
    sq_of_sum = int((upper_bound * (upper_bound + 1) / 2) ** 2)
    return abs(sum_of_sq - sq_of_sum)

def test_solution() -> None:
    assert diff_sum_of_sq_and_sq_of_sum_up_to_lte(0) == 0
    assert diff_sum_of_sq_and_sq_of_sum_up_to_lte(1) == 0
    assert diff_sum_of_sq_and_sq_of_sum_up_to_lte(10) == 2_640
    assert diff_sum_of_sq_and_sq_of_sum_up_to_lte(100) == 25_164_150
