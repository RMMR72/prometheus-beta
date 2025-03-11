import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_sieve_of_eratosthenes_basic():
    """Test basic functionality with a known set of primes."""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_sieve_of_eratosthenes_large_number():
    """Test with a larger number to ensure correct prime generation."""
    primes = sieve_of_eratosthenes(30)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sieve_of_eratosthenes_edge_case_two():
    """Test the smallest prime number."""
    assert sieve_of_eratosthenes(2) == [2]

def test_sieve_of_eratosthenes_invalid_input():
    """Test invalid input types and values."""
    with pytest.raises(TypeError):
        sieve_of_eratosthenes("10")
    
    with pytest.raises(TypeError):
        sieve_of_eratosthenes(3.14)
    
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(1)
    
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(0)
    
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(-5)

def test_sieve_of_eratosthenes_performance():
    """Ensure the function can handle a reasonably large input efficiently."""
    primes = sieve_of_eratosthenes(100)
    assert len(primes) == 25  # Known number of primes up to 100
    assert primes[-1] == 97  # Largest prime less than or equal to 100

def test_sieve_of_eratosthenes_correctness():
    """Verify the primality of generated primes."""
    primes = sieve_of_eratosthenes(20)
    
    # Manually verify each prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for prime in primes:
        assert is_prime(prime), f"{prime} should be prime"