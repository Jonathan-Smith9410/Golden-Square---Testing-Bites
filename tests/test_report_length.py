from lib.report_length import *

import pytest

def test_length_for_5_letter_string():
    assert report_length("house") == "This string was 5 characters long."

#def test_length_if_no_input():
 #   assert report_length("") == "This string was 0 characters long."

def test_length_if_string_contains_spaces():
    assert report_length("x y z") == "This string was 5 characters long."

def xtest_length_input_is_int():
    with pytest.raises(TypeError, match="has no len()") as error:
        report_length(4)
    print(error.value)
    assert str(error.value) == "object of type 'int' has no len()"

def test_length_input_is_int():
    with pytest.raises(TypeError) as error:
        report_length(4)
    print(error.value)
    assert str(error.value) == "Input is not string"

def test_if_string_is_empty():
    with pytest.raises(StringEmptyException) as error:
        report_length("")
    print(error.value)
    assert str(error.value) == "String is empty"