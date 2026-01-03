from functions import add, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c
import pytest

# --------------------------
# Tests for add()
# --------------------------
def test_add():
    # Normal numbers
    assert add(2, 3) == 5
    # Strings concatenation
    assert add('space', 'ship') == 'spaceship'
    # Edge cases
    assert add(0, 0) == 0
    assert add(-5, 5) == 0

# --------------------------
# Tests for subtract()
# --------------------------
def test_subtract():
    # Normal numbers
    assert subtract(2, 3) == -1
    # Edge cases
    assert subtract(0, 0) == 0
    assert subtract(-5, -5) == 0
    assert subtract(1000, 500) == 500

# --------------------------
# Tests for multiply()
# --------------------------
def test_multiply():
    # Normal numbers
    assert multiply(2, 3) == 6
    # Edge cases
    assert multiply(0, 100) == 0
    assert multiply(-5, 5) == -25
    assert multiply(-4, -2) == 8

# --------------------------
# Tests for Fahrenheit → Celsius
# --------------------------
def test_convert_fahrenheit_to_celsius():
    # Normal Fahrenheit values
    assert f2c(32) == 0                 # Freezing point
    assert f2c(212) == 100              # Boiling point
    assert f2c(122) == pytest.approx(50) # Example

    # Edge case: extreme low Fahrenheit
    with pytest.raises(ValueError):
        f2c(-600)  # Below absolute zero, should raise an error

    # Edge case: absolute zero
    assert f2c(-459.67) == pytest.approx(-273.15)  # Absolute zero in Celsius
