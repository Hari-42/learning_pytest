from unittest.mock import patch
from simple_outputs import main

def test_output():
    result = main.output()
    assert result == "Hello World!"

def test_average():
    result = main.average()
    assert result == 5;

def test_even():
    with patch('random.randint', return_value=4):
        result = main.even_odd()
        assert result == "Even"

def test_odd():
    with patch('random.randint', return_value=7):
        result = main.even_odd()
        assert result == "Odd"