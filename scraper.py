"""This web scraper collects information on which ward(s) in Tokyo 23 wards
have UR rental property vacancies available, and how many. """

from bs4 import BeautifulSoup
from re import compile
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen

# Initialize Selenium to crawl vacancy data
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.ur-net.go.jp/chintai/kanto/tokyo/area/")

pageSource = driver.page_source
bs = BeautifulSoup(pageSource, 'html.parser')

# Find wards element
wards = bs.find_all("li", 
                    {"class": "item_list js-searchMain", 
                     "data-count-key": compile("^1\d\d$")})

# Print out data
for ward in wards: 
    ward_name = ward.find("em", 
                          {"class": "js-label-text"}).get_text()
    ward_num = ward.find("span", 
                         {"class": "item_count js-searchMain-count"}).get_text()
    print(f"{ward_name}, {ward_num}")