# take integer input from user,and find sum of all even digits in the number and also for odd
# dont use typecasting and string methods
'''

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

'''

# count characters in string
'''
str1 = input("Enter string: ")
Lcount = 0
Ucount = 0
digit_count = 0
special_count = 0

for char in str1:
    ascii_val = ord(char)
    if 97 <= ascii_val <= 122:       
       Lcount += 1
    elif 65 <= ascii_val <= 90:      
        Ucount += 1
    elif 48 <= ascii_val <= 57:      
        digit_count += 1
    else:
        special_count += 1

print("Lowercase :",Lcount)
print("Uppercase :", Ucount)
print("Digits:", digit_count)
print("Special characters:", special_count)

'''

