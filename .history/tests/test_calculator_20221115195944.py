from shop_app import calculator

@pytest.fixture(scope=function)
def setup():
    return Calculator()
    

def test_add():
    assert calculator.add(1.2, 1.1) == 2.3
    
    
def test_add_negative_ones():
    assert calculator.add(-1, -1) == -2    