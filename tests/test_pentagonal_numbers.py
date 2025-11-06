from src import pentagonal_numbers


def test_pentagonal_numbers():
    assert pentagonal_numbers.getPentagonalNumber(1) == 1
    assert pentagonal_numbers.getPentagonalNumber(2) == 5
    assert pentagonal_numbers.getPentagonalNumber(3) == 12
    assert pentagonal_numbers.getPentagonalNumber(36) == 1926
    assert pentagonal_numbers.getPentagonalNumber(46) == 3151
