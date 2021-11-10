"""Testing Subtraction"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiply():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (2.0,1.0)
    multiply = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiply.get_result() == 2
