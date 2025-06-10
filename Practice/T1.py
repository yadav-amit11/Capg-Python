#slicing
str1="AmitYadav"
# print(str1[:]) #full string
# print(str1[0:4]) #Amit
# print(str1[2:]) #itYadav
# print(str1[2:5]) #itY
# print(str1[2:5:2]) #iY it skip 2 
# print(str1[::-1]) #reverse string
# print(str1[::2]) #AiYdv
# print(str1[0:-3]) #AmitYa (negative index)
# print(str1[0:-3:2]) #Ay (negative index with step)     
# str2="welcome to the world of python programming"
# print(str2.endswith("to",2,6)) #True
# print(str2[-4:-2]) #ar
# print(str2.rstrip("!")) #!!!!Harry
# print(str2.lstrip("!")) #Harry!!!!
# print(str2.strip("!")) #Harry
# print(str2.replace("!","")) #Harry 
# def calc():
#     a=int(input("enter num1 :"))
#     b=int(input("enter num2 :"))
#     print(f"sum of {a}+{b}={a+b}")
#     print(f"prod of {a}*{b}={a*b}")
# calc()

# a=True
# b="4"
# print(int(a)+int(b))

# implementing a do while loop in python
# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if  number < 0:
#     break

# for i in range(12): 
#     "abc"
#     if (i==10):
#         break
#     print("5 x ",(i+1),'=',(5*(i+1)))

# Use positional first, then keyword

#count digits in a number
"""def countDigits(n):
    cnt=0
    while n > 0:
        cnt+=1
        n//=10
    print(cnt)
countDigits(12333)"""
word2="amit is ma a  ff  "
word2=word2.strip()
print(word2)

""" reverse a number
def reversenum(n):
    print(int(str(n)[::-1]))
reversenum(987654321)"""

"""class Solution(object):
    def reverse(self, x):
       
        sign=-1 if x<0 else 1
        rev_num=str(abs(x))[::-1]
        return sign*int(rev_num)
        """
        
# def multiplication_table(a):
#     for i in range(1,11):
#         print(f"{a}*{i}={a*i}")
# multiplication_table(5)