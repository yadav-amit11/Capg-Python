# n=int(input("enter no. of words: "))
# inp=[]
# for i in range(n):
#     val=int(input("enter val: "))
#     inp.append(val, sep=" ")
# print(inp)

n=int(input("enter no. of words: "))
inp=list(map(int,input().split()))
inp2=list(set(inp))
print(inp2)
inp2.sort(reverse=True)
print(inp2[1])

n=int(input("enter no. of words: "))
inp=list(map(int,input().split()))
inp.sort(reverse=True)
for i in inp:
    if i<max(inp):
        print(i)
        break

# n=int(input("enter no. of words: "))
# inp=[]
# print(sorted(list(set(inp(map(int(input().split())))))),reverse=True[1])
