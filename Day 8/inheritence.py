#inheritance

class Dramateacher:
    def teach_act(self):
        print("teacher: project your drama")
    # def abc(self):
    #     print("testing123")

class Student(Dramateacher):
    def perform(self):
        print("student performs")
        self.teach_act()
        #self.perform() infinite error
       # super().teach_act()
       # Dramateacher.teach_act(self)
       # Dramateacher.abc(self)
      

s=Student()
#s.teach_act()
s.perform()