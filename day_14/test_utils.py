from utils import get_data


def test_crawler():
    # 建立測試參數
    url = "https://www.ptt.cc/bbs/index.html"

    # 呼叫方法
    result = get_data(url=url)

    # 進行驗證
    assert result
    for data in result:
        assert data.get("board")
        assert data.get("class")
        assert data.get("latest_paragraph")
