# # Write a Python code to check if a number is even or odd
# def check(n):
#     if (n%2==0):
#         print("even")
#     else:
#         print("odd")
    
# check(12)
#  Write a Python program to count the number of vowels in a string

# def cntvow(str1):
#     vowels='aeiouAEIOU'
#     cnt=0
#     for ch in str1:
#         if ch in vowels:
#             cnt+=1
#     print(cnt)
# cntvow("amita")

# def cntvow(str1):
#     vowels='aeiouAEIOU'
#     res=set()
#     for ch in str1:
#         if ch in vowels:
#             res.add(ch.lower())
#     print(len(res))
# cntvow("amitaEe")

#  Write a Python program to find the longest word in a sentence

# def findlen(str1):
#     words=str1.split()
#     print(words)
#     print(max(words,key=len))
# findlen("amist is here  ")

# def findlen(str1):
#     words=str1.split()
#     longest=""
#     for ch in words:
#         if len(ch)>len(longest):
#             longest=ch
#     print(longest)
# findlen("ami mtbr asd d   ")

# Reverse a String Without Using Built-in Functions

a="amit"
# res=a[::-1]
# res="".join(reversed(a))
# print(res)

# Sum of Digits in a Number

# extraction of digits
# def findsum(a):
#     total=0
#     while a>0:
#      ld=a%10
#      total+=ld
#      a//=10
     
#     return total
# print(findsum(123))

# check for prime no.
# def chkprime(num):
#     if num<=1:
#         return False
#     for i in range(2,num):
#         if num%2==0:
#             return False
#         else:
#             return True
# print(chkprime(13))

# character freq dict
# def chkfreq(str1):
#     dt={}
#     for ch in str1:
#         if ch in dt:
#             dt[ch]+=1
#         else:
#             dt[ch]=1
#     return dt
# print(chkfreq("amitazgmmi"))


# def fibo(n):
#     "nth fibo number "
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(24))

# fibo series upto n
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
# n = int(input())
# for i in range(n + 1):
#     print(fibo(i), end=" ")

# Swap Two Numbers Without Using a Third Variable
# def swapp(num1,num2):
#     num1=num1+num2
#     num2=num1-num2
#     num1=num1-num2
#     return num1,num2
# print(swapp(10,20))
    
# Find the GCD of Two Numbers
# def findGCD(a,b):
#     while a>0 and b>0:
#         if a>b:
#             a=a%b
#         else:
#             b=b%a
#     if a==0:
#         return b
#     else:
#         return a
# print(findGCD(12,6))
# Check if Two Strings are Anagrams

# def anagrams(str1,str2):
#     return sorted(str1)==sorted(str2)
# print(anagrams("amit","ishika"))

# HAPPY NUMBER
# def happynum(num):
#     while True:
#         if num==1:
#             return True
#         if num==4:
#             return False
#         num=str(num)
#         sum=0
#         for i in num:
#             sum+=int(i)**2
#         num=sum           
# n=int(input())
# print(happynum(n))

#ARMSTRONG NUMBER
# def armstrong(a):
#     return sum(int(i)**len(str(a)) for i in str(a))==a
# print(armstrong(120))

#Python program to interchange first and last elements in a list
# def interchange(list):
#    list[-1],list[0]=list[0],list[-1]
#    return list
# print(interchange([1,2,3,4]))