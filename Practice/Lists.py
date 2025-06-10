animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-2:-8])	#using negative indexes'  gives empty list
# print(animals[-5:-1])
# zoo=animals
# zoo[0]="hathi"
# print(zoo)
# print(animals)
# print(animals[102])

list=[1,2,3,4]
# print(list[::-1])
# list[1:4]=[200,300]
# print(list)

#duplicate in a list
# ls=[]
# items=int(input("enter no of list items : "))
# for i in range(items):
#     item=input("enter item : ")
#     ls.append(item)
# print(ls)
# for j in ls:
#     if ls.count(j)>1:
#         ls.remove(j)
# print(ls)

# def checkprime(n):
#     if n<=1:
#         print("not prime")
#         for i in range(2,n):
#             if n%i==0:
#              print("non prime")
#     else:
#         print("prime")
            
# checkprime(n=14)

ls=[]
items=int(input("enter no of list items : "))
for i in range(items):
    item=int(input("enter item : "))
    ls.append(item)
sum=0
for i in ls:
    sum+=i
print(sum)