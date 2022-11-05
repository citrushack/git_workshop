# pip3 install pytest -> Mac
# pip install pytest -> Windows

# pytest

from factorial import factorial

def test_factorial():
    assert 6 == factorial(3)

def test_factorial():
    assert 24 == factorial(4)

def test_factorial():
    assert 120 == factorial(5)