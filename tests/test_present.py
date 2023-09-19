import pytest
from lib.present import *

"""
When the user wraps an item
We get the item back when unwrapping
"""
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

"""
When the user tries to wrap an already wrapped present
Show error mesage "A contents has already been wrapped."
"""
def test_wrap_already_wrapped_present_throws_error():
    present = Present()
    present.wrap(45)
    with pytest.raises(Exception) as e:
        present.wrap(78)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

"""
When the user tries to unwrap a present when nothing has been wrapped
Show error message "No contents have been wrapped."
"""
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

"""
When the user tries to wrap an already wrapped present
The first-wrapped value is unchanged
"""
def test_wrap_already_wrapped_present_preserves_contents():
    present = Present()
    present.wrap(45)
    with pytest.raises(Exception) as e:
        present.wrap(78)
    assert present.unwrap() == 45

