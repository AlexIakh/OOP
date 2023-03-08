import pytest

def capital(x):
    return x.capitalize()

def test_cap():
    assert capital("hola") == "Hola"
def test_cap2():
    assert capital("hola") == "hola"