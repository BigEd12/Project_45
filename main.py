import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
films = soup.find_all(name="h3", class_="title")

reversed_film_list = []
for film in films:
    reversed_film_list.append(film.getText())

film_list = reversed_film_list[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for film in film_list:
        file.write(f"{film}\n")



