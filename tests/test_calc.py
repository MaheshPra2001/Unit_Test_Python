from calculator import add, sub, mul

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_sub():
    assert sub(5,3) == 2
    assert sub(0,4) == -4
    assert sub(-1,-1) == 0

def test_mul():
    assert mul(2,4) == 8
    assert mul(4,4) == 16
    assert mul(7,4) == 28