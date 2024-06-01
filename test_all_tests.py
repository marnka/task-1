import pytest
from dumb_code import addition

def test_addition():
    assert addition(5, 3) == 8
    assert addition(5, -3) == 2
    assert addition(-5, -3) == -8
