
import pytest
import factorial

def test_factorial_zeros():
    assert factorial.factorial(0)==0

def test_factorial_five():
    assert factorial.factorial(5)==120

def test_factorial_200():
    assert factorial.factorial(20)== 2432902008176640000

def test_reverse_factorial_120():
    assert factorial.reverse_factorial(120) == 5

def test_reverse_factorial_none():
    assert factorial.reverse_factorial(23) == "None"


def test_reverse_factorial_24():
    assert factorial.reverse_factorial(24) == 4


