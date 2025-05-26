#list comprehension
"""
syntax
ls=[value for_loop if_condt(optional)]

order of execution
1. for loop
2. if condt.
3. value

"""

# n=int(input("enter  no. of inputs "))
# ls=[]
# for i in range(n):
#     ls+=[int(input())]
# print(ls)

# ls=[int(input()) for i in range(5) if i%2==0]
# ls=[i for i in range(100) if i%2==0]
# ls=[i for i in "monday" if i in "aeiouAEIOU"]
# print(ls)

# tuple comprehension
# t=(i for i in "monday" if i in "aeiouAEIOU")
# print(t)
# o/p 
# <generator object <genexpr> at 0x00000199A634B510>  # lazy evaluation when using parentheses with a single expression, Python creates a generator, not a tuple.

# t=tuple(i for i in "monday" if i in "aeiouAEIOU")
# print(t)

#set comprehension
# st={i for i in "monday" if i in "aeiouAEIOU"}
# print(st)

# 
"""
dictionary comprehension

syntax :
d={key:value for_loop if_condt(optional)}

"""
# d={x:x+2 for x in range(8)}
# print(d)

#zip() method to extract both key and value. usually a lazy evaluation. ignores extra values/keys
# keys=[100,200,300]
# values=[101,901,301]
# print(zip(keys,values))   # lazy evaluation
# print(list(zip(keys,values))) displaya as a list
# print(dict(zip(keys,values)))
# for i,j in zip(keys,values):
#     print(i,j)

# names = ["Ajay", "Dhoni", "Sachin", "David","Chris"]
# first_letters = [ch[0] for ch in names]
# unique_letters = [ch for ch in first_letters if first_letters.count(ch) == 1]
# print("Unique first letters:", unique_letters)

#take list of age and print valid age using list comprehension 
# take list of names and find all first letter unique characters

age=[10,20,-30,50,100,200,99]
ls = [i for i in age if  i>=0  and i<100]
print("Valid ages:", ls)

word = ['dhoni', 'virat', 'rohitsharma']
word_lengths = {w: len(w) for w in word}
print(word_lengths)

players=[('dhoni',95),('virat',20),('gill',100)]
topPlayers={name: score for name, score in players if score > 45}
print(topPlayers)

names = ["Ajay", "Dhoni", "Sachin", "David","Chris"]
firstLetter=[ch[0] for ch in names]
uniqueNames=[i for i in firstLetter if firstLetter.count(i)==1]
print(uniqueNames)