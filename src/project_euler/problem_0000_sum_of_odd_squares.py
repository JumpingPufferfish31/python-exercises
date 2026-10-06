def solution() -> None:
    """
    A solution to Project Euler problem 0
    https://projecteuler.net/register

    Find the sum of odd squares among the first n square numbers.
    A square number is a square of a positive integer.
    """
    print(sum_of_odds_among_first_n_squares(574_000))

def sum_of_odds_among_first_n_squares(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        square = i * i
        if square % 2 == 1:
            total += square
    return total

def test_solution() -> None:
    assert sum_of_odds_among_first_n_squares(0) == 0
    assert sum_of_odds_among_first_n_squares(1) == 1
    assert sum_of_odds_among_first_n_squares(5) == 35
    assert sum_of_odds_among_first_n_squares(574_000) == 31_519_870_666_571_000
