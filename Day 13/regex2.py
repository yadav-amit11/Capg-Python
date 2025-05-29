s='''
Dates: 01/02/2025, 01-02-2024
Times : 9:00 AM,18:45,4:15PM
+91-9812313423
91-0987621323
919876543210
9876543210
abcd9899999
+1 1236 456 7890
+1 123-456-7890
'''
import re
# res=re.findall(r'\+91-[0-9]+',s)
# res = re.findall(r'\+?\d{1,3}[ -]?\d{3}[ -]?\d{3}[ -]?\d{4}+', s)

# \b -> word boundary
# res=re.findall(r'\+?\b\d{1,3}[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{1,4}\b',s)

# to check for indian and international numbers pattern
# res = re.findall(r'\+?\d{1,2}?[\s-]?\d{5}[\s-]?\d{5}|\+?\d{1,3}?[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{4}',s)

# date pattern matching
res= re.findall(r'\d{1,2}[/,-]\d{1,2}[/,-]\d{2,4}',s)
print(res)