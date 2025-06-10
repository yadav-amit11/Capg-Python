#take a no. as input and store its factors in a list and then use len() to determine if its prime or not

# factors=[]
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if n % i == 0:
#         factors += [i]
# print("Factors:", factors)
# if len(factors) == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

# primes = []
# for num in range(100, 1001):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         primes += [num]
# print(primes)

#l = [[5,6],1, 2, 3]
# newl = l.copy()
# print(newl)
# newl[1:2] = 100, 200
# print(newl)
# print(l)

#shallow copy 

# original = [[1, 2], [3, 4]]
# shallow = original.copy()
# shallow[0][1] = 99
# print("Original:", original)
# print("Shallow:", shallow)
#l=[1,12,2,3]
#res=l.append([20,30])
#res2=l.insert(10,"100")
#print(l,res)
#print(l,res2)
#print(type(res2))
s=["app","moaee"]
#res=l.pop(2)
#res=l.remove(12)
#print(l)
#res=l.index(1,0,9)

size = int(input("Enter number of elements: "))
l = []

for i in range(size):
    val = input("Enter element: ")
    l += [val]
n = int(input("Enter no. right rotations: "))
for i in range(n):
    last = l[-1]        
    for i in range(size - 1, 0,-1):
        l[i] = l[i - 1]
    l[0] = last
print("Right rotated list:", l)

#left rotation
size = int(input("Enter number of elements: "))
l = []
for i in range(size):
    val = int(input("Enter element: "))
    l += [val]
n = int(input("Enter number of left rotations: "))
for _ in range(n):
    first = l[0]
    for i in range(0, size - 1):
        l[i] = l[i + 1]
    l[-1] = first
print("Left rotated list:", l)


