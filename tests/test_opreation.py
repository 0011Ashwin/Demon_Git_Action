from src.math_opreations import add,sub


def test_add():
    assert add(2,3) == 5
    assert add(5,5) == 10
    
    
    
def test_sub():
    assert sub(5,3) == 2
    assert sub(4,3) == 1