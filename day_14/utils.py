import requests
from bs4 import BeautifulSoup
from pprint import pprint


def get_data(url: str) -> list:
    res = requests.get(url=url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "lxml")

        result = []
        targets = soup.find_all("div", class_="b-ent")
        for target in targets:
            tmp = {"board": target.find("div", class_="board-name").text,
                   "class": target.find("div", class_="board-class").text,
                   "latest_paragraph": target.find("div", class_="board-title").text}
            result.append(tmp)

        pprint(result)
        return result


if __name__ == '__main__':
    get_data(url="https://www.ptt.cc/bbs/index.html")