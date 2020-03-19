import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    RANK = 54

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}  # 오류 방지
    req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')

    time = parse.find_all("div", {"class": "calendar_prid"})
    now = []
    for t in time:  # 현재 시간 추출
        now.append(t.find("span", {"class": "year"}).text)
        now.append(t.find("span", {"class": "hour"}).text)

    # 제목, 가수, 앨범, 이미지url 추출
    titles = parse.find_all("div", {"class": "ellipsis rank01"})
    songs = parse.find_all("div", {"class": "ellipsis rank02"})
    albums = parse.find_all("div", {"class": "ellipsis rank03"})
    images = parse.find_all("a", {"class": "image_typeAll"})

    title = []
    song = []
    album = []
    image = []

    for t in titles:
        title.append(t.find('a').text)

    for s in songs:
        song.append(s.find('span', {"class": "checkEllipsis"}).text)

    for a in albums:
        album.append(a.find('a').text)

    for i in images:
        image.append(i.find('img')["src"])

    print("시간: ", now[0], now[1])
    print("순위 | 제목 | 가수 | 앨범 | 이미지")
    for i in range(RANK):
        pass
        print('%3d | %s | %s | %s | %s ' %
              (i+1, title[i], song[i], album[i], image[i]))
