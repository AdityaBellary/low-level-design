from abc import ABCMeta, abstractmethod

class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass

class BE(AbstractDegree):
    def info(self):
        print("Bachelor of Engineering")
    
    def __str__(self) -> str:
        return "Bachelor of Engineering"

class ME(AbstractDegree):
    def info(self):
        print("Master of Engineering")
    
    def __str__(self) -> str:
        return "Master of Engineering"

class MBA(AbstractDegree):
    def info(self):
        print("Master of Business Administration")

    def __str__(self) -> str:
        return "Master of Business Administration"

class ProfileAbstractFactory(metaclass=ABCMeta):
    def __init__(self):
        self.__degrees = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):
        pass

    def addDegree(self, degree):
        self.__degrees.append(degree)
    
    def getDegrees(self):
        return self.__degrees
    
class ManagerFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(MBA())

class EngineerFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(ME())

class ProfileCreatorFactory(object):
    @classmethod
    def create_profile(self,name):
        return eval(profile_type + 'Factory')()

if __name__ == '__main__':
    profile_type = input("Which Profile would you like to create? Manager/Engineer - ")
    profile = ProfileCreatorFactory.create_profile(profile_type)
    print("Creating Profile of ", profile_type)
    print("Profile has following degrees -")
    for deg in profile.getDegrees():
        print('- ', deg)