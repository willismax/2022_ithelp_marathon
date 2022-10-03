from contextlib import contextmanager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
    driver.get("https://ithelp.ithome.com.tw/questions")
    yield driver
    driver.quit()


def get_question_by_relative_xpath():
    with make_chrome_driver() as driver:
        xpath = "//div[@class='board tabs-content']/div[1]"
        question = driver.find_element(By.XPATH, xpath)
        print(question.text)


def get_questions_by_relative_xpath():
    with make_chrome_driver() as driver:
        xpath = "//div[@class='board tabs-content']/div[@class='qa-list']"
        questions = driver.find_elements(By.XPATH, xpath)
        print(len(questions))


if __name__ == '__main__':
    # get_question_by_relative_xpath()
    get_questions_by_relative_xpath()
