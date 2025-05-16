nums = int(input("enter no. of elements "))
s1 = set()
for i in range(nums):
    item = int(input("enter integers: "))
    s1.add(item)
print(s1)
max_val = sum(s1)
print("max value:", max_val)


