import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_website():
    try:
        URL = "https://en.wikipedia.org/wiki/Main_Page" # Wikipedia URL
        
        # Get today's date
        today = datetime.today().strftime("%B %d, %Y")
        json_filename = datetime.today().strftime("on_this_day_%Y-%m-%d.json")

        print(f"Fetching Wikipedia page: {URL}")
        response = requests.get(URL)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch page, status code: {response.status_code}")

        soup = BeautifulSoup(response.content, "html.parser")

        # Locate "On this day" section
        otd_content = soup.find("div", id="mp-otd")
        otd_births_and_deaths = soup.select("div#mp-otd div.hlist ul li")

        events, births, deaths = [], [], []

        if otd_content:
            print("Extracting events...")
            for ul in otd_content.find_all("ul", recursive=False):
                for li in ul.find_all("li", recursive=False):
                    text = ' '.join(li.stripped_strings).strip()
                    events.append(text)
        else:
            print("No events found.")

        if otd_births_and_deaths:
            print("Extracting births and deaths...")
            for li in otd_births_and_deaths:
                text = ' '.join(li.stripped_strings).strip()
                if "(b." in text or "( b." in text:
                    births.append(text)
                elif "(d." in text or "( d." in text:
                    deaths.append(text)
        else:
            print("No births or deaths found.")

        print(f"Scraped {len(events)} events, {len(births)} births, and {len(deaths)} deaths.")

        return today, json_filename, events, births, deaths

    except Exception as e:
        print(f"Error during scraping: {e}")
        return None, None, [], [], []