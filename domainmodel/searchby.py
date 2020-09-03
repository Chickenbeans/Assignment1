from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader

class SearchBy:

    def __init__(self, director: Director, actor: Actor = Actor("")):
        if isinstance(director, Director):
            self.__director = director
        else:
            self.__director = Director("")
        if isinstance(actor, Actor):
            self.__actor = actor
        else:
            self.__actor = Actor("")
        self.__movies_by_director = []
        self.__movies_by_actor = []
        csv_info = MovieFileCSVReader("../datafiles/Data1000Movies.csv")
        csv_info.read_csv_file()
        self.__all_movies = csv_info.dataset_of_movies


    def search_by(self):
        self.movies_by_director = []
        self.movies_by_actor = []
        for movie in self.all_movies:
            if movie.director == self.director:
                self.movies_by_director.append(movie)
            if isinstance(self.actor.actor_full_name, str):
                if self.actor.actor_full_name != None:
                    for act in movie.actors:
                        if self.actor == act:
                            self.movies_by_actor.append(movie)


    @property
    def movies_by_actor(self):
        return self.__movies_by_actor

    @property
    def all_movies(self):
        return self.__all_movies

    @property
    def movies_by_director(self):
        return self.__movies_by_director

    @property
    def director(self):
        return self.__director

    @property
    def actor(self):
        return self.__actor

    @movies_by_director.setter
    def movies_by_director(self, value):
        self.__movies_by_director = value

    @movies_by_actor.setter
    def movies_by_actor(self, value):
        self._movies_by_actor = value

    @director.setter
    def director(self, other_dic: Director):
        if isinstance(other_dic, Director) == True:
            self.__director = other_dic
            self.search_by()

    @actor.setter
    def actor(self, other_act: Actor):
        if isinstance(other_act, Actor):
            self.__actor = other_act
            self.search_by()

class TestSearchBy:

    def test_search_by(self):
        director1 = Director("Quentin Tarantino")
        director2 = Director("Martin Scorsese")
        actor1 = Actor("Tom Hanks")
        actor2 = Actor("Brad Pitt")
        inv_d = ""
        inv_a = 12324
        my_search = SearchBy(director1)
        my_search.search_by()
        for movie in my_search.movies_by_director:
            assert movie.director == director1
        second_search = SearchBy(director2, actor1)
        second_search.search_by()
        for movie in second_search.movies_by_actor:
            assert actor1 in movie.actors
        invalid_search = SearchBy(inv_d, inv_a)
        invalid_search.search_by()
        assert len(invalid_search.movies_by_actor) == 0
        assert len(invalid_search.movies_by_director) == 0




