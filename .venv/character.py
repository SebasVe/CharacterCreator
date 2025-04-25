import abc

class Character(abc.ABC):
    #abstract the character name and items
    @abc.abstractmethod
    def description(self):
        pass

    #This is the characters magic resist value
    @abc.abstractmethod
    def magic_resistance(self):
        pass

    #This is the characters strength value
    @abc.abstractmethod
    def strength(self):
        pass
    #returns the string with the description,magic resistance, and strength
    def __str__(self):
        return f"Name: {self.description()}\nMR: {self.magic_resistance()} \nSTR: {self.strength()}"
