#recursion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

#fibonacci series

# def fibo(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
# n = int(input())
# for i in range(n + 1):
#     print(fibo(i), end=" ")

#palindrome string

# def palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrome(s[1:-1])
# text = input()
# if palindrome(text):
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#anonymous function (lambda)
'''
syntax :
var=lambda args:expression
used for small tasks
'''
# var=lambda X:str(X)[::-1]
# print(var("fyuf"))
# var1=lambda s:s[1].isupper()
# print(var1("abc"))
# var2=lambda n:"even" if n%2==0 else "odd"
# print(var2(10))


#print max value from dict
# dict={'amit':10,'ak':20,'kyz':30}
# val=dict.items()
# val2=dict.keys()
# print()
# print(val)
# print(max(val,key=lambda x:x[1]))

# first 2 letters in caps,others in smallcase
# l = eval(input())
# f = lambda x: x[:2].upper() + x[2:].lower()
# print(list(map(f, l)))

# The filter() method in Python has the following syntax:

#     Syntax: filter(function, sequence)

#     function: A function that defines the condition to filter the elements. This function should return True for items you want to keep and False for those you want to exclude.
#     iterable: The iterable you want to filter (e.g., list, tuple, set).

#filter the integers
ls=[1,'hii',2.4,3,4,5,6]
f=lambda x:type(x)==int
print(list(filter(f,ls)))