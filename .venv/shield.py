import decorator
#Extending from Decorator
class Shield(decorator.Decorator):
#overriding the 3 abstract methods and calling each method with super
    def description(self):
        return super().description() + " + Shield"


    def magic_resistance(self):
        return super().magic_resistance() + 0


    def strength(self):
        return super().strength() + 2