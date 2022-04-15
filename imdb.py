import requests
import csv
from bs4 import BeautifulSoup
filmy_list = []
r = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(r.text, "html.parser")
filmy = soup.find_all("td", class_="titleColumn")
for film in filmy:
    name = film.find("a").text
    year = film.find("span").text
    year = int(year.strip("()"))
    director_and_actors_list = film.find("a").get("title").split(",")
    director, *actors = director_and_actors_list
    director = director[0:-6]
    result = [name, year, director, actors]
    filmy_list.append(result)

header = ["jméno", "rok vydání", "režisér", "hlavní herci"]
sorted_films = sorted(filmy_list, key=lambda x: x[1], reverse=True)
with open("imdb_top250.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(sorted_films)