import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2.0, 3.0) == 5.0
    assert add(-2.0, 3.0) == 1.0
    assert add(-2.0, -3.0) == -5.0


def test_subtract():
    assert subtract(5.0, 2.0) == 3.0
    assert subtract(-5.0, 2.0) == -7.0
    assert subtract(-5.0, -2.0) == -3.0


def test_multiply():
    assert multiply(2.0, 3.0) == 6.0
    assert multiply(-2.0, 3.0) == -6.0
    assert multiply(2.0, -3.0) == -6.0


def test_divide():
    assert divide(10.0, 2.0) == 5.0
    assert divide(-10.0, 2.0) == -5.0
    assert divide(0.0, 1.0) == "Error: Division by zero is not allowed"
    assert divide(10.0, 0.0) == "Error: Division by zero is not allowed"
