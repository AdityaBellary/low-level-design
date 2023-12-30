# A factory is used to create objects by hiding the logic of creating the objects.
# Abstract classes are classes that cannot be instantiated on their own and are meant to be subclassed by concrete classes.

from abc import ABCMeta,abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class HR(Person):
    def create(self,name):
        print(f"HR {name} is created")

class Engineer(Person):
    def create(self,name):
        print(f"Engineer {name} is created")

class PersonFactory(object):
    @classmethod
    def createPerson(cls, designation, name):
        eval(designation)().create(name)

designation = input("enter designation -->")
name = input("Enter Name -->")
PersonFactory.createPerson(designation, name)