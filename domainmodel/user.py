from domainmodel.movie import Movie
from domainmodel.review import Review

class User:

    def __init__(self, user_name: str, password: str):
        if user_name == "" or (isinstance(user_name, str) == False):
            self.__user_name = None
            self.__password = None
        else:
            self.__user_name = user_name.lower()
        self.__password = str(password)
        self.__watched_movies = []
        self.__what_hes_watching = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other_user: "User"):
        if self.user_name == other_user.user_name:
            return True
        else:
            return False

    def __lt__(self, other_user: "User"):
        if self.user_name != None and other_user.user_name != None:
            if self.user_name < other_user.user_name:
                return True
            else:
                return False
        else:
            return False


    def __hash__(self):
        return hash(str(self.user_name) + str(self.password))

    @property
    def user_name(self):
        return self.__user_name

    @property
    def friend_watched(self):
        return self.__what_hes_watching

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie):
        if movie.title != None:
            self.watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += int(str(movie.runtime_minutes))

    def add_review(self, review: Review):
        if isinstance(review, Review):
            self.reviews.append(review)

    def what_hes_watching(self, user: "User"):
        if isinstance(user, User):
            self.friend_watched = []
            if len(user.watched_movies) > 0:
                for movie in user.watched_movies:
                    if movie in self.watched_movies:
                        pass
                    else:
                        self.friend_watched.append(movie)
                return self.friend_watched

    @friend_watched.setter
    def friend_watched(self, value):
        self.__what_hes_watching = value


class TestUserExtensions:

    def test_what_hes_watching(self):
        u1 = User("Elliot", "1234")
        u2 = User("Bob", "42069")
        m1 = Movie("I Love 235", 2020)
        m2 = Movie("Testing class testing 123", 1960)
        m1.runtime_minutes = 90
        m2.runtime_minutes = 90
        u1.watch_movie(m1)
        u1.watch_movie(m2)
        u2.what_hes_watching(u1)
        assert len(u1.watched_movies) == len(u2.friend_watched)








