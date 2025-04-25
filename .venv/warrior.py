import character
#Extending from Character
class Warrior(character.Character):
# overriding the 3 abstract methods and returning them as values
    def description(self):
        return "Harcor the Warrior"


    def magic_resistance(self):
        return 0


    def strength(self):
        return 4

