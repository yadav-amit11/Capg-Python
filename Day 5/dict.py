# n = int(input("enter no. of values "))
# d = {}
# for i in range(n):
#     key = eval(input(f"enter key{i}"))
#     value = eval(input("enter value"))
#     d[key] = value
# print(d)
'''

d={1:20,2:30,1:2}
d1={1:10,1:10}
print(d)
print(d1)
d3={1:1.3,2:40.5}
print(d3)
#d4={[10,20,30]:100}
#print(d4)  Type error
d5={(1,2,3,4):100,23:3}
print(d5)
d6={1.4:{1,23}}
print(d6)


d={1:20,2:30,12:2,0:3}
# for i in d.items():
#         print(i)
# for i in d:
#     print(i,d[i])

# keys
print(d.keys()) # return type dict keys
print(d.values()) # return type dict values

#get()
res1=d.get(2)
res=d.get(100,"value not present")
#res3=d.pop(key,"default message")
print(res1)


#popitem
d={1:20,2:30,12:2,0:3}
d.update({1:40,10:2})
#res=d.popitem()  #Removes and returns the last inserted key-value pair as a tuple.
print(d) 
'''
#take a dict from user .create 5 pairs of names and marks, 
# and find highest marks and name;based on score, arrange the key and value in ascending order
# take one name from user side , check the if name is present and if not present, add it to dictionary
# remove least score from dictionary.


#Strings
'''
s="rwttw"'sd'
s1="sdsds"ddsd" #error
s='asasass'"ddq"
s3='asda'ff'
s4="wrwd3f"
'''

# str1=input("enter string: ")
# result = ""
# for char in str1:
#     if char not in result:
#         result += char
# print(result)
d={1:2,4:"hi"}
res=d.pop(3)
print(res,d)

