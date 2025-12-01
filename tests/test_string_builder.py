from lib.string_builder import *

def test_size_returns_5_for_house():
    test_string = StringBuilder()
    test_string.add("house")
    assert test_string.size() == 5

def test_output_returns_house_for_house():
    test_string = StringBuilder()
    test_string.add("house")
    assert test_string.output() == "house"

def test_size_returns_10_for_house_and_plant():
    test_string = StringBuilder()
    test_string.add("house")
    test_string.add("plant")
    assert test_string.size() == 10

def test_output_returns_houseplant_for_house_and_plant():
    test_string = StringBuilder()
    test_string.add("house")
    test_string.add("plant")
    assert test_string.output() == "houseplant"

def test_size_returns_10_for_house_and_plant_with_spaces():
    test_string = StringBuilder()
    test_string.add("house")
    test_string.add(" plant ")
    assert test_string.size() == 12

def test_output_returns_house_plant__for_house_and_plant_with_spaces():
    test_string = StringBuilder()
    test_string.add("house")
    test_string.add(" plant ")
    assert test_string.output() == "house plant "

# Additional from answers video:
# 1. Initially output is empty string (testing class instantiation)
# 2. Could use more than two strings