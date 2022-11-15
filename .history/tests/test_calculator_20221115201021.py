from shop_app.calculator import Calculator
import pytest



def test_add():
    assert Calculator.add(1.2, 1.1) == 2.3
    
def test_add_negative_ones():
    assert Calculator.add(-1, -1) == -2    
    
    
    