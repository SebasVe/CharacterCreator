import abc
import character
#abstracting and extending from Character
class Decorator(character.Character, abc.ABC):
    def __init__(self, c):
        self._ch = c

# overriding the 3 abstract methods to call each other on the character attribute
    def description(self):
        return self._ch.description()

    def magic_resistance(self):
        return self._ch.magic_resistance()

    def strength(self):
        return self._ch.strength()