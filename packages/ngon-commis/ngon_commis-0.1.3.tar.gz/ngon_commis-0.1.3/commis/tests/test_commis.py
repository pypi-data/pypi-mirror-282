import pytest

from ..scripts.commis import BaseIngredient

class Test(BaseIngredient):
    def __init__(self):
        super().__init__()
        self.add_parameter('number_a', int, default=1)
        self.add_parameter('number_b', int, default=2)
        self.add_pinch('sum', bool, default=False)
        self.add_taste('result', int)
    
    def run(self):
        if self.pinches['sum'].value:
            self.tastes['result'].value = self.parameters['number_a'].value + self.parameters['number_b'].value
        else:
            self.tastes['result'].value = self.parameters['number_a'].value * self.parameters['number_b'].value

@pytest.mark.parametrize("number_a,number_b,sum,result", [(2,3,True,5),(2,3,False,6)])
def test_BaseIngredient(number_a, number_b, sum, result):
    test = Test()
    test(sum, number_a=number_a, number_b=number_b)
    assert test.tastes['result'].value == result
    test(number_a=number_a, number_b=number_b, sum=sum)
    assert test.tastes['result'].value == result