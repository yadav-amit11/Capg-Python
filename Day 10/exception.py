"""
EXCEPTION HANDLING
 Types of exception handling
 1. Default exception
 2.Custom Exception

Syntax:
try:
    #main logic(here we have to write main logic)
except:
    #if any error in try part this except will receive errors
else:
    #if there is no error in try then this block will execute
finally:
    #after try and except this block will execute,always executes.
"""


# try:
#     a=100/int(input())
#     print(f'a={a}')
# except Exception as e:
#     print("error : ",e)
# # except ValueError as e:
# #     print("error",e)
# finally:
#     print("finally block")

# try:
#     a=int(input())
#     # print(f'a={a}')
#     if a<18:
#         raise ZeroDivisionError("less than 18")
# except Exception as e:
#     print("error : ",e)
# except ValueError as e:
#     print("error",e)
# # else:
# #     print(f'a={a}')
# finally:
#     print("finally block")

# class lessthan18(Exception):
#     pass
# try:
#     a=int(input())
#     if a<18:
#         raise lessthan18("less than 18")
# except lessthan18 as e:
#     print("error ",e)
# except Exception as e:
#     print("error ",e)

class error:
    def __init__(self,error="invalid literal error"):
        self.error=error
        print(self.error)
error("neew ere")



















































