# Given the participants' score sheet for your University Sports Day, you are required to find the 
# runner-up score. You are given  scores. Store them in a list and find the score of the runner-up. 
# Input Format 
# # The first line contains . The second line contains an array   of  integers each separated by a space.
lsSize=int(input("enter no of items"))
ls=[]
for i in range(lsSize):
    score=int(input("enter item "))
    ls.append(score)
ls=list(set(ls))
ls.sort(reverse=True)
print(ls[1])

