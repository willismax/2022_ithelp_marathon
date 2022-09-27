import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(name="driver")
def driver_fixture() -> Chrome:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")

    driver = Chrome(ChromeDriverManager().install(),
                    options=options)

    yield driver

    driver.quit()
