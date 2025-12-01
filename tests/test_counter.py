from lib.counter import *

def test_passing_positive_int_returns_expected_value():
    count_test = Counter()
    count_test.add(6)
    assert count_test.report() == "Counted to 6 so far."

def test_passing_zero_returns_expected_value():
    count_test = Counter()
    count_test.add(0)
    assert count_test.report() == "Counted to 0 so far."

def test_passing_negative_int_returns_expected_value():
    count_test = Counter()
    count_test.add(-5)
    assert count_test.report() == "Counted to -5 so far."

def test_passing_positive_float_returns_expected_value():
    count_test = Counter()
    count_test.add(2.3)
    assert count_test.report() == "Counted to 2.3 so far."

def test_passing_negative_float_returns_expected_value():
    count_test = Counter()
    count_test.add(-2.3)
    assert count_test.report() == "Counted to -2.3 so far."

# Additional from answers video:
# 1. Check initial state, ie instantiates with a count of 0
# 2. Add multiple numbers to counter sequentially then testing for total
# 3. Add both positive and negative numbers