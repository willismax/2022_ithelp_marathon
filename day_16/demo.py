from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = "https://www.ptt.cc/bbs/index.html"


def make_chrome_driver() -> Chrome:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")

    driver = Chrome(ChromeDriverManager().install(),
                    options=options)
    return driver


def demo_css_selector():
    driver = make_chrome_driver()
    driver.get(url=url)

    data = driver.find_element(By.CSS_SELECTOR, "div.b-ent").text
    print(data)

    datas = driver.find_elements(By.CSS_SELECTOR, "div.b-ent")
    [print(tmp.text) for tmp in datas]


def demo_xpath():
    driver = make_chrome_driver()
    driver.get(url=url)

    data = driver.find_element(By.XPATH, "//*[@id='main-container']/div[2]/div[1]").get_attribute("class")
    print(data)

    datas = driver.find_elements(By.XPATH, "//*[@id='main-container']/div[2]/div")
    [print(tmp.get_attribute("class")) for tmp in datas]


def demo_wait():
    driver = make_chrome_driver()
    driver.get(url=url)

    data = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "div.b-ent"))).text
    print(data)

    datas = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, "div.b-ent")))
    [print(tmp.text) for tmp in datas]


if __name__ == '__main__':
    demo_css_selector()
    demo_xpath()
    demo_wait()
