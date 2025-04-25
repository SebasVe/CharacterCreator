import decorator
#Extending from Decorator
class Ring(decorator.Decorator):
#overriding the 3 abstract methods and calling each method with super
    def description(self):
        return super().description() + " + Ring"

    def magic_resistance(self):
        return super().magic_resistance() + 2

    def strength(self):
        return super().strength() + 0
