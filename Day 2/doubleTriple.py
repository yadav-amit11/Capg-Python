num = int(input("Enter a number: "))
if (10 <= num <= 99) or (-99 <= num <= -10):
    print("Double digit")
elif (100 <= num <= 999) or (-999 <= num <= -100):
    print("Triple digit")
else:
    print("Others")
