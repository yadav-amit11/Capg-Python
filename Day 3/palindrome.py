print("Enter a number:")
num = int(input())
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num= num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


