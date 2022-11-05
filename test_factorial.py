# pip3 install pytest -> Mac
# pip install pytest -> Windows

# pytest

from factorial import factorial

def test_factorial_6():
    assert 6 == factorial(3)

def test_factorial_4():
    assert 24 == factorial(4)

def test_factorial_5():
    assert 120 == factorial(5)