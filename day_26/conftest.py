import sys
import pytest
from typing import Union
from selenium.webdriver import Remote, Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(name="driver")
def driver_fixture() -> Union[Remote, Chrome]:
    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

    if sys.platform == "win32":
        driver = Chrome(ChromeDriverManager().install(),
                        options=options)
    else:
        driver = Remote(command_executor="http://CICD_Selenium:4444/wd/hub",
                        options=options)

    yield driver

    driver.quit()
