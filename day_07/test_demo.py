import requests
from fixtures import headers_fixture, parse_user_agent_fixture, make_user_agent_fixture

# 單純不讓 pycharm 跳驚嘆號，沒有實際用途
use_fixtures = [headers_fixture, make_user_agent_fixture, parse_user_agent_fixture]


def test_assert_headers(headers: dict):
    url = "https://httpbin.org/headers"
    res = requests.get(url=url, headers=headers)

    print(res.status_code)
    print(res.json())

    assert res.status_code == 200
    assert res.json()['headers']["User-Agent"] == headers["User-Agent"]


def test_assert_user_agent(make_user_agent: dict, parse_user_agent: dict):
    assert make_user_agent == parse_user_agent
