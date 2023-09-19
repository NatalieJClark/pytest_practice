from lib.gratitudes import Gratitudes

"""
Initially the gratitudes list is empty
"""
def test_intially_empty_gratitudes_list():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

"""
When you add a single gratitide
It is reflected in the formatted list
"""
def test_adding_single_gratitude_adds_it_to_list():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    assert gratitudes.format() == "Be grateful for: family"

"""
When you add multiple gratitides
They are reflected in the formatted list
"""
def test_adding_multiple_gratitudes_adds_them_to_list():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("health")
    assert gratitudes.format() == "Be grateful for: family, health"
