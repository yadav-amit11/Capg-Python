# # properties of list
# list=[1,2,3,4]
# #print(list[8]) # IndexError: list index out of range
# #list[-1]=100  # update
# #print(list[::-1])
# list[100:200]=[200,300]
# # del list  #name error, deletes the list
# print(list)
# print(list[::-1])
# print(list[:-100:-1])

# l=[1,2,3,4,7]
# # del l[-1:-3] check
# print(l)

# l=[1,2,3,4,5,6]
# print(len(l))
# for i in l:
#     print(i,end=" ")

# for i in range(len(l)):
#     print(l[i])
# l=[]
# items=int(input("enter no. of items"))
# for i in range(items):
#     item=(input("enter item"))
#     l+=[item]
# for i in l:
#     if l.count(i)>1:
#         l.remove(i)
# print(l)

l = []
result = []
nums = int(input("Enter no. of items: "))
for i in range(nums):
    item = input("Enter item: ")
    l += [item]
for i in l:
    # exists = False
    # for x in result:
    #     if x == item:
    #         exists = True
    #         break
    # if not exists:
    #     result += [item]
    if i not in result:
        result+=[i]
print(result)

