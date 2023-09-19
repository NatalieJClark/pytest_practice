import pytest
from lib.password_checker import *

"""
When checking the password, if it is at least 8 characters long
Return True
"""
def test_password_at_least_eight_chars():
    password = PasswordChecker()
    password.check("LongPassword")
    assert True


"""
When the checking the password, if it is under 8 characters long
Show "Invalid password, must be 8+ characters."
"""
def test_password_under_eight_chars():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("Short")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

