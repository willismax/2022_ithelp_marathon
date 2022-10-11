# Python 與自動化測試的敲門磚_Day28_Pytest 與客製化

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon)
如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

今天我們要來介紹如何客製化自己的 pytest，透過設定 pytest.ini 即可讓我們進行一些簡單的客製化，
讓 pytest 更符合我們的需求

## 一、預設指令

透過設定 pytest.ini 我們可以達到每次執行 pytest 時，會自動帶入指定的參數，例如：-s、-v ...

- 於整個專案最外層建立 pytest.ini 檔案

  ![img](img/dir.jpg)

- 編輯 pytest.ini
  
  下面的範例當中，我們設定了在使用 pytest 時會自動帶入 -s、-v 參數，並且設定當發生一次錯誤時就會停止測試
    ```ini
    [pytest]

    addopts = --maxfail=1 -s -v 
    ```

- 建立測試程式
  
  可以看到下面的範例當中，我們利用參數化的方式建立了四次測試
    ```python
    import pytest

    argvalues = [[1, 1, 2], [2, 2, 5], [3, 3, 7], [4, 4, 8]]
    
    
    @pytest.mark.parametrize(argnames='num1, num2, result', argvalues=argvalues)
    def test_add(num1: int, num2: int, result: int):
        assert num1 + num2 == result
    ```

- 結果展示

  可以看到下圖執行結果當中，pytest 只有執行了兩次測試，並且其中一次為錯誤
  ![img](img/max_error.jpg)

  正常來說應該會有四次的測試結果，下圖為沒有設定 pytest.ini 時的情況，pytest 就成功執行了四次測試並且其中兩次為錯誤
  ![img](img/max_error_no_ini.jpg)
  
## 二、蒐集條件
pytest 預設會自動蒐集開頭為 test 的 function，當然這個部份我們也可以透過 pytest.ini 來進行設定

- 編輯 pytest.ini

  ```ini
  [pytest]
  python_functions = test_* example_*
  ```
  
- 建立測試程式
  
  下方利用參數化的方式建立兩個測試函式，總共數量會是八個測試，並分別用 test_ 開頭以及 example_ 開頭
  ```python
  import pytest
  
  argvalues = [[1, 1, 2], [2, 2, 5], [3, 3, 7], [4, 4, 8]]
  
  
  @pytest.mark.parametrize(argnames='num1, num2, result', argvalues=argvalues)
  def test_add(num1: int, num2: int, result: int):
      assert num1 + num2 == result
  
  
  @pytest.mark.parametrize(argnames='num1, num2, result', argvalues=argvalues)
  def example_add(num1: int, num2: int, result: int):
      assert num1 + num2 == result
  ```
  
- 利用 pytest --co 觀察蒐集到的測試函式數量，可以看到成功蒐集到八個測試

  ![img](img/collect.jpg)

## 三、參考資料
透過閱讀 [官方文件](https://docs.pytest.org/en/6.2.x/reference.html#ini-options-ref) 可以知道更多 pytest.ini 相關的設定，
讓 pytest 測試更加客製化