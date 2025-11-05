from calculator import add, subtract, multiply, divide
import pytest

def test_addition():
    assert add(1, 1) == 2
    assert add(5, 3) == 8

def test_subtraction():
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 5) == 25

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_failure_example():
    assert 2 * 2 == 5  # This will fail intentionally