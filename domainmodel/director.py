

class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name #Returns full name as an attribute

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other_director: "Director"):
        return str(self.director_full_name) == str(other_director.director_full_name)

    def __lt__(self, other_director: "Director"):
        return str(self.director_full_name) < str(other_director.director_full_name)

    def __hash__(self):
        return hash(self.director_full_name)




class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test_eq(self):
        director1 = Director("Elliot Prosser")
        director2 = Director("")
        assert director1 != director2
        director3 = Director("")
        assert director1 != director3
        assert repr(director1) != repr(director3)

    def test_lt(self):
        director1 = Director("John James")
        director2 = Director("Jane James")
        assert director2 < director1
        director3 = Director("")
        director4 = Director("Jacob jose")
        assert director4 < director3

    def test_hash(self):
        director1 = Director("")
        director2 = Director("")
        assert director1 == director2
        print(hash(director1))
        print(hash(director2))





