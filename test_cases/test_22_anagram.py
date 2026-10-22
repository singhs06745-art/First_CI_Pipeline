import importlib

module = importlib.import_module("22_anagram")
are_anagrams = module.are_anagrams


def test_anagrams():
    assert are_anagrams("listen", "silent") is True


def test_not_anagrams():
    assert are_anagrams("hello", "world") is False


def test_uppercase():
    assert are_anagrams("Listen", "Silent") is True


def test_spaces():
    assert are_anagrams("rail safety", "fairy tales") is True


def test_empty_strings():
    assert are_anagrams("", "") is True
