import pytest

argvalues = [[1, 1, 2], [2, 2, 5], [3, 3, 7], [4, 4, 8]]


@pytest.mark.parametrize(argnames='num1, num2, result', argvalues=argvalues)
def test_add(num1: int, num2: int, result: int):
    assert num1 + num2 == result


@pytest.mark.parametrize(argnames='num1, num2, result', argvalues=argvalues)
def example_add(num1: int, num2: int, result: int):
    assert num1 + num2 == result
