from src import prime_numbers

def test_is_prime():
    assert prime_numbers.is_prime(4) == False
    assert prime_numbers.is_prime(13) == True
    assert prime_numbers.is_prime(7019) == True
    assert prime_numbers.is_prime(2) == True
