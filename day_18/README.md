# Python 與自動化測試的敲門磚_Day18_Selenium 手刻測試程式

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon) 如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

今天我們要來實際制訂一些簡單的測試範例，並利用 pytest 執行測試，讓大家看看實際利用 Selenium 進行測試時，test case 有可能會長成什麼樣子

## 一、建立測試目標
1. 確認瀏覽器請求網址後的網址是否為 "https://ithelp.ithome.com.tw/"，title 開頭是否為 "iT 邦幫忙"
2. 確認請求 "https://ithelp.ithome.com.tw/" 後，網頁上是否有出現 "技術問答" 字樣，且 HTML tag 為 h2
3. 確認請求 "https://ithelp.ithome.com.tw/" 後，網也上是否有出現 "技術問答"、"技術文章"... 等選項按鈕

## 二、建立 conftest.py
在開始撰寫測試程式前，我們可以先撰寫 fixture 方便後續的測試進行，而由於 driver 確定是每個 test case 都會使用到的功能，
因此我們將此 fixture 撰寫在 conftest.py 當中

- conftest.py
```python
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(name="driver")
def driver_fixture() -> Chrome:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

    driver = Chrome(ChromeDriverManager().install(),
                    options=options)

    yield driver

    driver.quit()
```

## 三、驗證 url 及 title
程式解析：
- 先對指定網址進行請求
- 驗證請求後跳轉的網址是否正確
- 驗證跳轉網址後的頁面的 title 是否開頭為 "iT 邦幫忙"
```python
from selenium.webdriver import Chrome


def test_current_url(driver: Chrome):
    driver.get("https://ithelp.ithome.com.tw/")

    correct_url = "https://ithelp.ithome.com.tw/"
    assert driver.current_url == correct_url

    correct_title_start = "iT 邦幫忙"
    assert driver.title.startswith(correct_title_start)
```

## 四、驗證元素文字是否正確
程式解析：
- 建立測試資料
- 進行請求
- 透過 CSS_SELECTOR 找到元素
- 驗證該元素的 text 內容是否符合測試資料
```python
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_text_visible(driver: Chrome):
    correct_text = "技術問答"

    driver.get("https://ithelp.ithome.com.tw/")
    question_h2_element = driver.find_element(By.CSS_SELECTOR, "h2.tab-title")

    assert question_h2_element.text == correct_text
```

## 五、驗證按鈕選項是否都有出現
程式解析：
- 建立測試資料
- 進行請求
- 透過 driver 先找到位於左方的選項列表元素 (ul)
- 在針對該元素尋找所有的選項內容 (li) 並透過 generator 的方式取得文字內容串列
- 文字內容串列是否符合正確的測試資料
```python
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_element_clickable(driver: Chrome):
    correct_options = ["技術問答", "技術文章", "iT 徵才", "Tag", "聊天室", "2022 鐵人賽"]

    driver.get("https://ithelp.ithome.com.tw/")
    options = driver.find_element(By.CSS_SELECTOR, "ul.list-unstyled.menu__left")
    options = [tmp.text for tmp in options.find_elements(By.CSS_SELECTOR, "li.menu__item")]

    assert options == correct_options
```


## 六、內容預告
今天我們簡單用幾個範例展示了該如何透過 Selenium 制定前端的測試案例，一旦完善後，便可於每次更新之前透過執行腳本自動化進行一些常規測試，
減少我們人工測試的時間，並且也可以避免一些該測但卻遺漏沒有測到的部分，未來搭配 CI/CD 更可以在每次 push 的時候都對其自動進行測試，有問題會馬上通報開發人員進行修正，
明天我們要來介紹 Selenium IDE 這個瀏覽器上的套件，他可以協助我們用 "錄製腳本" 的方式來進行測試，並且可以輸出成 python 測試腳本，讓我們放入 CI/CD 當中，
是一個非常便利的小工具
