# Python 與自動化測試的敲門磚_Day27_Pytest 與 Mock

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon)
如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

這邊做個整裡並說聲抱歉，由於時程安排的關係，Appium 以及 Jenkins 在本次鐵人賽當中進行說明，接下來的日子裡會繼續針對 pytest
相關功能進行補充，
至於 Appium 以及 Jenkins 會放到鐵人賽之後另外開系列文章進行教學與說明

## 一、情境說明及套件安裝

今天我們要說明該如何再進行測試時，把不想要執行的方法給替換掉，在測試的過程中，有時候只是要測試函式的可用性，
但像是發送 email、撰寫檔案等等的函式，往往是不希望被執行的，總不能每執行一次測試就寄一封 mail 給你，這樣信箱會很快就爆炸的，
針對這個情況我們就可以透過 pytest-mock 來替我們進行函式的抽換，並回傳假的資料，只要確認函式運行的流程是正確的即可

pytest-mock 為一個第三方套件，也是以 unittest 裡面的 mock 進行開發而成，安裝方法如下

- pip

```shell
pip install pytest-mock
```

- poetry

```shell
poetry add pytest-mock
```

## 二、抽換屬性

### (一)、建立函式 demo.py

- 建立一個透過 sys 取得 platform 的函式

```python
import sys


def get_sys_platform():
    platform = sys.platform
    return platform
```

### (二)、建立測試函式 test_demo.py

- 將會用到的 package 全部 import 近來
- 直接在 test case 當中的參數部分打上 mocker 即可進行使用，後面的 `MockFixture` 只是用來提式型態用的
- 建立一個變數用來存放假的回傳資料，此樹使用 new (對齊 mock.path 函式的參數)

  ```python
  import sys
  import demo
  from pytest_mock import MockFixture
  
  
  def test_mock_object(mocker: MockFixture):
      new = "test_mock"
  ```

- 使用 mocker.patch.object 進行變數的替換
    - target：指定要替換的物件
    - attribute：指定要替換的物件的屬性
    - new：要回傳的假資料

  ```python
  import sys
  import demo
  from pytest_mock import MockFixture
  
  
  def test_mock_object(mocker: MockFixture):
      new = "test_mock"
  
      mocker.patch.object(target=sys,
                          attribute="platform",
                          new=new)
  ```

- 實際呼叫想要測試的函式並進行驗證
    ```python
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
    ```
  
- 下圖中我們實際執行此測試函式，可以看到終端機上印出 test_mock 字串且測試結果為 passed
  
  ![img](img/attr_result.jpg)

## 三、抽換函式
### (一)、建立函式
```python
def add(num1, num2):
    return num1 + num2


def calculate(num1, num2):
    add_result = add(num1=num1, num2=num2)

    return add_result
```

### (二)、建立測試函式
- 透過 `mocker.patch` 直接進行抽換
  - target：使用 "字串" 指定要抽換的函式路徑，當成式執行到此函式時，會直接回傳一個假資料並不會實際執行該函式
  - return_value：指定要回傳的假資料
  ```python
  import demo
  from pytest_mock import MockFixture
  
  
  def test_mock_function(mocker: MockFixture):
      return_value = 100
  
      mocker.patch(target="demo.add",
                   return_value=return_value)
  
      result = demo.calculate(num1=10, num2=10)
      print(result)
  
      assert result == return_value
  ```

- 結果展示
  ![img](img/function_result.jpg)