"""This web scraper collects information on which ward(s) in Tokyo 23 wards
have UR rental property vacancies available, and how many. """

from bs4 import BeautifulSoup
from re import compile
from urllib.request import urlopen

html = urlopen("https://www.ur-net.go.jp/chintai/kanto/tokyo/area/")
bs = BeautifulSoup(html, 'html.parser')

zones = bs.find_all("label", 
                    {"for": compile("^area_0[1-5]$")})
for zone in zones: 
    print(zone.get_text().strip())