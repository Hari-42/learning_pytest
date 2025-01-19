import pytest
from LU02_controlstructures.main import positive_or_negative, simple_counter, number_comparison, countdown
def test_positive_or_negative():
    assert positive_or_negative(7) == "Positive"
    assert positive_or_negative(-3) == "Negative"
    assert positive_or_negative(0) == "Zero"


def test_simple_counter():
    assert simple_counter() == [1, 2, 3, 4, 5]


def test_number_comparison():
    assert number_comparison(10, 20) == "a is less than b"
    assert number_comparison(20, 10) == "a is greater than b"
    assert number_comparison(10, 10) == "a and b are equal"

def test_countdown():
    assert countdown() == [5, 4, 3, 2, 1, "Done!"]

