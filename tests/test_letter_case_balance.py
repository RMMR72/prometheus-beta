import pytest
from src.letter_case_balance import check_letter_case_balance

def test_balanced_simple_cases():
    assert check_letter_case_balance('AbCd') == 'Balanced'
    assert check_letter_case_balance('ABab') == 'Balanced'

def test_not_balanced_cases():
    assert check_letter_case_balance('AbCde') == 'Not Balanced'
    assert check_letter_case_balance('ABCD') == 'Not Balanced'
    assert check_letter_case_balance('abcd') == 'Not Balanced'

def test_with_spaces_and_punctuation():
    assert check_letter_case_balance('A b C d!') == 'Balanced'
    assert check_letter_case_balance('Hello, World!') == 'Not Balanced'

def test_mixed_content():
    assert check_letter_case_balance('123Aa456') == 'Balanced'
    assert check_letter_case_balance('x 2!3 Y') == 'Balanced'

def test_error_cases():
    with pytest.raises(ValueError, match="Input string must contain at least one letter"):
        check_letter_case_balance('123 !@#')
    with pytest.raises(ValueError, match="Input string must contain at least one letter"):
        check_letter_case_balance('')

def test_edge_cases():
    assert check_letter_case_balance('Aa') == 'Balanced'
    assert check_letter_case_balance('aA') == 'Balanced'
    assert check_letter_case_balance('A a') == 'Balanced'