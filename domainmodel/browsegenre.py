from domainmodel.movie import Movie
from domainmodel.genre import Genre
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader

class BrowseGenre:

    def __init__(self, genre: Genre):
        self.__catalogue = []
        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            self.__genre = Genre("")
        the_test = MovieFileCSVReader("../datafiles/Data1000Movies.csv")
        the_test.read_csv_file()
        self.__avaliable_genres = the_test.dataset_of_genres
        self.__avaliable_movies = the_test.dataset_of_movies
        self.__top_x = []

    @property
    def avaliable_genres(self):
        return self.__avaliable_genres

    @property
    def avaliable_movies(self):
        return self.__avaliable_movies

    @property
    def genre(self):
        return self.__genre

    @property
    def catalogue(self):
        return self.__catalogue

    @property
    def top_x(self):
        return self.__top_x

    def browse_by_genre(self):
        self.catalogue = []
        for movie in self.avaliable_movies:
            for genre in movie.genres:
                if genre == self.genre:
                    self.catalogue.append(movie)
        return self.catalogue

    def browse_top_x(self, user_num: int):
        self.browse_by_genre()
        self.top_x = []
        if (len(self.catalogue) != 0) & isinstance(user_num, int):
            if user_num > len(self.catalogue):
                user_num = len(self.catalogue)
            result = sorted(self.catalogue, key=Movie.metascore.fget, reverse=True)
            for i in range(user_num):
                    self.top_x.append(result[i])
            return self.top_x
        return self.top_x

    @top_x.setter
    def top_x(self, value):
        self.__top_x = value

    @catalogue.setter
    def catalogue(self, value):
        self.__catalogue = value


class TestBrowseGenre:

    def test_browse_by_genre(self):
        x = Genre("horror")
        browse_x = BrowseGenre(x)
        browse_x.browse_by_genre()
        browse_x.browse_by_genre()
        print(browse_x.catalogue)
        testing = MovieFileCSVReader("../datafiles/Data1000Movies.csv")
        testing.read_csv_file()
        count = 0
        for movie in testing.dataset_of_movies:
            for genre in movie.genres:
                if genre == x:
                    count += 1
        assert len(browse_x.catalogue) == count
        y = Genre("")
        z = 123213213
        browse_y = BrowseGenre(y)
        browse_z = BrowseGenre(z)
        browse_y.browse_by_genre()
        browse_z.browse_by_genre()
        assert len(browse_y.catalogue) == 0
        assert len(browse_z.catalogue) == 0

    def test_browse_top_x(self):
        romance = Genre("romance")
        browse_romance = BrowseGenre(romance)
        complete_list = browse_romance.browse_top_x(5)
        count = 0
        assert complete_list[0].metascore > complete_list[1].metascore
        for movie in complete_list:
            if movie != complete_list[0]:
                assert movie.metascore <= complete_list[count - 1].metascore
            count += 1
        assert len(complete_list) == 5
        invalid_gen = Genre(1223)
        browse_invalid = BrowseGenre(invalid_gen)
        complete_invalid = browse_invalid.browse_top_x("24204")
        assert len(complete_invalid) == 0




















        



