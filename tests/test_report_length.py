from lib.report_length import report_length

"""
If string given
Returns length of string including spaces
"""
def test_report_length_of_given_string():
    result = report_length("Hello world!")
    assert result == "This string was 12 characters long."


"""
If empty string given
Returns 0 length
"""
def test_report_length_of_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."