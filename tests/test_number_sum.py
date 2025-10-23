from src import number_sum

def test_summation():
    assert number_sum.summation(101, 1001) == 496451
    assert number_sum.summation(10, 20) == 165
