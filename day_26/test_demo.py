from selenium.webdriver import Remote, Chrome
from typing import Union


def test_current_url(driver: Union[Remote, Chrome]):
    driver.get("https://ithelp.ithome.com.tw/")

    correct_url = "https://ithelp.ithome.com.tw/"
    assert driver.current_url == correct_url

    correct_title_start = "iT 邦幫忙"
    assert driver.title.startswith(correct_title_start)
