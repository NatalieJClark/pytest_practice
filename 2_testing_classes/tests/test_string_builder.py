from lib.string_builder import StringBuilder

"""
Initially the output is an empty string
"""
def test_initially_output_is_an_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

"""
When we add multiple strings
The output is those strings concatenated together
"""
def test_adding_multiple_strings_outputs_concatenated_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.output() == "hello world"

"""
When we add multiple strings
The size is the total size of the concatenated strings
"""
def test_adding_multiple_strings_has_total_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.size() == 11
