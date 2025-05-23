# # # #dict:-

# # # '''

# # # d={K:V,K1:V1}

# # # '''
# # # d={}
# # # d1={1:100,2:200,3:300}
# # # # print(d1[100])
# # # d1[10]=1000
# # # d1[1]=101
# # # print(d1)


# # # d={1:10,2:10,3:10,1:20}
# # # print(d)

# # # d={1:10,1:10}
# # # print(d)
# # # d={1.5:10,10.5:10}
# # # print(d)
# # # d={"Ttt":10}
# # # print(d)
# # # d={True:1000}
# # # print(d)
# # # d={[10,20,30]:100}
# # # print(d)
# # # d={(1,2,3,4):100}
# # # print(d)
# # # d={{10,20,30}:1000}
# # # print(d)

# # d={1:100,2:1000,30:3}
# # print(d.items())
# # # for i,j in d.items():
# # #     print(i,j)

# # #keys()
# # print(d.keys())
# # print(d.values())

# # #get()
# # res=d.get(100,"Value not present")
# # print(res)
# # #pop()
# # res=d.pop(100,"key is not present")
# # print(res,d)
# # #popitem()
# # res=d.popitem()
# # print(res,d)
# d={1:100,2:1000,30:3}
# d.update({1:1000,200:90})
# print(d)
# #setdefault()
# res=d.setdefault(1,800)
# print(d,res)
# #fromkeys
# # d={}
# # l=[1,2,3,4]
# # res=d.fromkeys(l,"Selected")
# # print(res,d)

s='sdfghjk'
s='dgfh"fg' #possible
# s='ghjk'dfc' #not possible
# s="fghj"hgj" #not possible

'''

'''

d={"Aaa":80,"Bbb":70,"Ccc":67,"Ddd":65,"Eee":99}
res={}
while d:
    min_val = list(d.values())[0]
    min_key = list(d.keys())[0]
    for i in d:
        if d[i]<min_val:
            min_val=d[i]
            min_key = i
    res[min_key]=min_val
    del d[min_key]
print(res)
