from abc import ABCMeta,abstractmethod

class CarFactory(metaclass=ABCMeta):
    @abstractmethod
    def build_car(self):
        pass
    def build_parts(self):
        pass

class SedanCarFactory(CarFactory):
    def build_car(self):
        return SedanCarAssembleFactory()

    def build_parts(self):
        return SedanCarPartsFactory()

class SUVCarFactory(CarFactory):
    def build_car(self):
        return SUVCarAssembleFactory()

    def build_parts(self):
        return SUVCarPartsFactory()
    
class CarPartsFactory(metaclass=ABCMeta):
    @abstractmethod
    def build(self):
        pass

class SedanCarPartsFactory(CarPartsFactory):
    def build(self):
        print("Sedan Car parts are built")
    
    def __str__(self) -> str:
        return "<Sedan car parts are built>"

class SUVCarPartsFactory(CarPartsFactory):
    def build(self):
        print("SUV car parts are built")
    
    def __str__(self) -> str:
        return "<SUV car Parts are built>"
    
class CarAssembleFactory(metaclass=ABCMeta):
    @abstractmethod
    def assemble(self):
        pass
class SedanCarAssembleFactory(CarAssembleFactory):
    def assemble(self):
        print("Sedan Body is assembled")
    
    def __str__(self) -> str:
        return "Sedan is assembled"

class SUVCarAssembleFactory(CarAssembleFactory):
    def assemble(self):
        print("SUV Body is assembled")
    
    def __str__(self) -> str:
        return "SUV is assembled"
    
if __name__ == "__main__":
    for factory in (SedanCarFactory(), SUVCarFactory()):
        car_parts = factory.build_parts()
        car_parts.build()
        car_builder = factory.build_car()
        car_builder.assemble()