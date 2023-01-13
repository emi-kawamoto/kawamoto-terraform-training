from bs4 import BeautifulSoup
import urllib.request as req

url = "https://blog.flinters-base.co.jp/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# タイトルを表示
print(soup.find("title").text)

# a タグ（リンク）の一覧を表示
links = soup.find_all("a")
for link in links:
    print(link.contents[0])
