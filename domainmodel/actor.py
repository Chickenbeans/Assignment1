
class Actor:

    def __init__(self, actor_name: str):
        if actor_name == "" or type(actor_name) is not str:
            self.__actor_name = None
        else:
            self.__actor_name = actor_name.strip()

        self.collegue_list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_name

    def add_actor_colleague(self, colleague: "Actor"):
        control = 0
        for actor in self.collegue_list:
            if str(self.actor_full_name) == str(actor.actor_full_name):
                control += 1
                break
        if (control == 0):
            if type(colleague.actor_full_name) == str:
                self.collegue_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague: "Actor"):
        for actor in self.collegue_list:
            if str(actor.actor_full_name) == str(colleague.actor_full_name):
                return True
        return False

    def __repr__(self):
        return f"<Actor {self.actor_full_name}>"

    def __eq__(self, other_actor: "Actor"):
        if isinstance(self.actor_full_name, str) & isinstance(other_actor.actor_full_name, str):
            return self.actor_full_name == other_actor.actor_full_name
        else:
            return False

    def __lt__(self, other_actor: "Actor"):
        return str(self.actor_full_name) < str(other_actor.actor_full_name)

    def __hash__(self):
        return hash(self.actor_full_name)


class TestGenreMethods:

    def test_init(self):
        actor1 = Actor("  Chris Pratt")
        actor2 = Actor("Vin Diesel")
        actor3 = Actor("Matt Damon")
        actor4 = Actor("Tian Jing")
        actor5 = Actor("")
        actor6 = Actor(69)
        assert actor1.actor_full_name == "Chris Pratt"
        assert actor5.actor_full_name is None
        assert actor6.actor_full_name is None

    def test_add_actor_colleague(self):
        actor1= Actor("Chris Pratt")
        actor2= Actor("Vin Diesel")
        actor3 = Actor("")
        actor4 = Actor("")
        actor1.add_actor_colleague(actor2)
        actor1.add_actor_colleague(actor4)
        actor1.add_actor_colleague(actor4)
        print()
        print(actor1.collegue_list)
        print(actor3.check_if_this_actor_worked_with(actor4))


    #def test_eq(self):


    #def test_lt(self):

    #def test_hash(self):





