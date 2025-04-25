import character
#Extending from Character
class Bard(character.Character):
#overriding the 3 abstract methods and returning them as values
    def description(self):
        return "Barth the Bard"

    def magic_resistance(self):
        return 2

    def strength(self):
        return 2

