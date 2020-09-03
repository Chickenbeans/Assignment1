from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = movie
        self.__review_text = review_text
        if (rating > 0) & (rating <= 10) & isinstance(rating, int):
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.today()

    def __repr__(self):
        return f"<Review {self.movie}:, {self.review_text}, *{self.rating}>"

    def __eq__(self, other):
        if (self.movie == other.movie) & (self.review_text == other.review_text) & (self.rating == other.rating) & (
                self.timestamp == other.timestamp):
            return True
        else:
            return False

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

