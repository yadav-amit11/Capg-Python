# take integer input from user,and find sum of all even digits in the number and also for odd
# dont use typecasting and string methods

print("Enter a number:")
n = int(input())  
evenSum = 0
oddSum = 0

while n > 0:
    digit = n % 10  
    if digit % 2 == 0:
        evenSum += digit
    else:
        oddSum += digit
    n = n // 10
print("Sum of even digits:", evenSum)
print("Sum of odd digits:", oddSum)

