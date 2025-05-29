#abstraction:-
from abc import ABC,abstractmethod
class juicemaker(ABC):
    @abstractmethod
    def makejuice(self):
        pass
class orangejuice(juicemaker):
    def makejuice1(self):
        print("orange juice processing....")
class mangojuice(juicemaker):
    def makejuice(self):
        print("mango juice processing....")
obj=orangejuice()
obj.makejuice1()