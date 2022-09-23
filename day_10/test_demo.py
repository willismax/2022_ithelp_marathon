import sys
import pytest


def raise_error():
    raise IndexError("list 的位置錯誤")


# 只對第一行有效
def test_error():
    with pytest.raises(IndexError):
        raise_error()

    # assert 1 + 1 == 3


# 針對錯誤訊息做驗證
def test_error_message():
    # 將接收到的錯誤丟給一個名為 exc 的變數，該變數可於外部使用
    with pytest.raises(IndexError) as exc:
        raise_error()

    # 印出錯誤訊息內容並驗證
    print(str(exc.value))
    assert str(exc.value) == "list 的位置錯誤"

    # 印出錯誤訊息類別並驗證
    print(str(exc.typename))
    assert exc.typename == IndexError.__name__


@pytest.mark.skip(reason="測試案例跳過範例")
def test_skip_test_case():
    assert 1 + 1 == 3


@pytest.mark.skipif(condition=sys.platform == "win32", reason="測試跳過指定條件範例")
def test_skip_test_case_by_condition():
    assert 1 + 1 == 4
