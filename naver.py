# pip install requests beautifulsoup4

import requests

source = requests.get("https://www.naver.com/srchrank?frm=main").json()
ranks = source.get("data")
for row in ranks:
    print(str(row.get("rank")) + ". " + row.get("keyword"))
