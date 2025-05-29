
"""
#search,findall
search
syntax:
import re
re.search(pattern,str)
"""

# s='abc student@cgmail.com or abc support@capgemini.com  for queries'
# pattern="com"
import re
# # res=re.search(pattern,s)
# res=re.findall(pattern,s)
# if res:
#     print(f"{pattern} is present")
# else:
#      print(f"{pattern} is not present")
# print(res)


#\d->  to search for number's index using search() and findall for all no.
import re
s='''abc 4 23 trainer123@cgmail.com or abc 
support123@capgemini.com for queries
trainer_123@gmail.com
Trainer_123@cgmail.com

o/p
trainer123cgmail,
support123@capgemini,
trainer_123@cgmail,
Trainer_123.abc@cgamil
'''

# res=re.search(r'\d',s) #returns index where no. starts
# res=re.search(r'\D',s) # returns starting of non digit
# res=re.findall(r'\d',s)  # returns all digits
# res=re.findall(r'\s',s) # search for all blank space
# res=re.search(r'\S',s)  #<re.Match object; span=(0, 1), match='a'>
# res2=re.findall(r'\S',s) # all chars w/o space
# res=re.findall(r'\w',s)  # ignores all speacial chars except underscore
# res=re.search(r'\W',s)  # returns first special char
# res=re.search(r'\w',s) # returns first alphanumeric char
# res=re.findall(r'\W',s) # returns all special chars as list
# res=re.findall(r'\d+',s) # returns all digits as list
# res=re.search(r'\d+',s) # returns first digit
# res=re.findall(r'\d*',s) # returns all digits as list including empty string
# res=re.search(r'\d*',s) # returns first digit including empty string
# res=re.findall('[abc]',s) # returns all a,b,c as list
# res=re.findall('[a-z]',s) # returns all small letters as list
# res=re.findall('[A-Z]',s) # returns all capital letters as list
# res=re.findall('[0-9]',s) # returns all digits as list

s='''abc 4 23 trainer123@cgmail.com or abc 
support123@capgemini.com for queries
trainer_123@gmail.in
Trainer_123@cgmail.org
'''

'''
o/p
trainer123cgmail,
support123@capgemini,
trainer_123@cgmail,
Trainer_123.abc@cgamil
'''
# res = re.findall(r'[\w.]+@+\w+', s)

res2=re.findall('[A-Za-z0-9._]+@[a-z.]+.(?:com|in|org)',s)
print(res2)
# print(res2)