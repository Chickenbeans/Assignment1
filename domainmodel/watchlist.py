from domainmodel.movie import Movie

class WatchList:

    def __init__(self):
        self.__user_watch_list = []

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__user_watch_list):
            self.n += 1
            return self.watch_list[self.n - 1]
        else:
            raise StopIteration


    @property
    def watch_list(self):
        return self.__user_watch_list

    def add_movie(self, movie: Movie):
        if movie.title != None:
            if movie not in self.watch_list:
                self.watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        if isinstance(movie, Movie) == True:
            if movie.title != None:
                if movie in self.watch_list:
                    self.watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if index > len(self.watch_list) or index < -len(self.watch_list):
            return None
        else:
            return self.watch_list[index]

    def size(self):
        return len(self.watch_list)

    def first_movie_in_watchlist(self):
        if len(self.watch_list) == 0:
            return None
        else:
            return self.watch_list[0]







