import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test a basic weighted sum calculation."""
    numbers = [1, 2, 3]
    weights = [0.5, 1, 1.5]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(7.0)

def test_single_element_lists():
    """Test weighted sum with single element lists."""
    numbers = [10]
    weights = [2]
    assert compute_weighted_sum(numbers, weights) == 20

def test_zero_weights():
    """Test weighted sum with some zero weights."""
    numbers = [1, 2, 3]
    weights = [0, 1, 0]
    assert compute_weighted_sum(numbers, weights) == 2

def test_negative_numbers_and_weights():
    """Test weighted sum with negative numbers and weights."""
    numbers = [-1, 2, -3]
    weights = [1, -2, 3]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(-13)

def test_float_inputs():
    """Test weighted sum with float inputs."""
    numbers = [1.5, 2.5, 3.5]
    weights = [0.5, 1.5, 2.5]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(13.25)

def test_empty_lists_raise_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="Both numbers and weights lists must be non-empty"):
        compute_weighted_sum([], [])

def test_mismatched_list_lengths_raise_error():
    """Test that lists with different lengths raise a ValueError."""
    with pytest.raises(ValueError, match="Numbers and weights lists must have the same length"):
        compute_weighted_sum([1, 2], [1, 2, 3])

def test_non_numeric_inputs_raise_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="All numbers and weights must be numeric"):
        compute_weighted_sum([1, 'a'], [1, 2])
    
    with pytest.raises(TypeError, match="All numbers and weights must be numeric"):
        compute_weighted_sum([1, 2], [1, None])