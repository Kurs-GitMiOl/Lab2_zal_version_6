from calculator import Calculator
import runpy

# Test addition
def test_sum():
    calc_1 = Calculator(10.0, 5.0)
    assert calc_1.sum() == 15.0


# Test subtraction
def test_subtract():
    calc_1 = Calculator(10.0, 5.0)
    assert calc_1.subtract() == 5


# Test multiplication
def test_multiply():
    calc_1 = Calculator(10.0, 5.0)
    assert calc_1.multiply() == 50.0


# Test division with correct numbers
def test_division():
    calc_1 = Calculator(10.0, 5.0)
    assert calc_1.divide() == 2.0


# Test division (for first implementation of division) with op2 == 0
def test_divide_by_zero():
    calc_1 = Calculator(10.0, 0.0)
    assert calc_1.divide() == "Error - division by zero!!!"




