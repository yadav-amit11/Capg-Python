# '''
# take one dict from user key - your friends name,value - marks/score
# 1)find maximum score pair without using max()
# 2)find minimum score pair without using min()
# 3) sort dict based on value(score) without using sorted() ---- ascending..
# 4)take name from user check the name is already present
# or not if not ask value from user add this pair(key,value) to dict
# 5)remove least score pair.
# '''
# # find max number in list without using max(),sort()
# '''
# i/p:- [10,1,2,100,1000]
# o/p:- 1000
# '''
# # find min number in list without using max(),sort()
# '''
# i/p:- [10,1,2,100,1000]
# o/p:- 1
# '''
# '''
# 1)sort by ascending:-

# d={'ironman':100,'captain':50,'spiderman':60,'black':80,'batman':100}
# res={}
# min_value= d.values()[0] =100
# min_key = d.keys()[0]- 'ironman'
# for i in d:
#     if d[i]<min_value:
#         min_value=d[i]
#         min_key=i

# res[min_key]=min_value
# del d[min_key]
# d={'ironman':100,'spiderman':60,'black':80,'batman':100}
# res={'captain':50}
# min_value= d.values()[0] =100
# min_key = d.keys()[0]- 'ironman'
# for i in d:
#     if d[i]<min_value:
#         min_value=d[i]
#         min_key=i
# min_value= 60
# min_key = spiderman
# res[min_key]=min_value
# del d[min_key]
# '''
# print(bool({}))
# print(bool({1:100}))
# d={'ironman':100,'captain':50,'spiderman':60,'black':80,'batman':100}
# res={}
# # print(list(d.values())[0])
# # d={'ironman':100,'spiderman':60,'black':80,'batman':100}

# # while d: #True #True
# #     min_val=list(d.values())[0] #100
# #     min_key=list(d.keys())[0] #ironman #captain
# #     for i in d:#i = ironman
# #         if d[i]<min_val:#d[ironman]= 100 >> 100<100 #d[captain]-> 50 <100
# #             min_val=d[i] #60
# #             min_key=i#spiderman
# #     res[min_key]=min_val
# #     del d[min_key]
# # # print(d,res)
# # print(list(res.items())[0])

# #string built-in methods:-

# #1) upper()
# s="Kiit iS a good college"
# print(s.upper())
# #2) lower()
# #3) islower()
# print(s.islower())
# #4) isupper()
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

# print(s.count('kKK'))
# # print(s.index('K'))
# # print(s.index('k'))
# print(s.find('Kii'))
# print(s.replace('ki','v'))
# s1=s.replace('i','t')
# print(s1,s)
# print("Suiiiii".lstrip('ui'))
# print("   Suiii   ".strip())
# a="##100##".strip("#")
# print(int(a))
# print("aaabb".removeprefix('a'))
# print("aaabb".strip('a'))

# #split(),join()
# s="Today is a good day"
# res= s.split('o')
# print(res)
# print(min(res))
# print(max(res))

# print('-'.join(res))
'''
i/p:-
s="Today is a good day"
o/p:-
yaddo og a siya doT
s="Hello! Python ai machine learning"
o/p: 
gninra elenih ca mianoht yP!olleH
'''
s="Today is a good day"
# print(''.join(s.split())[::-1])
