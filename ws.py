import urllib.request
from urllib.parse import urljoin  # URLを扱うモジュールを追加
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "actl/news" in url:
                print("\n" + urljoin(self.site, url))


news = "https://trendy.nikkeibp.co.jp/news/"
Scraper(news).scrape()
