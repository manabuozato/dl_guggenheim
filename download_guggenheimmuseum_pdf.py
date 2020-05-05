import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path

#bsでarchive.org上のguggenheimをスクレイピング
load_url = "https://archive.org/details/guggenheimmuseum"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

#ダウンロード可能な図録をpdfでダウンロード
for element in soup.select("div.item-ttl > a"):
    url = element.get("href")
    link_url = urllib.parse.urljoin(load_url, url)
    filename = link_url.split("/")[-1]
    download_url = "https://archive.org/download/"+filename+"/"+filename+".pdf"
    save_name = filename+".mobi"
    print(download_url)
    urllib.request.urlretrieve(download_url, save_name)
