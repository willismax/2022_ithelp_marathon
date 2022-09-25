# Python 與自動化測試的敲門磚_Day13_TDD 開發流程與概念

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon)
如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

昨天我們結束了為期 11 天的 pytest 入門教學，接下來要花費兩天的時間來介紹 TDD 開發流程，今天主要以概念為主，
明天會實際利用 TDD 的概念來開發一個簡單的小腳本，來 demo 給大家看

## 一、TDD 簡介

TDD 全名為 Test-Driven Development 中文翻譯為 「測試驅動開發」，顧名思義就是藉著撰寫測試程式，來一步一步建構出我們的系統，
其倡導的概念為，先撰寫測試程式，再撰寫實際相對應的 function，因此程式開發者需要先行和 PM 或使用者討論系統需求，並逐步擬定測試計畫，
最後才會真正開始撰寫程式

採用 TDD 開發的好處有：

- 無須事後再補寫測試程式，會非常的痛苦
- 每一位 RD 都可以透過測試程式了解每個 function 的內容，較容易熟悉系統
- 可以確保每個 function 被更動時，可以馬上進行測試，降低錯誤產生

有好處當然也有壞處：

- 若系統需求溝通不良，會容易造成系統設計不良
- 測試程式有很大的機率只有 RD 部門看得懂，需要花費多於成本溝通

總結來說，筆者認為不論甚麼樣的方式，最重要的還是要保持持續溝通，只是說 TDD 這種開方方式，可以更方便的讓我們進行程式的開發，
尤其是不用在事後補寫測試程式以及可以邊寫邊測試 function 這點，真的是很方便，不過還是老話一句，規定是死的，人是活的，
不論是什麼工具，都應該要活用，而不是一昧地配合規定，找出適合自己的開發方式，才是最正確的寫程式的方法

接下來我們就針對 TDD 中的一些原則以及步驟來進行說明

## 二、TDD 的 3A 原則

在 TDD 當中，對於每個測試程式的撰寫有著 3A 原則 (步驟)，分別為 Arrange、Act 以及 Assert，下面按照順序來進行說明

下面這段程式碼是我們在 demo 3A 原則的時候要進行測試的函式

```python
def add_num(num1: int, num2: int) -> int:
    return num1 + num2
```

- Arrange 初始、期望結果

在這個步驟當中，我們要準備我們的測試環境、測試資料 以及預期結果

```python
def test_add_num():
    # Arrange
    num1 = 10
    num2 = 20
    except_result = 30
```

- Act 實際呼叫

在這個步驟當中，我們就會實際呼叫我們需要測試的 function 來驗證其正確性

```python
def test_add_num():
    # Arrange
    num1 = 10
    num2 = 20
    except_result = 30

    # Act
    result = add_num(num1, num2)
```

- Assert 驗證

最後我們才會進行驗證，看看該 function 是否如預期的回傳我們想要的值

```python
def test_add_num():
    # Arrange
    num1 = 10
    num2 = 20
    except_result = 30

    # Act
    result = add_num(num1, num2)

    # Assert
    assert result == except_result
```

以上就是 TDD 針對撰寫每一個 test case 的 3A 原則

## 三、TDD 的開發五步驟
接下來是要講的部分是，TDD 針對開發流程的五步驟，亦即每一組函式的開發過程 (function + test function)，分別為：

### (一)、新增測試程式
- 選定一個要撰寫的需求、功能 (function)
- 思考使用情境，準備測試環境以及資料
- 先建立測試函式，不要先寫 function 本身 (即先撰寫 test_function)
- 對應到 3A 中的 Arrange)

### (二)、執行測試程式 (亮紅燈)
- 由於還沒有實踐撰寫 function，因此在這個步驟一定會是錯誤
- 這個步驟要確定的是錯誤只發生在沒有撰寫 function 的部分，其他部分必須要確保可以正常運行，例如：fixture
  是否可以正常接收，測試資料語法是否錯誤

### (三)、撰寫 function
- 這個步驟我們要開始撰寫 function 本身
- 撰寫原則為以最低限度可以回傳正確資料為主，不需要對程式碼進行優化
- 對應到 3A 中的 Act

### (四)、執行測試程式 (亮綠燈)
- 確保撰寫的功能正常
- 驗證回傳資料是否正確
- 對應到 3A 中的 Assert

### (五)、優化程式
- 在前面四個步驟當中，我們已經將整組 function 以及 test_function 準備完成，接下來我們可以針對 function 進行重構
- 重構的過程當中我們可以不斷地執行測試程式，確保每一次改動都可以回傳正確資料

## 四、內容預告
今天我們簡單介紹了一下 TDD 的簡介、3A 原則以及開發五步驟，明天我們會實際利用 TDD 的開發五步驟來簡單時做一個小型的爬蟲腳本，
來為大家 demo 實際該如何使用 TDD 開發程式碼