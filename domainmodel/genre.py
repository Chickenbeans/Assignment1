
class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip().capitalize()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.genre_name}>"

    def __eq__(self, other_genre: "Genre"):
        return self.genre_name == other_genre.genre_name

    def __lt__(self, other_genre: "Genre"):
        return str(self.genre_name) < str(other_genre.genre_name)

    def __hash__(self):
        return hash(self.genre_name)


class TestGenreMethods:

    def test_init(self):
        horror = Genre("horror")
        assert repr(horror) == "<Genre Horror>"
        empty_genre = Genre("")
        assert empty_genre.genre_name is None
        empty_genre2 = Genre(69)
        assert empty_genre2.genre_name is None

    def test_eq(self):
        g1 = Genre("Horror")
        g2 = Genre("Horror")
        assert g1 == g2
        g3 = Genre("")
        assert g1 != g3
        assert repr(g1) != repr(g3)

    def test_lt(self):
        g1 = Genre("Horror")
        g2 = Genre("Action")
        assert g2 < g1
        g3 = Genre("")
        assert g3 != g1

    def test_hash(self):
        g1 = Genre("")
        g2 = Genre("")
        assert g1 == g2
        print(hash(g1))
        print(hash(g2))
