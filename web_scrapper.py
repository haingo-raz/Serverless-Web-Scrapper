import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

# Wikipedia URL
URL = "https://en.wikipedia.org/wiki/Main_Page"

# Get today's date
today = datetime.today().strftime("%B %d, %Y")
json_filename = datetime.today().strftime("on_this_day_%Y-%m-%d.json")

# Fetch the page
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Locate "On this day" section
otd_content = soup.find("div", id="mp-otd") # Events will be the direct children of the div with id mp-otd
otd_births_and_deaths = soup.select("div#mp-otd div.hlist ul li")

events = []
births = []
deaths = []

if otd_content:
    for ul in otd_content.find_all("ul", recursive=False):
        for li in ul.find_all("li", recursive=False):
            text = ' '.join(li.stripped_strings).strip()
            events.append(text)

if otd_births_and_deaths:
    for li in otd_births_and_deaths:
            text = ' '.join(li.stripped_strings).strip()
            if "(b." in text or "( b." in text:
                births.append(text)
            elif "(d." in text or "( d." in text:
                deaths.append(text)

# Save in JSON format
data = {today: {"events": events, "births": births, "deaths": deaths}}
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

