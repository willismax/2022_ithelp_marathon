from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_current_url(driver: Chrome):
    driver.get("https://ithelp.ithome.com.tw/")

    correct_url = "https://ithelp.ithome.com.tw/"
    assert driver.current_url == correct_url

    correct_title_start = "iT 邦幫忙"
    assert driver.title.startswith(correct_title_start)


def test_text_visible(driver: Chrome):
    correct_text = "技術問答"

    driver.get("https://ithelp.ithome.com.tw/")
    question_h2_element = driver.find_element(
        By.CSS_SELECTOR, "h2.tab-title")

    assert question_h2_element.text == correct_text


def test_element_clickable(driver: Chrome):
    correct_options = ["技術問答", "技術文章", "iT 徵才",
                       "Tag", "聊天室", "2022 鐵人賽"]

    driver.get("https://ithelp.ithome.com.tw/")
    options = driver.find_element(
        By.CSS_SELECTOR, "ul.list-unstyled.menu__left")
    options = [tmp.text for tmp in options.find_elements(
        By.CSS_SELECTOR, "li.menu__item")]

    assert options == correct_options
