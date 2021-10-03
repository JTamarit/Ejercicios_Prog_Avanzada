import requests
from time import sleep, time
from random import randint
import os
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, title, year, rating, votes):
        self.title = title
        self.year = year
        self.rating = rating
        self.votes = votes

start_elems = [str(i) for i in range(1,52,50)]
years = [str(i) for i in range(2019, 2021)]

n_requests = 0
start_time = time()
error_list = []

movie_list = []

for year in years:
    for start_elem in start_elems:
        URL = f'https://www.imdb.com/search/title?title_type=feature&release_date={year}&sort=num_votes,desc&start={start_elem}'
        page = requests.get(URL)

        sleep(randint(1, 2))

        n_requests += 1
        elapsed_time = time() - start_time
        os.system('cls')
        print(f"Request Number {n_requests}, Frequency {n_requests/elapsed_time}")

        if page.status_code != 200:
            error = f"Request Number {n_requests}, Status Code {page.status_code}"
            error_list.append(error)
            print(error)

        soup = BeautifulSoup(page.text, 'html.parser')

        main = soup.find(id='main')

        movie_containers = main.find_all('div', class_='lister-item mode-advanced')
        for movie in movie_containers:
            header = movie.find('h3', class_='lister-item-header')
            title_element = header.find('a')
            year_element = header.find('span', class_='lister-item-year text-muted unbold')
            rating_element = movie.find('div', class_='ratings-bar').find('strong')
            votes_element = movie.find('p', class_='sort-num_votes-visible').find('span', attrs={'name':'nv'})

            movie_list.append(Movie(title_element.text.strip(), year_element.text.strip(),
                f"{float(rating_element.text.strip())}", f"{int(votes_element['data-value'])}"))

print(movie_list)
print(error_list)