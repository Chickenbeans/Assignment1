import csv
from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                genres_list = row['Genre'].split(",")
                metascore = row['Metascore']
                our_movie = Movie(title, release_year)
                if metascore != "N/A":
                    our_movie.metascore = int(metascore)
                else:
                    our_movie.metascore = 0
                for gen in genres_list:
                    our_movie.genres.append(Genre(gen))
                index += 1
                self.dataset_of_movies.append(our_movie)
                my_actors = row['Actors'].split(",")
                my_director = row['Director']
                director_name = Director(str(my_director))
                our_movie.director = director_name

                for a in my_actors:
                    act = Actor(str(a))
                    if act not in self.dataset_of_actors:
                        self.dataset_of_actors.append(act)
                    our_movie.add_actor(act)

                if director_name not in self.dataset_of_directors:
                    self.dataset_of_directors.append(director_name)

                for gen in genres_list:
                    my_gen = Genre(str(gen))
                    if my_gen not in self.dataset_of_genres:
                        self.dataset_of_genres.append(my_gen)
