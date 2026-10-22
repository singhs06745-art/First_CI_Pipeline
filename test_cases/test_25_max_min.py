import importlib

module = importlib.import_module("25_max_min")
find_max_min = module.find_max_min


def test_positive_numbers():
    assert find_max_min([3, 1, 9, 5]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -10]) == (-2, -10)


def test_single_number():
    assert find_max_min([7]) == (7, 7)


def test_duplicate_numbers():
    assert find_max_min([4, 4, 4]) == (4, 4)


def test_empty_list():
    assert find_max_min([]) == (None, None)