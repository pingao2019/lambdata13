# pytest

from stats import MulDiv, Calc

def test_add():
    assert MuiDiv(2,2).add_me() == 4

def test_sub():
    assert MuiDiv(2,2).sub_me() == 0

def test_mul():
    assert MuiDiv(2,2).mul_me() == 4

def test_div():
    assert MuiDiv(2,2).div_me() == 1

