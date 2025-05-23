# # # #oops:- 

# # # # print(type([10,3]))

# # # #class(blueprint):-
# # # # attributes/property
# # # # 1)states/Variables
# # # # class,instance variables
# # # # 2)methods
# # # # 1)classmethods
# # # # 2)instance methods
# # # #   1)normal instance method
# # # #   2) special/magic methods
# # # # 3)static method

# # # # Class creation:-
# # # # class KIIT:
# # # #     pass

# # # # obj=KIIT() #object creation
# # # # print(len(dir(obj)))

# # # #object creation with values:-
# # # # class new:
# # # #     var_c="New class"
# # # #     def __init__(self,a):
# # # #         self.a=a
# # # #         print(self.a)
# # # #     # print(a,self.a)# ❌ not possible
# # # # obj = new(10)
# # # # obj1=new(11)
# # # # print(obj.a)
# # # # # print(obj1.a)
# # # # # print(obj1.var_c)
# # # # class Aa:
# # # #     print("inside")

# # # # class stud_detail:
# # # #     name="Student details"
# # # #     def __init__(self,name,regno):
# # # #         self.name=name
# # # #         self.regno=regno
# # # #     def get_details(self):
# # # #         print(f"name : {self.name}\nReg no :{self.regno}")
# # # #     def update(self,name):
# # # #         self.name=name
# # # # obj=stud_detail("Jarvis",111222)
# # # # print(stud_detail.name)
# # # # print(obj.name)
# # # # obj.get_details()
# # # # obj.update("AAAAA")
# # # # obj.get_details()
# # # # obj1=stud_detail("Vipul",333555)
# # # # obj1.get_details()


# # # #encapsulation:-

# # # #public

# # # #protected (_)
# # # #private(__)
# # # class example:
# # #     def __init__(self):
# # #         self.a="I am public"
# # #         self._b="Protected"
# # #         self.__c="private"
# # #     def display(self):
# # #         print(self.a,self._b,self.__c)
# # #     def public(self):
# # #         print("public !!!!")
# # #     def _protected(self):
# # #         print("Protected!!!!")
# # #     def __private(self):
# # #         print("private!!!")
# # # obj=example()
# # # # print(obj.a)
# # # # print(obj._b)
# # # # print(obj._example__c)
# # # # obj._protected()
# # # # obj._example__private()
# # # # obj.__private()

# # #inheritance:-
# # #single-level inheritance
# # # class DramaTeacher:
# # #     def teach_acting(self):
# # #         print("Teacher: Project your voice and feel the emotion!")
# # #         self.perform()
# # # class Student(DramaTeacher):
# # #     # def teach_acting(self):
# # #     #     print("Teacher: Project your voice and feel the emotion!")
# # #     def perform(self):
# # #         print("Student: I will now perform on stage.")
# # #         # super().teach_acting()
# # #         # DramaTeacher.teach_acting(self)
# # # s = Student()
# # # # s.teach_acting()
# # # s.teach_acting()

# # # #multi level:-
# # # class Senior:
# # #     def teach_dance(self):
# # #         print("Senior: Here's how to do classical dance.")
# # # class Junior(Senior):
# # #     def teach_stage_entry(self):
# # #         print("Junior: Enter stage with confidence!")
# # # class Fresher(Junior):
# # #     def perform_scene(self):
# # #         print("Fresher: I'm ready to perform with all your teachings!")
# # #         super().teach_stage_entry()
# # # f = Fresher()
# # # # f.teach_dance()
# # # # f.teach_stage_entry()
# # # f.perform_scene()

# # # #multiple:-
# # # class MusicTeacher:
# # #     def teach_music(self):
# # #         print("Music Teacher: Practice your notes daily.")
# # # class ActingCoach:
# # #     def teach_acting(self):
# # #         print("Acting Coach: Let emotions flow!")
# # # class Performer(MusicTeacher, ActingCoach):
# # #     def final_show(self):
# # #         print("Performer: I'll sing and act!")
# # # p = Performer()
# # # p.teach_music()
# # # p.teach_acting()
# # # p.final_show()

# # # #Hierarchical 
# # class DramaTeacher:
# #     def teach(self):
# #         print("Drama Teacher: Everyone, warm up!")
# # class Actor(DramaTeacher):
# #     def act(self):
# #         print("Actor: Acting scene!")
# # class Director(DramaTeacher):
# #     def direct(self):
# #         print("Director: Action!")
# # a = Actor()
# # # d = Director()
# # # a.teach()
# # # a.act()
# # # d.teach()
# # # d.direct()

# # # class VoiceTrainer:
# # #     def train_voice(self):
# # #         print("Voice Trainer: Do your vocal exercises!")

# # # class Dancer:
# # #     def teach_dance(self):
# # #         print("Dancer: Practice your steps!")

# # # class Performer(VoiceTrainer):
# # #     def perform(self):
# # #         print("Performer: Singing and dancing!")

# # # class Star(Dancer, Performer):
# # #     def star_moment(self):
# # #         print("Star: Time to shine on stage!")

# # # s = Star()
# # # s.train_voice()
# # # s.teach_dance()
# # # s.perform()
# # # s.star_moment()

# #polymorphism:-
# # operator overloading:-
# #method overloading:-
# # a=10
# # a=50
# # def fun(a,b):
# #     return a*b
# #     print("hhh")
# def fun(a,b):
#     print(a*b)
# # fun(10,20)
# def fun(**arg):
#     print(arg)

# fun(a=10,b=10)
# #method overiding:-

# class parent:
#     def one(self):
#         print("hhh")
# class child(parent):
#     def one(self):
#         print("ggg")
# obj=child()
# obj.one()
