 # control statements
 # if, else, elif

# num=int(input("enter num:"))
# if num>9 and num<100:
#     print("csk")
# else:
#     print("rcb")

# q1 double triple
#q2 div by 4,5,7
num = int(input("Enter a number: "))

if num % 4 == 0:
    if num % 5 == 0:
        print("Divisible by both 4 and 5")
    else:
        print("Divisible by 4")
else:
    if num % 5 == 0:
        print("Divisible by 5")

if num % 7 == 0:
    print("Divisible by 7")
else:
    if num % 4 != 0 and num % 5 != 0:
        print("Not divisible by 4, 5, or 7")
        


