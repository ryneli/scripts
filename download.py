from bs4 import BeautifulSoup
import requests
import shutil
from subprocess import call

page = requests.get("https://avgle.com/video/3456/%E5%9B%BD%E6%B0%91%E7%9A%84%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%AB%E8%B6%85%E5%A4%A7%E9%87%8F%E4%B8%80%E6%92%83%E3%83%89%E3%83%AA%E3%83%BC%E3%83%A0%E9%A1%94%E5%B0%84-%E4%B8%89%E4%B8%8A%E6%82%A0%E4%BA%9C-snis-825")
soup = BeautifulSoup(page.text, 'html.parser')
items = soup.select('video > source');
for item in items:
    print(item.attrs['src'])
    call(["wget", item.attrs['src']])
