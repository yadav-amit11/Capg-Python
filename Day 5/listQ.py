#isdisjoint()
'''
s1={1,20,3,4,"hi"}
s2={10,20,30,1,"hi"}
s3={100,200,300,400}
res=s1.isdisjoint(s3)
res2=s1.isdisjoint(s2)
print(res)
print(res2)
s1.clear()
print(s1)
copys2=s2.copy()
print(copys2)
subsett=s1.issubset(s2)
print(subsett)
subset2=s1.issubset(s3)
print(subset2)

'''
'''
s1={1,2,3,4,"hi"}
s2={1,3,10,"hi"}
s3={100,200,300,400}
superset2=s1.issuperset(s2)
print(superset2)
'''

#difference
# s={10,"hi",20,30,40}
# s1={10,20,4,"bye"}
# diff=s.difference(s1)
# print(diff)
#diff=s1.difference_update(s)
#print(diff)
# diff2=s.symmetric_difference(s1)
# print(diff2)

#take list from user side and give item which has maximumm count, print that value and frequency
# take a set() from user side and print maximum integer  value

nums = int(input("enter no. of items: "))
l = []
for i in range(nums):
    item = input("enter list item: ")
    l.append(item)

max_item = None
max_count = 0
for item in l:
    count = l.count(item)
    if count > max_count:
        max_count = count
        max_item = item
print("Item with maximum count:", max_item)
print("Frequency:", max_count)
