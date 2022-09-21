import pytest
import requests
from fake_useragent import FakeUserAgent


@pytest.fixture(name="headers", scope="function", autouse=False)
def headers_fixture() -> dict:
    ua = FakeUserAgent()
    headers = {"User-Agent": ua.random}

    return headers


@pytest.fixture(name="make_user_agent", scope="function", autouse=False)
def make_user_agent_fixture() -> dict:
    ua = FakeUserAgent()
    headers = {"User-Agent": ua.random}

    return headers


@pytest.fixture(name="parse_user_agent", scope="function", autouse=False)
def parse_user_agent_fixture(make_user_agent: dict) -> dict:
    url = "https://httpbin.org/headers"
    res = requests.get(url=url, headers=make_user_agent)
    user_agent = res.json()["headers"]['User-Agent']

    return {"User-Agent": user_agent}
