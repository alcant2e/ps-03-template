from src import pentagonal_numbers


def test_pentagonal_numbers():
    assert getPentagonalNumber(1) == 1
    assert getPentagonalNumber(2) == 5
    assert getPentagonalNumber(3) == 12
    assert getPentagonalNumber(36) == 1926
    assert getPentagonalNumber(46) == 3151
