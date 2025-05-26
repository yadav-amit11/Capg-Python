# # my_list = [10, 20, 30, 40, 50]
# # my_list[1] = 25                # Changes index 1 20 to 25 ; gives index error if index is not present
# #my_list.append(60)          # Adds at the end TypeError: list.append() takes exactly one argument (2 given)
# # my_list.insert(2, 99)       # Inserts 99 at index 2
# # my_list.extend([70, 80])    # Adds multiple elements
# # print(my_list)


# # my_list.remove(20)    # Removes first occurrence of 25
# # res=my_list.pop()         # Removes and returns last element
# # res=my_list.pop(1)        # Removes and returns element at index 0
# # del my_list[1:3]        # Deletes element at index ,at slices

# # res=my_list.clear()       # Empties the entire list
# # print(my_list,res)       # Prints the list

# #-------------------------------------------
# '''
# nums=[1,2,3,2,4,5]
# res=[]
# for i in range(len(nums)):
#     if i not in res:
#         nums.append(i)
# print(res)
# '''

# # merge two list and sort them
# # nums=[1,2,1]
# # nums2=[4,5,6,0]
# # nums+=nums2
# # res=[]
# # # to merge uniquely
# # for i in nums:
# #     if i not in res:
# #         res.append(i)
# # res.sort()
# # print(res)

# ## Code with harry

# #SETs
# # sets={}  ❌ not an empty set
# sets=set() #empty set
# print(type(sets))
# # notes
# The method related to sets are:-
# 1) union()---->creates a new set with the unique elements from both the sets
# 2)update()----->applied on a set itself and it also adds unique elements from the both the sets into one of the sets
# 3) intersection()----> creates a new set with the common elements from both the sets
# 4)intersection_update()------> applied on a set itself and it also contains the common elements from both the sets
# 5)symmetric_difference--------> creates a new set with the elements from the both the sets that are not common in between
# 6)symmetric_difference_update-------> applied on a set itself and it contains elements from the sets that are not common inj between
# 7)difference------> creates a new set with the elements from a single set that are not common 
# 8) difference_update-----> applied on a set itself and contains elements of a set that are not common

# 9)isdisjoint()---->checks if there are common elements between two sets
# 10)issuperset----> checks if a set is a superset of another set
# 11) issubset-----> checks is a set is subset of another set
# 12)add------> to add a element into a set
# 13) remove-------> to remove an elements from a set, but raises key error if the element is not present in the set
# 14) discard-----> to remove an element from a set, does not raises error if the lement is not present in the set
# 15) del------> not method, a keyword, to delete the complete set
# 16) clear-------> to clear all the elements of a set 
# 17) in keyword used to check if a element is present in the set or not
# 18) pop()-----> to remove a random element from the set and also we can get that 

# city1={"a","b","c","d","z"}
# city2={"c","b","a"}
# print(city1.issuperset(city2))
# print(city2.issubset(city1))

dict={"a":10,"b":20,"c":"amit"}
print(dict.values())
for i in dict:
    print(dict[i])




