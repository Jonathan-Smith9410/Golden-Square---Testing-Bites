from lib.gratitudes import *

def test_instantiation_with_no_input():
    gratitude_test = Gratitudes()
    assert gratitude_test.format() == "Be grateful for: "

def test_with_one_input_string():
    gratitude_test = Gratitudes()
    gratitude_test.add("I have a cup of tea")
    assert gratitude_test.format() == "Be grateful for: I have a cup of tea"

def test_with_two_input_strings():
    gratitude_test = Gratitudes()
    gratitude_test.add("I have a cup of tea")
    gratitude_test.add("a chocolate biscuit")
    assert gratitude_test.format() == "Be grateful for: I have a cup of tea, a chocolate biscuit"

def test_with_three_input_strings():
    gratitude_test = Gratitudes()
    gratitude_test.add("I have a cup of tea")
    gratitude_test.add("a chocolate biscuit")
    gratitude_test.add("and five minutes of peace.")
    assert gratitude_test.format() == "Be grateful for: I have a cup of tea, a chocolate biscuit, and five minutes of peace."

def test_with_three_identical_input_strings():
    gratitude_test = Gratitudes()
    gratitude_test.add("I have a cup of tea")
    gratitude_test.add("I have a cup of tea")
    gratitude_test.add("I have a cup of tea")
    assert gratitude_test.format() == "Be grateful for: I have a cup of tea, I have a cup of tea, I have a cup of tea"

