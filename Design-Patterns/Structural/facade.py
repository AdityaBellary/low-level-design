#Provides a simplified interface to a complex subsystem, making it easier to use and understand.

class Cook:
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cut()

        self.boiler = Boiler()
        self.boiler.boil()

        self.frier = Frier()
        self.frier.fry()


class Cutter:
    def cut(self):
        print("Veggies are cut")

class Boiler:
    def boil(self):
        print("Veggies are boiled")

class Frier:
    def fry(self):
        print("Veggies are fried")

cook = Cook()
cook.prepareDish()