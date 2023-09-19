from lib.greet import *

def test_returns_helloname_for_name():
    result = greet("Natalie")
    assert result == "Hello, Natalie!"