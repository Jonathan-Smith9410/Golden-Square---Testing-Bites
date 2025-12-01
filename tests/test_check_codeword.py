from lib.check_codeword import *

def test_check_codeword_returns_correct_for_horse():
    assert check_codeword("horse") == "Correct! Come in."

def test_check_codeword_returns_close_for_house():
    assert check_codeword("house") == "Close, but nope."

def test_check_codeword_returns_wrong_for_swordfish():
    assert check_codeword("swordfish") == "WRONG!"

def test_check_codeword_for_right_first_letter_and_wrong_last():
    assert check_codeword("hous") == "WRONG!"

def test_check_codeword_for_wrong_first_letter_and_right_last():
    assert check_codeword("mouse") == "WRONG!"
