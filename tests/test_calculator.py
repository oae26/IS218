"""
Provides some arithmetic Functions
"""
from calculator import add
from calculator import subtract
from calculator import divide
def test_addition():
    """Tests addition"""
    assert add(2,2)
def test_subtraction():
    """Tests the subtraction of two numbers"""
    assert subtract(2,2) == 0
def test_division():
    """Tests the division of two numbers"""
    assert divide(2,2)
