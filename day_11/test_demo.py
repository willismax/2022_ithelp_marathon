import json
import pytest
from fixtures import mongo_client_fixture
from mongomock.mongo_client import MongoClient


# 基本範例
@pytest.mark.parametrize(argnames='num1, num2, result', argvalues=[[1, 1, 2], [2, 2, 4]])
def test_add(num1: int, num2: int, result: int):
    assert num1 + num2 == result


# 搭配檔案讀取
with open("./test_args.json", "r", encoding="utf8") as file:
    test_args = json.loads(file.read())['test_add']


@pytest.mark.parametrize(argnames='num1, num2, result', argvalues=test_args)
def test_add_with_json_file(num1: int, num2: int, result: int):
    assert num1 + num2 == result


# ids 的使用
ids = [f"case: {i}" for i in range(1, len(test_args) + 1)]


@pytest.mark.parametrize(argnames='num1, num2, result', argvalues=test_args, ids=ids)
def test_add_with_json_file_and_ids(num1: int, num2: int, result: int):
    assert num1 + num2 == result


use_fixtures = [mongo_client_fixture]


# 搭配 fixture 使用
@pytest.mark.parametrize(argnames='num1, num2, result', argvalues=[(1, 1, 2), (2, 2, 4)])
def test_add_with_fixtures(num1: int, num2: int, result: int, conn: MongoClient):
    assert num1 + num2 == result
    assert isinstance(conn, MongoClient)
