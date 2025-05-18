def add2nums():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = int(num1) + int(num2)
    return num1,num2,result
    print(f"The sum of {num1} and {num2} is {result}")


res=add2nums()
print(res)