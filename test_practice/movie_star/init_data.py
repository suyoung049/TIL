import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client.dbjungle


def get_urls():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    data = requests.get(
        "https://movie.naver.com/movie/sdb/rank/rpeople.nhn", headers=headers
    )
    soup = BeautifulSoup(data.text, "html.parser")
    # old_content > table > tbody > tr:nth-child(2) > td.title > a

    trs = soup.select("#old_content > table > tbody > tr")

    urls = []

    for tr in trs:
        a = tr.select_one("td.title > a")
        if a is not None:
            base_url = "https://movie.naver.com/"
            url = base_url + a["href"]
            urls.append(url)

    return urls


def insert_stars(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, "html.parser")

    # content > div.article > div.mv_info_area > div.mv_info.character > h3 > a
    name = soup.select_one(
        "#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a"
    ).text
    # content > div.article > div.mv_info_area > div.poster > img
    image = soup.select_one(
        "#content > div.article > div.mv_info_area > div.poster > img"
    )["src"]
    recent = soup.select_one(
        "#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)"
    ).text

    # content > div.article > div.mv_info_area > div.mv_info.character > dl > dd:nth-child(4) > a:nth-child(1)
    # content > div.article > div.mv_info_area > div.mv_info.character > dl > dd:nth-child(4) >
    # recent = soup.select('#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a')

    # test = []
    # for movie in recent:
    #     if movie.text != '더보기':
    #         test.append(movie.text)

    # print(test)

    doc = {"name": name, "img_url": image, "recent": recent, "url": url, "like": 0}

    db.mystar.insert_one(doc)
    print("완료!", name)


def insert_all():
    db.mystar.drop()
    urls = get_urls()
    for url in urls:
        insert_stars(url)


insert_all()
