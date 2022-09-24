import pytest


def test_select_permission(permission: list):
    if "select" in permission:
        assert True
    else:
        assert False


def test_update_permission(permission: list):
    if "update" in permission:
        assert True
    else:
        with pytest.raises(ValueError) as exc:
            raise ValueError("permission not allow")

        print(str(exc.value))
        assert str(exc.value) == "permission not allow"
