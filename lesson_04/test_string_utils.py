import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    (" hello", " hello"),
    ("   ", "   "),
    ])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  Skypro", "Skypro"),
    ("   Hello world", "Hello world"),
    (" Space in end  ", "Space in end  "),
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("  . ", ". "),
    ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("Skypro", "ky", True),
    ("Space in end  ", " ", True),
    ("12.04.2000", "00", True)
    ])
def test_contains_positive(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("Skypro", "kp", False),
    ("Hello world", "L", False),
    ("Space", " ", False),
    ])
def test_contains_negative(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("Skypro", "ky", "Spro"),
    ("Space in end  ", " ", "Spaceinend"),
    ("1204.2000", "0", "124.2")
    ])
def test_delete_symbol_positive(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected", [
    (" Space in end  ", " ", "Spaceinend"),
    ("12.04.2000", "8", "12.04.2000"),
    ("Hello world", "L", "Hello world"),
    ("", "", ""),
    ])
def test_delete_symbol_negative(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("input_str, input_sym, expected", [
    (" Space in end  ", None, " Space in end  "),
    (None, "o", None),
    ])
def test_delete_symbol_fail(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected
