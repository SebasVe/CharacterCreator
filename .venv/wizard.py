import character
#Extending from Character
class Wizard(character.Character):
# overriding the 3 abstract methods and returning them as values
    def description(self):
        return "Altar the Wizard"


    def magic_resistance(self):
        return 3


    def strength(self):
        return 1