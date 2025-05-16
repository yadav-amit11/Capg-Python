#take list of int from user and count how many digits end with 7 and 8. 
# take only one varibale to count both

nums = int(input("Enter number of items: "))
l = []
for i in range(nums):
    n = int(input("Enter number: "))
    l += [n]
count_7 = 0
count_8 = 0
for num in l:
    ld = abs(num) % 10  
    if ld == 7:
        count_7 += 1
    elif ld == 8:
        count_8 += 1

print("Count ending 7:", count_7)
print("Count ending 8:", count_8)




