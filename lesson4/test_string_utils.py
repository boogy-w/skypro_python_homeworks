import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("SkyPro") == "Skypro"
    assert string_utils.capitilize("") == ""
    assert string_utils.capitilize("123") == "123"


def test_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   123") == "123"
    assert string_utils.trim("") == ""
    assert string_utils.trim("   ") == ""


def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("", ",") == []
    assert string_utils.to_list(" , ", ",") == [" ", " "]


def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S")
    assert not string_utils.contains("SkyPro", "U")
    assert not string_utils.contains("", "S")
    assert string_utils.contains("1234", "3")


def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "U") == "SkyPro"
    assert string_utils.delete_symbol("1234", "3") == "124"
    assert string_utils.delete_symbol("", "S") == ""


def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S")
    assert not string_utils.starts_with("SkyPro", "P")
    assert not string_utils.starts_with("", "S")
    assert string_utils.starts_with(" 123", " ")


def test_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o")
    assert not string_utils.end_with("SkyPro", "y")
    assert not string_utils.end_with("", "o")
    assert string_utils.end_with("123 ", " ")


def test_is_empty(string_utils):
    assert string_utils.is_empty("")
    assert string_utils.is_empty(" ")
    assert not string_utils.is_empty("SkyPro")
    assert string_utils.is_empty("  ")
    assert not string_utils.is_empty("123")


def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([1]) == "1"
    assert string_utils.list_to_string([" ", ""]) == " , "
