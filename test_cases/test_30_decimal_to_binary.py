import importlib

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_decimal_10():
    assert decimal_to_binary(10) == "1010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one():
    assert decimal_to_binary(1) == "1"


def test_decimal_7():
    assert decimal_to_binary(7) == "111"


def test_decimal_18():
    assert decimal_to_binary(18) == "10010"