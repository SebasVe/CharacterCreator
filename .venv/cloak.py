import decorator
#Extending from Decorator
class Cloak (decorator.Decorator):
#overriding the 3 abstract methods and calling each method with super
    def description(self):
        return super().description() + " + Protection Cloak"


    def magic_resistance(self):
        return super().magic_resistance() + 1


    def strength(self):
        return super().strength() + 1