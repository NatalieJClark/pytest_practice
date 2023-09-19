import pytest
from lib.reminder import *


"""
When the user sets a task
The user is reminded of that task
"""
def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Natalie")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Natalie!"

"""
When the user doesn't set a task
The user is given the error message "No reminder set!"
"""
def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"
