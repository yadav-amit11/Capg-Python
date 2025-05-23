# encapsulation

# public 
#private (__)
#protected  (_)

class example:
    def __init__(self):
        self.a="public"
        self._b="protected"
        self.__c="private"
    def display(self):
        print(self.a,self._b,self.__c)
    def publicM(self):
        print("public method")
    def _protected(self):
        print("protected method")
    def __private(self):
        print("private method")
obj=example()
# obj.a="new publ val"
# obj._b="new prtcd val"
# obj._example__c="new pvt val"
# print(obj.a)
# print(obj._b) 
#print(obj.__c)  # AttributeError: 'example' object has no attribute '__c'
#print(obj._example__c)  # Accessing private variable 
obj.publicM()
obj._example__private()
obj._protected()
