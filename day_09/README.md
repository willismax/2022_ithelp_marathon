# Python 與自動化測試的敲門磚_Day09_Pytest 與 MongoMock

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon)
如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

今天我們要來介紹 NoSQL 陣營的虛擬資料庫套件 - MongoMock，這個套件可以很好的協助我們在不實際建立 mongo 資料庫的情況下，
讓我們進行測試程式的撰寫，並且可以很好的兼容 pymongo 所產生出的 MongoClient，由於是 NoSQL 今天的專案目錄相較於昨天會
少了一個 models，同樣的資料格式的部分不是本次的重點，因此只會撰寫一個很簡單的 insert 方法來進行展示

## 一、套件安裝
- pymongo：正式用來撰寫 mongo 相關的 CRUD 時常用的套件，crud.py 內的 MongoClient，會由此套件產生
- mongomock：協助用來建立一個虛擬的 MongoClient 讓我們可以透過 fixture 的方式來進行 crud.py 的測試

```bash
poetry add pymongo

poetry add mongomock
```
or
```bash
pip install pymongo

pip install mongomock
```

## 二、建立 crud
這邊會在 crud.py 檔案內建立一個寫入資料的方式，直接附上範例並進行解說

注意：在正式的專案檔案中 (即非測試程式) 需要使用 pymongo 所提供的 MongoClient，才不會造成不可避免的錯誤

程式解析：
- import **pymongo** 的 MongoClient，進行 mongo 的 CRUD
- 建立一個 insert_user 函式
  - 進行資料的寫入
  - 寫入的同時取得 id
  - 寫入完畢後透過 id 查詢該筆資料並回傳
```python
from pymongo.mongo_client import MongoClient

database_name = "test"
collection_name = "user"


def insert_user(conn: MongoClient, data: dict) -> dict:
    # 插入資料並取得 id
    insert_id = conn[database_name][collection_name].insert_one(data).inserted_id

    # 藉由 id 搜尋並回傳
    result = conn[database_name][collection_name].find_one({"_id": insert_id})
    return result
```

## 三、建立 fixtures
接著我們要利用 MongoMock 所提供的 MongoClient 來進行 fixture 的撰寫，在開頭有提到，MongoMock 可以很好的兼容 PyMongo，因此我們可以直接使用
MongoMock 的 MongoClient 來進行 CRUD 的測試，範例如下

注意：雖然 MongoMock 可以很好的兼容 PyMongo 不過由於版本問題，某些功能還是會無法使用，因此若測試過程中有跳錯，請留意一下錯誤訊息，
看看是否為 MongoMock 還沒支援相關功能

程式解析：
- import **mongomock** 的 MongoClient
- 建立一個 fixture 命名為 conn
- 利用 mongomock 的 MongoClient 建立一個虛擬的連線
- 透過 yield 回傳出去給 test case 使用
```python
import pytest
from mongomock.mongo_client import MongoClient


@pytest.fixture(name="conn")
def mongo_client_fixture() -> MongoClient:
    with MongoClient() as conn:
        yield conn
```

## 四、test case 建立
最後我們要來建立測試程式了，直接附上範例進行解釋

程式解析：
- 將需要使用到的套件 import 進來
- 建立一筆假資料
- 調用 crud 當中的 insert_user 進行寫入測試
- 驗證回傳出的資料是否和我們建立的假資料內容一致
```python
from datetime import datetime
from pymongo.mongo_client import MongoClient
from fixtures import mongo_client_fixture
from crud import insert_user

use_fixtures = [mongo_client_fixture]


def test_insert_user(conn: MongoClient):
    # 建立假資料
    data = {"username": "nick",
            "email": "test@test",
            "birthday": datetime(year=2022, month=12, day=31)}
    
    # 測試 CRUD 方法
    result = insert_user(data=data, conn=conn)
    print(result)
    
    # 驗證內容
    assert result["username"] == data["username"]
    assert result["email"] == data["email"]
    assert result["birthday"] == data["birthday"]
```

## 五、內容預告
今天我們介紹了 MongoMock 他可以很快速地協助我們進行 mongodb 相關的 CRUD 函式進行測試，接下來我們會花 1 ~ 2 天的時間將一些零碎的 pytest 的方法補齊
相信在這之後，大家已經可以有能力架構出屬於你自己的測試程式了，加油!!