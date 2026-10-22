import importlib

module = importlib.import_module("26_sum_without_sum")
calculate_sum = module.calculate_sum


def test_positive_numbers():
    assert calculate_sum([1, 2, 3, 4]) == 10


def test_negative_numbers():
    assert calculate_sum([-1, -2, -3]) == -6


def test_mixed_numbers():
    assert calculate_sum([10, -5, 2]) == 7


def test_empty_list():
    assert calculate_sum([]) == 0


def test_single_number():
    assert calculate_sum([8]) == 8