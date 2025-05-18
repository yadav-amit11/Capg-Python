my_list = [10, 20, 30, 40, 50]
# my_list[1] = 25                # Changes index 1 20 to 25 ; gives index error if index is not present
#my_list.append(60)          # Adds at the end TypeError: list.append() takes exactly one argument (2 given)
# my_list.insert(2, 99)       # Inserts 99 at index 2
# my_list.extend([70, 80])    # Adds multiple elements
# print(my_list)


# my_list.remove(20)    # Removes first occurrence of 25
# res=my_list.pop()         # Removes and returns last element
# res=my_list.pop(1)        # Removes and returns element at index 0
# del my_list[1:3]        # Deletes element at index ,at slices

# res=my_list.clear()       # Empties the entire list
# print(my_list,res)       # Prints the list

#-------------------------------------------
'''
nums=[1,2,3,2,4,5]
res=[]
for i in range(len(nums)):
    if i not in res:
        nums.append(i)
print(res)
'''

# merge two list and sort them
# nums=[1,2,1]
# nums2=[4,5,6,0]
# nums+=nums2
# res=[]
# # to merge uniquely
# for i in nums:
#     if i not in res:
#         res.append(i)
# res.sort()
# print(res)


