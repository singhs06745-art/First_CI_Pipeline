import importlib

module = importlib.import_module("23_bubble_sort")
bubble_sort = module.bubble_sort


def test_unsorted_list():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


def test_already_sorted_list():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicate_numbers():
    assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_empty_list():
    assert bubble_sort([]) == []