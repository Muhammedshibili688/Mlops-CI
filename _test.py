import pytest

# To test squares, cubes, and fifth powers of numbers
def square(n):
    return n ** 2
def cube(n):
    return n ** 3
def fifth_power(n): 
    return n ** 5

# Testing
def test_sqaure():
    assert square(2) == 4, "Test failed square of 2 should be 4"
    assert square(3) == 9, "Test failed square of 3 should be 9"
    assert square(4) == 16, "Test failed square of 4 should be 16" 

def test_cube():
    assert cube(2) == 8, "Test failed cube of 2 should be 8"
    assert cube(3) == 27, "Test failed cube of 3 should be 27"
    assert cube(4) == 64, "Test failed cube of 4 should be 64" 

def test_fifth_power():
    assert fifth_power(2) == 32, "Test failed fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test failed fifth power of 3 should be 243"
    assert fifth_power(4) == 1024, "Test failed fifth power of 4 should be 1024"

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
    with pytest.raises(TypeError):
        cube(None)
    with pytest.raises(TypeError):
        fifth_power([])