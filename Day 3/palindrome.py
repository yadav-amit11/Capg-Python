print("Enter a number:")
num = int(input())
original = str(num)
reverse=original[::-1]
if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


