# Python 與自動化測試的敲門磚_Day17_Selenium 瀏覽器基本操作

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon) 如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

昨天我們介紹了該如何利用 selenium 找到元素，今天我們要來介紹，找到元素後，該如和對元素進行一些操作，例如：點選、發送文字... 等等，
另外也會介紹該如何取得一些網頁的基本資訊，取得的資料也可以作為驗證項目放入 test case 當中

## 一、建立 driver 函式
同樣的我們今天一樣先附上建立 driver 的函式，今天比較不一樣的地方是，我們透過 contextmanager 來建立，
這樣我們就可以透過 yield 以及 with 的方式來操作 driver，並於操作結束後會自動回到此函式內執行 driver.quit()，
以此確保瀏覽器會被完全關閉，不殘留在記憶體當中

另外我們今天爬取的目標是 ithelp，因此代入 user-agent 以免被誤認為是機器人而造成範例失敗，
理論上如果是拿來測試網頁的話，應該是不用帶入這個參數的，不過還是要視情況而定
```python
from contextlib import contextmanager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

@contextmanager
def make_chrome_driver() -> Chrome:
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

## 二、取得基本資訊
我們可以透過 driver 物件本身取得一些瀏覽器的資訊，下面列舉三點並附上程式碼做參考：
- driver.current_url：取得瀏覽器目前所在頁面的網址
- driver.title：取得瀏覽器目前所在頁面的 title，就是我們可以在瀏覽器最上方看到的分頁的名稱
- driver.page_source：取得瀏覽器目前所在頁面的 HTML Code，取得後可透過 BeautifulSoup 進行網頁解析

```python
def demo_basic_info():
    with make_chrome_driver() as driver:
        driver.get("https://ithelp.ithome.com.tw/")

        # 取得目前頁面的網址
        current_url = driver.current_url
        print(current_url)

        # 取得目前頁面的 title
        current_title = driver.title
        print(current_title)

        # 取得目前頁面的 HTML Code
        current_code = driver.page_source
        print(current_code)
```

## 三、點選元素
在 selenium 當中點選元素的方式有兩種，分別為透過 selenium 找到元素後進行點選以及找到元素後透過執行 javascript 進行點選，
後者通常用於當要被點選的按鈕被某個跳出視窗遮住，或是畫面上被隱藏但是 HTML Code 實際上是存在時，我們就可以透過執行 javascript
直接對其進行點選的動作

### (一)、使用 Selenium 點選
程式解析：
- 利用 selenium 找到 "技術文章" 按鈕元素
- 透過呼叫元素當中的 click() 方法即代表使用 selenium 內建的方式進行點選
- 點選該元素後頁面會進行跳轉，於點選後透過 driver.current_url 來取得該頁面網址
- 驗證取得的網址是否如同預期該出現的網址內容
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def demo_click_by_selenium():
    with make_chrome_driver() as driver:
        driver.get("https://ithelp.ithome.com.tw/")
        technical_article_button = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/nav/div[1]/div/ul[1]/li[2]/a")))

        # click by selenium
        technical_article_button.click()

        technical_article_url = "https://ithelp.ithome.com.tw/articles?tab=tech"
        current_url = driver.current_url

        assert current_url == technical_article_url
```

### (二)、使用 Javascript 點選
語法：`driver.execute_script("arguments[0].click();", <元素名稱>)`

程式解析：
運作邏輯基本同上面一樣，差別只在於透過 javascript 執行點選的部分，有特別使用註解標記
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def demo_click_by_javascript():
    with make_chrome_driver() as driver:
        driver.get("https://ithelp.ithome.com.tw/")
        technical_article_button = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/nav/div[1]/div/ul[1]/li[2]/a")))

        # click by js
        driver.execute_script("arguments[0].click();", technical_article_button)

        technical_article_url = "https://ithelp.ithome.com.tw/articles?tab=tech"
        current_url = driver.current_url

        assert current_url == technical_article_url
```

## 四、鍵盤操作
在 selenium 當中，我們可以透過 send_keys() 方法來對元素進行文字的輸入，另外也可以透過 selenium 提供的 Keys 類別來模擬鍵盤的操作，
下面的範例當中我們就分別使用上述兩種方法來進行帳號密碼的輸入，並用 Enter 鍵進行確認

程式解析：
- 先分別透過 selenium 找到輸入帳號、密碼的元素
- 利用 send_keys() 輸入帳號及密碼
- 輸入完成後於 password 利用 Keys 模擬 Enter 鍵的操作進行確認以及頁面跳轉
- 於跳轉後，取得 user name 並進行驗證
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def demo_input_keyboard():
    with make_chrome_driver() as driver:
        driver.get("https://member.ithome.com.tw/login")
        account = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, "//*[@id='account']")))
        password = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, "//*[@id='password']")))

        account.send_keys("<你的帳號>")
        password.send_keys("<你的密碼>")
        password.send_keys(Keys.ENTER)

        user_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='editNickname']")))

        assert user_name.text == "熊熊工程師"
```

## 五、內容預告
到今天為止我們花了三天的時間介紹了一些 Selenium 的基本用法，包含建立 driver、元素定位以及瀏覽器操作，明天開始我們會進入該如何透過 Selenium 進行
測試的部分，其實在今天的內容當中，就有包含一點點測試的部分了，例如：驗證 username 是否如預期出現、網址是否如預期一樣等等，明天我們會為大家實際制訂幾個簡單的測試目標並實際撰寫出 test case 讓他家看看如果寫成測試程式的話，程式大概會長的如何