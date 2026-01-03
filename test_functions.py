from functions import add, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

# Step 5: uncommented test_subtract
def test_subtract():
    assert subtract(2, 3) == -1

# Step 11: uncommented test_convert_fahrenheit_to_celsius
def test_convert_fahrenheit_to_celsius():
    # Test normal Fahrenheit values
    assert f2c(32) == 0
    assert f2c(122) == pytest.approx(50)

    # Test extremely low Fahrenheit value raises an error
    with pytest.raises(AssertionError):
        f2c(-600)

