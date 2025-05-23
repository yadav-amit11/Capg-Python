# # # a=int(input("enter first num"))
# # # b=int(input("enter 2nd num"))
# # # if(a>b):
# # #     print("a is greater")
# # # elif(b>a):
# # #     print("b is greater")
# # # else:
# # #     print("both are equal")

# # a=int(input("enter first num"))
# # b=int(input("enter 2nd num"))
# # c=int(input("enter 3rd num"))
# # if a>b and a>c:
# #     if b>c:
# #         print('b sec lar')
# #     else:
# #         print('c is sec lar')
# # elif b>a and b>c:
# #     if a>c:
# #         print('a is sec lar')
# #     else:
# #         print('c is sec lar')
# # else:
# #     if a>b:
# #         print('a is sec lar')
# #     else:
# #         print('b is sec lar')

# a = input("Enter char : ")
# vow = 'aeiou'
# a = a.lower()

# if a in vow:
#     ty = "Vowel"
# elif 'a' <= a <= 'z' and a not in vow:
#     ty = "Consonant"
# elif '0'<=a<='9':
#     ty = "Digit"
# else :
#     ty = "Special"

# print("Type = ",ty)

# option = int(input())
# match option:
#     case 1:
#         print("Hiii")
#     case 1:
#         print("Byee")
#     case 3:
#         print("HiiByee")
#     case _:
#         print("OOps!!!")


'''
for variablename in range(start_value,end_value+1,step_value):
    #statements
'''

# for s in range(100,200,10):
#     print("hiii")
# for s in range(10,101):
#     print(s,end=" ")
# for s in range(500,99):
#     print(s)

'''
syntax:-
for variablename in collectionname:
    #statements
'''
# for i in "Python is a good language"[::-1]:
#     print(i,end=" ")

#while loop:-

# if True:
#     pass
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i,end=" ")
# i=1
# while i<=10:
#     if i==5:
#         break
#     print(i) 
#     i+=1




#include
# l=[]
# l=eval(input())
# print(l)
l=[1,2,3]
l+=[7,8]
# del l[0:]
# print(l)
# print(l.__dir__(1))
# print(l)

# s={1,2,3,410,51}
# s1={20,30,40,50,60}

# print(s.add(10))
# print(s.isdisjoint(s1))

s={1:2,2:3,4:4}
