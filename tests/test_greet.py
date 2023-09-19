from lib.greet import *

def test_greets_given_name():
    result = greet("Natalie")
    assert result == "Hello, Natalie!"