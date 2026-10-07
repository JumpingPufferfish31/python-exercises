from utils.string import is_palindrome
from utils.typing import Nullable

def solution() -> None:
    """
    A solution to Project Euler problem 4
    https://projecteuler.net/problem=4

    Find the largest palindrome made from the product of two 3-digit numbers.
    A palindromic number reads the same both ways.
    """
    print(largest_palindrome_product(terms_digit_lte=3))

def largest_palindrome_product(terms_digit_lte: int) -> Nullable[int]:
    if terms_digit_lte < 1:
        return None
    product = 1
    upper_bound = (10**terms_digit_lte) - 1
    lower_bound = 10 ** (terms_digit_lte - 1)
    for term_1 in range(upper_bound, lower_bound - 1, -1):
        for term_2 in range(term_1, lower_bound - 1, -1):
            candidate = term_1 * term_2
            if is_palindrome(str(candidate)) and candidate > product:
                product = candidate
    return product

def test_solution() -> None:
    assert largest_palindrome_product(terms_digit_lte=0) is None
    assert largest_palindrome_product(terms_digit_lte=1) == 9
    assert largest_palindrome_product(terms_digit_lte=2) == 90_09
    assert largest_palindrome_product(terms_digit_lte=3) == 906_609
