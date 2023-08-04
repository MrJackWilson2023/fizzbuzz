import pytest
from fizzbuzz import fizzbuzz
from fizzbuzz import fizzbuzz_range


def test_return_number():
    """Tests to see if fizzbuzz returns number passed to it"""

    assert fizzbuzz(1) == 1


def test_fizz():
    """fizz is returned if number is divisable by 3 evenly"""

    assert fizzbuzz(3) == "fizz"


def test_buzz():
    """buzz is returned if number is divisable by 5 evenly"""

    assert fizzbuzz(5) == "buzz"


def test_fizzbuzz():
    """tests numbers that are evenly divisiable by both 3 and 5 return
     "fizzbuzz"""

    assert fizzbuzz(15) == "fizzbuzz"


def test_fizzbuzz_range():
    """tests fizzbuzz on range of numbers"""

    test_range = fizzbuzz_range(0, 16)
    expected_result =\
        [0, 1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz",
         13, 14, "fizzbuzz"]

    assert len(test_range) == 16
    assert test_range == expected_result
    
