from lib.greet import *

def test_returns_Hello_Jon_from_Jon():
    result = greet("Jon")
    assert result == "Hello, Jon!"
    