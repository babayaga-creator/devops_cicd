"""Module providingFunction printing python version."""
class Calculator():
    '''Takes in a number n, returns the square of n'''
    @classmethod
    def add(cls, n_1=float, n_2=float ) -> float:
        '''Takes in a number n, returns the square of n'''
        return n_1 + n_2

    @classmethod
    def division(cls,x_1:int, y_1:int):
        '''Takes in a number n, returns the square of n'''
        try:
            return x_1/y_1
        except ZeroDivisionError:
            print("Can't division with zero")
            return None
