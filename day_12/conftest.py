import json
import pytest


def pytest_addoption(parser):
    parser.addoption("--permission", default="RD")


@pytest.fixture(name="permission")
def permission_fixture(pytestconfig):
    role = pytestconfig.getoption("permission")
    with open("./permission.json", "r") as file:
        permission_data = json.loads(file.read())
    if role == "RD":
        permission = permission_data["RD"]
    else:
        permission = permission_data["costumer"]

    return permission
