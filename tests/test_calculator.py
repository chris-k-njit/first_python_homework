# Add and subtract from Professor Williams
# Added multiply and divide as additional test for this assignment.
from calculator import add, subtract, multiply, divide

def test_addition(): # Testing addition
    assert add(2,2) == 4

def test_subtraction(): # Test subtraction
    assert subtract(2,2) == 0

def test_multiplication(): 
    assert multiply(1*2) == 2

def test_division():
    assert divide(4/2) == 2