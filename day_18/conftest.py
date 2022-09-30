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
