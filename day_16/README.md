# Python 與自動化測試的敲門磚_Day16_Selenium 定位元素

每天的專案會同步到 github 上，可以前往 [這個網址](https://github.com/nickchen1998/2022_ithelp_marathon) 如果對於專案有興趣或是想討論一些問題，歡迎留言 OR 來信討論，信箱為：nickchen1998@gmail.com

昨天我們快速講解了該如何透過 selenium 開啟一個瀏覽器並對網址進行請求，也介紹了該如何設定瀏覽器的方式，例如：背景運行... 等等，
今天我們要來介紹在瀏覽器開啟之後，我們該如何找到我們想要的元素在哪裡以及如何取得該元素的一些相關資訊

## 一、建立 driver 函式
首先我們先建立一個通用的可以回傳 driver 的函式，這個部份我們昨天介紹過了，今天就直接上範例方便大家對應函式名稱

本次進行範例說明所請求的網址為 PTT 熱門版，下方範例中有附上網址
```python
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.ptt.cc/bbs/index.html"


def make_chrome_driver() -> Chrome:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")

    driver = Chrome(ChromeDriverManager().install(),
                    options=options)
    return driver
```

## 二、使用 CSS_SELECTOR 定位
Selenium 的官方文件中，提供了許多種定位 HTML 元素的方式，今天我們就挑兩種比較常用的來進行介紹，首先我們先介紹 CSS_SELECTOR

CSS_SELECTOR 語法：`<html 元素名稱><CSS 名稱>`，其中 CSS 名稱可以是複數個，下面附上使用範例
至於該如何取得 CSS，我們可以透過在網頁上按又鍵開啟 "檢查" 選項來進行查看

程式解析：
- 取得 driver 並進行請求
- 使用 driver.find_element 來尋找元素，並指定使用 CSS_SELECTOR 進行尋找，第二個參數為 CSS 條件
- 印出該元素的資訊
- 使用 driver.find_elements 尋找所有在葉面上已出現並符合 CSS 條件的資訊
- 透過 generator 的方式來印出所有元素的文字資訊

補充說明：
每一個透過 selenium 都一定有 text 屬性以及 get_attribute() 方法，其中 text 會印出該元素下所有的文字資訊，
get_attribute() 則可以該元素的相關資訊，例如：class、href ... 等等，下方的範例為取得 text
```python
from selenium.webdriver.common.by import By

def demo_css_selector():
    driver = make_chrome_driver()
    driver.get(url=url)
    
    # 回傳最先找到的元素，若沒有找到則會跳 error
    data = driver.find_element(By.CSS_SELECTOR, "div.b-ent").text
    print(data)
    
    # 會尋找目前葉面當中所有符合條件的元素，並回傳一個 list，若沒找到會回傳一個空 list
    datas = driver.find_elements(By.CSS_SELECTOR, "div.b-ent")
    [print(tmp.text) for tmp in datas]
```

## 三、使用 XPATH 定位
接下來的範例當中，我們會使用 XPATH 的方式尋找元素，並使用 get_attribute() 來取得該元素的 class

補充：我們同樣可以透過 "檢查" 來複製該元素在網頁上的 XPATH
1. 在 "檢查" 當中找到該元素
2. 對該元素點選右鍵，選取 "複製" -> "複製 XPATH" or "複製完整 XPATH"

至於 XPATH 的使用方式則不是本次重點，之後可以在鐵人賽後找時間進行說明

程式解析：
運作羅基基本上一樣，只是 By.CSS_SELECTOR 更換成 By.XPATH，並搭配 XPATH 條件
```python
def demo_xpath():
    driver = make_chrome_driver()
    driver.get(url=url)

    data = driver.find_element(By.XPATH, "//*[@id='main-container']/div[2]/div[1]").get_attribute("class")
    print(data)

    datas = driver.find_elements(By.XPATH, "//*[@id='main-container']/div[2]/div")
    [print(tmp.get_attribute("class")) for tmp in datas]
```

## 四、等待元素出現
由於 selenium 是實際開啟一個瀏覽器來進行請求，因此會受限於各種情況導致元素會比較慢出現，因此 selenium 提供了一種等待元素的方式，
下面附上使用範例

程式解析：
- 透過 WebDriverWait 進行元素的等待，告訴 Selenium 等待該元素 10 秒，當元素在 10 秒內出現，則會繼續進行下一段程式，但是超過 10 秒還沒出現，則會拋出 Timeout 錯誤
- ec.presence_of_element_located 則表示要去尋找目前出現在畫面上的元素，和下方的 of_all 差別為單數之分，用法同 find_element
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def demo_wait():
    driver = make_chrome_driver()
    driver.get(url=url)
    
    # 單個元素，回傳 webelement 物件
    data = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "div.b-ent"))).text
    print(data)
    
    # 多個元素，回傳 list
    datas = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, "div.b-ent")))
    [print(tmp.text) for tmp in datas]
```

## 五、內容預告
今天我們介紹了一些針對 selenium 該如何找到我們想要的 HTML 元素，並說明該如何取得元素相關的資訊，上面的範例大家可以實際複至下來並執行看看效果如何，
明天我們會針對如何透過 selenium 進行 "瀏覽器" 本身的操作，例如：鍵盤打字、回到上一頁... 等等