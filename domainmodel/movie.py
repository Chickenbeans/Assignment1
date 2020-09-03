from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, movie_title: str , release_yr: int):
        if (movie_title == "" or type(movie_title) is not str) or (release_yr < 1900):
            self.__movie_title = None
            self.__release_yr = None
        else:
            self.__movie_title = movie_title.strip()
            self.__release_yr = release_yr

        self.__description = str
        self.__director = Director
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = int
        self.__meta_score = 0

    def __repr__(self):
        return f"<Movie {self.title}, {self.__release_yr}>"

    def __eq__(self, other_movie: "Movie"):
        if self.title != None:
            if (self.title == other_movie.title) & (self.__release_yr == other_movie.__release_yr):
                return True
            else:
                return False
        return False

    def __lt__(self, other_movie: "Movie"):
        if (self.title != None) & (other_movie.title != None):
            if self.title == other_movie.title:
                return self.__release_yr < other_movie.__release_yr
            else:
                return self.title < other_movie.title

    def __hash__(self):
        combined = self.title + str(self.__release_yr)
        return hash(combined)


    @property
    def title(self) -> str:
        return self.__movie_title

    @property
    def metascore(self) -> int:
        return self.__meta_score

    @metascore.setter
    def metascore(self, met):
        self.__meta_score = met

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def description(self) -> str:
        return self.__description

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def genres(self) -> list:
        return self.__genres

    @description.setter
    def description(self, the_description: str):
        if (the_description == "") or type(the_description) is not str:
            self.description = None
        else:
            self.__description = the_description.strip()

    @director.setter
    def director(self, add_director: Director):
        if add_director.director_full_name != None:
            self.__director = add_director
        else:
            pass

    @runtime_minutes.setter
    def runtime_minutes(self, rtm: int):
        if (rtm is None) or (rtm <= 0) or (type(rtm) == str ) :
            raise ValueError
        self.__runtime_minutes = rtm


    def add_actor(self, actor: Actor):
        if actor.actor_full_name != None:
            control = 0
            for act in self.__actors:
                if act.actor_full_name == actor.actor_full_name:
                    control += 1
                    break
            if control != 1:
                self.__actors += [actor]

    def remove_actor(self, actor: Actor):
        if actor.actor_full_name != None:
            for act in self.__actors:
                if act.actor_full_name == actor.actor_full_name:
                    self.__actors.remove(act)

    def add_genre(self, genre: Genre):
        if genre.genre_name != None:
            control = 0
            for gen in self.__genres:
                if gen.genre_name == genre.genre_name:
                    control += 1
                    break
            if control != 1:
                self.__genres += [genre]

    def remove_genre(self, genre: Genre):
        if genre.genre_name != None:
            for gen in self.__genres:
                if gen.genre_name == genre.genre_name:
                    self.__genres.remove(gen)


class TestMovieMethods:

    def test_init(self):
        Movie1 = Movie("Jungle awake", 1900)
        Movie2 = Movie("Harijuku coffee", 2006)
        Movie3 = Movie("", 1900)
        Movie4 = Movie("Valid movie", 1800)
        print(Movie1)
        print(Movie2)
        print(Movie3)
        print(Movie4)
        print()
        print()
        print()
        genre1 = Genre("horror")
        genre2 = Genre("more horror")
        genre3 = Genre("Ultimate horror")
        Movie1.add_genre(genre1)
        Movie1.add_genre(genre2)
        Movie1.add_genre(genre3)
        print(Movie1.genres)
        Movie1.remove_genre(genre3)
        print(Movie1.genres)




    #def test_eq(self):

    #def test_hash(self):






