# # # # # #properties of list:-
# # # # # #1) both homogeneous and heterogeneous collection

# # # # # l=[10,67,46]
# # # # # l1=['hiii',0,'iih']
# # # # # print(l)
# # # # # print(l1)
# # # # # #it is an ordered collection
# # # # # l=[10,67,46]
# # # # # print(l)
# # # # # #it can support duplicate values/elements.
# # # # # # l=[10,67,46,10]
# # # # # print(l)
# # # # # #it supports indexing +ve,-ve
# # # # # l=[1,67,46,10]
# # # # # # print(l[-4])
# # # # # # l[-4]=100
# # # # # # print(l)
# # # # # #it support slicing
# # # # # # print(l[::-1])
# # # # # # l[1:100]=[200,300]
# # # # # # print(l[::-1])
# # # # # # print(l[:-10000:-1])
# # # # # #it is a mutable collection
# # # # # # l=[1,67,46,10]
# # # # # # del l[0:3]
# # # # # # print(l)

# # # # # #
# # # # # l=[1,67,46,10]
# # # # # print(len(l))
# # # # # # for i in l:
# # # # # #     print(i,end=" ")

# # # # # # for i in range(len(l)):
# # # # # #     print(l[i])
# # # # # l=["even","odd"]
# # # # # n=int(input("enter a number : ")) #13
# # # # # print(l[n%2]) #l[13%2]-->l[1]
# # # # # # l=[10,20,30]
# # # # # # print(l[1])

# # # # # l,n =[],int(input())
# # # # # for i in range(1,n+1):
# # # # #     if n%i==0:
# # # # #         l+=[i]
# # # # # if len(l)==2:
# # # # #     print("primeeee num")
# # # # # else:
# # # # #     print("not a primee num")

# # # # #built-in methods in list

# # # # #clear()

# # # # # l=[1,2,3,4,5]
# # # # # res = l.clear()
# # # # # print(res,l)
# # # # #copy()
# # # # # l=[1,2,3,4,5]
# # # # # copyofl=l.copy()
# # # # # print(copyofl)

# # # # # copyofl[0]=1000
# # # # # print(copyofl,l)
# # # # # l=[0,2,[100,200,400]]
# # # # # copyofl=l.copy()
# # # # # print(l[2][0])

# # # # #append()

# # # # # l=[1,2,3]
# # # # # res = l.append([45,56,78])
# # # # # print(l,res)
# # # # # #insert()
# # # # # l=[1,2,3]
# # # # # l.insert(1200,["hi",1,2,5])
# # # # # print(l)

# # # # #extend()

# # # # # l=[10,"hiii","CSKRCB"]
# # # # # s="IPL"

# # # # # l.extend(s)
# # # # # print(l)

# # # # #pop()
# # # # # l=[1,2,3,"aabb",10]
# # # # # res = l.pop(2)
# # # # # print(l,res)
# # # # #remove()
# # # # # l=[1,2,3,"aabb",10,1]
# # # # # l.remove(1,2)
# # # # # print(l)

# # # # #count()
# # # # # l=[1,2,3,"aabb",10,1]
# # # # # res=l.count(100)
# # # # # print(res)

# # # # #index()
# # # # # l=[1,2,3,"aabb",10,1]

# # # # # res=l.index(100,0,6)
# # # # # print(res)

# # # # #reverse()
# # # # # l=[1,2,3,"aabb",10,1]
# # # # # l.reverse()
# # # # # print(l)
# # # # #sort()
# # # # # l=[1,2,3.5,10,1]
# # # # # l1=[1,2,3,"aabb",10,1]
# # # # # l2=['Abb','Zzz','Cbb','Bbb']
# # # # # l.sort(reverse=True)
# # # # # # l1.sort()
# # # # # print(l)
# # # # # l2.sort()
# # # # # print(l2)

# # # # #tuple()
# # # # t=(10.5,)
# # # # t=1,2,3
# # # # print(t,type(t))

# # # # # t+=(1,4,5) #t=t+(1,4,5)
# # # # # t[0]=100
# # # # # print(t)
# # # # # s={1,1000,1,500,"hi",'1',1,True}
# # # # # # s1=
# # # # # print(s)
# # # # # s=set()
# # # # # print(type(s))

# # # # #built-in methods in set:-
# # # # #union()
# # # # s={1,1000,1,500,"hi",'1',1,"True",1.5}
# # # # s1={27,898,89,45,1}
# # # # # res=s.union(s1)
# # # # # print(res)
# # # # # #update()
# # # # # s.update(s1)
# # # # # print(s)
# # # # # res=s.intersection(s1)
# # # # # print(res)
# # # # # print(s)
# # # # # s.intersection_update(s1)
# # # # # print(s)
# # # # #pop/discard
# # # # res=s.pop()
# # # # print(res)
# # # # res=s.discard(100)
# # # # print(res,s)

# # # # #add()
# # # # s.add("abbbb")
# # # # s.add(11001)

# # # # print(s)
# # # # #isdisjoint()
# # # # s1={1,2,3,4,1,"hi"}
# # # # s2={10,20,30,40,1,"hi"}
# # # # s3 = {100,200,300,400,500}
# # # # res= s1.isdisjoint(s3)

# # # # print(res)
# # # # #clear()

# # # # #copy()

# # # # #issubset()
# # # # s={10,20,30,40}
# # # # s1={10,20}
# # # # s3={10,20,1}
# # # # res=s3.issubset(s)
# # # # print(res)
# # # # #issuperset()
# # # # res=s3.issuperset(s1)
# # # # print(res)

# # # # #difference()
# # # # s={10,20,30,40}
# # # # s3={10,20,1}
# # # # # res=s3.difference(s)
# # # # #difference_update()
# # # # #symmetric_difference
# # # # res=s.symmetric_difference(s3)
# # # # print(res)
# # # # print(s)
# # # # res=s.symmetric_difference_update(s3)
# # # # print(s,res)

# # # s={10,20,30,40}
# # # s.remove(10)
# # # # s.discard(100)
# # # print(s)
# # # l=[1,10,20,30,20,1]
# # # print(list(set(l)))
# # s={10,20,10,10,50}
# # for i in s:
# #     print(i,end=" ")
# # '''
# # 1)
# # i/p:  
# # l=[1,1,2,2,2,3,3]
# # o/p:
# # 2 3
# # 2)
# # s={1,2,3,1000,24,55,90,4}
# # o/p:-
# # 1000
# # '''
# # print()
# # l=[1,1,2,2,2,3,3]
# # res=[0,0]
# # copy = set(l)
# # print(res[1],l.count(1))
# # for i in copy:
# #     # print(type(res[1]),type(l.count(i)))
# #     if l.count(i)>res[1]:
# #         res[1]=l.count(i)
# #         res[0]=i
# # print(res)
# l=[1,1,2,2,2,3,3]
# copy=list(set(l))
# res=[]
# for i in copy:
#     res+=[l.count(i)]
# max_f = max(res)
# print(f"list values {copy} and freq : {res}")
# # print(max_f)

# s={1,2,3,1000,24,55,90,4}
# print(max(s))


