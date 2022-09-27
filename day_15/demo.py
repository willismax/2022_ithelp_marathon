from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def make_webdriver() -> Chrome:
    options = create_options()
    driver = Chrome(ChromeDriverManager().install(),
                    options=options)

    return driver


def create_options() -> Options:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")

    return options


if __name__ == '__main__':
    url = "https://ithelp.ithome.com.tw/questions"
    _driver = make_webdriver()

    _driver.get(url=url)

    _driver.quit()
