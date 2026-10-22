import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_common_elements():
    assert set_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_no_common_elements():
    assert set_intersection([1, 2], [3, 4]) == []


def test_duplicate_elements():
    assert set_intersection([1, 2, 2, 3], [2, 2, 4]) == [2]


def test_empty_first_list():
    assert set_intersection([], [1, 2]) == []


def test_empty_second_list():
    assert set_intersection([1, 2], []) == []