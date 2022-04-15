# https://data.world/petrsevcik/testproject/workspace/file?agentid=arthur&datasetid=banks&filename=top100banks2017-12-31.xlsx
import csv
from itertools import islice
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from os import path


# http://planecrashinfo.com/database.htm

def create_link_queue(from_year=1921, to_year=2021):
    url_queue = []
    BASE_URL = "http://planecrashinfo.com/"
    for year in range(from_year, to_year):
        url = f"{BASE_URL}{year}/{year}.htm"
        url_queue.append(url)
    return url_queue


def scrape_data_from_page(page_url):
    crash_data = []
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, "html.parser")
    table_rows = soup.find_all("tr")
    for row in islice(table_rows, 1, None):  # skip table headers
        table_fields = row.find_all("td")
        date = table_fields[0].text
        location_operator = table_fields[1].text.strip()
        aircraft_type_and_registration = table_fields[2].text
        fatalities = table_fields[3].text
        scraped_data = (date, location_operator, aircraft_type_and_registration, fatalities)
        crash_data.append(scraped_data)
    return crash_data


def format_date(date):
    d = datetime.strptime(date, '%d %b %Y')
    return (d.strftime('%d-%m-%Y'))


def format_aircraft_brand(aircraft_type_and_registration):
    a = aircraft_type_and_registration.split(" ")
    aircraft_brand = a[0]
    return aircraft_brand


def format_number_of_deaths(fatalities):
    f = fatalities.split("/")
    number_of_deaths = f[0]
    return int(number_of_deaths)


def create_headers_in_csv_file():
    if not path.isfile("crash_data.csv"):
        with open("crash_data.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "location", "aircraft_brand", "no_deaths"])
        return "File Created!"
    return "File exists"

def write_data_to_csv(crash_data):
    with open("crash_data.csv", "a") as file:
        writer = csv.writer(file)
        for _ in crash_data:
            d, loc, type, deaths = _
            date = format_date(d)
            location = loc
            brand = format_aircraft_brand(type)
            no_deaths = format_number_of_deaths(deaths)
            writer.writerow([date, location, brand, no_deaths])


links_2010_2021 = create_link_queue(2010, 2021)
create_headers_in_csv_file()
for year_link in links_2010_2021:
    crash_data = scrape_data_from_page(year_link)
    write_data_to_csv(crash_data)
