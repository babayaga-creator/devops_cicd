from shop_app.calculator import Calculator
import pytest

@pytest.mark.parametrize("num, num2, sum",[(2,2,4), (5,5,10), (-1,-10,-11)])
def test_add(num, num2, sum):
    assert Calculator.add(num, num2) == sum

def test_add_negative_ones():
    assert Calculator.add(-1, -1) == -2


def test_division():
    assert Calculator.division(10, 5) == 2

def test_division_fails():
    try:
        Calculator.division(10, 0)
    except ZeroDivisionError as exc:
        assert False

def test_division_with_str():
    with pytest.raises(TypeError):
        Calculator.division(2, "w")
