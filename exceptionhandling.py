#exception handling:-
'''
types of exception handling:-
1)default exception
2)custom exception(user defined)
'''
'''
syntax:-
try:
    #main logic(here we have to write main logic)
except:
    #If any error in try part this except will receive errors
else:
    #if there is no error in try then this block will execute
finally:
    #after try and except this block will execute.
'''
#
# try:
#     a = int(input())
#     if a<18:
#         raise ValueError("less than 18")
# except ZeroDivisionError as e:
#     print("Error: ",e)
# except ValueError as e:
#     print("Error1 :",e)
# else:
#     print(f'a = {a}')
# finally:
#     print("finally")

# class lessthan18(Exception):
#     pass
# try:
#     a = int(input())
#     if a<18:
#         raise ValueError("less than 18")
# except lessthan18 as e:
#     print("Error: ",e)
# except Exception as e:
#     print("Error : ",e)
    
# class error:
#     def __init__(self,error="invalid literal for int() with base 10: 'abc'"):
#         self.error = error
#         print(self.error)
# error("This is error")

#module and package:-
#module:-

# import random

# #random
# print(random.random())
# print(random.randint(1,100))
# print(random.choice(["Stone","paper","scissor"]))
# l=[1,2,4,900]
# random.shuffle(l)
# print(l)

class game:
    def start(self):
        print("Game starts")
