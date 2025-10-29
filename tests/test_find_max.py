from src import find_max

def test_max_num():
    assert find_max.max_num(20, 21) == 21
    assert find_max.max_num(-1, -2) == -1