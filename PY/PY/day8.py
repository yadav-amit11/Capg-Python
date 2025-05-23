# #recursion:-

# # def fact(n):
# #     if n==0 or n==1:
# #         return 1
# #     return n * fact(n-1)
# # print(fact(5))

# #anonymous fun(lambda):-
# '''
# syntax:-
# var = lambda args:expression
# '''
# var = lambda X:str(X)[::-1]
# print(var(10))
# # var1=lambda s:s[0].isupper()
# # print(var1("hellooo"))

# # var1=lambda s:s[0].upper()
# # print(var1("hellooo"))

# num=lambda n: "Even" if n%2==0 else "Odd"
# print(num(10))

# d={'ironman':100,'captain':50,'spiderman':60,'black':80,'batman':100}
# val = d.items()
# print(val)
# # print(sorted(val,key=lambda x:len(x[0])))


# l=[1,2,3,4]
# f= lambda x:x+2
# print(list(map(f,l)))
# l = eval(input())
# f = lambda x: x[:2].upper()+x[2:].lower()
# print(list(map(f,l)))
l=[1,2,3,4,5,7]
f=lambda x:not x%2
print(list(filter(f,l)))