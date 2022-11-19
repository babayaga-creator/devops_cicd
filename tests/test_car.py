from shop_app.car import Car
import pytest



@pytest.fixture()
def my_car():
    return Car("white", 4, 150)


def test_color(my_car):
    my_car.set_color("red")
    assert my_car.color == "red"

def test_doors(my_car):
    my_car.set_doors(2)
    assert my_car.doors == 2

def test_power(my_car):
    my_car.set_power(1000)
    assert my_car.power == 1000
