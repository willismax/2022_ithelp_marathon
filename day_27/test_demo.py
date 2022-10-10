import sys
import demo
from pytest_mock import MockFixture


def test_mock_object(mocker: MockFixture):
    new = "test_mock"
    mocker.patch.object(target=sys,
                        attribute="platform",
                        new=new)

    result = demo.get_sys_platform()
    print(result)

    assert result == new


def test_mock_function(mocker: MockFixture):
    return_value = 100

    mocker.patch(target="demo.add",
                 return_value=return_value)

    result = demo.calculate(num1=10, num2=10)
    print(result)

    assert result == return_value
