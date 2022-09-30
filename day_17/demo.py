from contextlib import contextmanager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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


if __name__ == '__main__':
    # demo_basic_infor()
    # demo_click_by_selenium()
    # demo_click_by_javascript()
    demo_input_keyboard()
