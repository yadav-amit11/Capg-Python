#filehandling(r,r+,w,w+,a,a+)
"""
syntax :
with open('filename.txt','r,r+,w,w+,a,a+') as f
    #file operations like(read(),readline(),readlines() | write(),writelines())
r,r+

"""
with open('dummy.txt','r') as f:
    res = f.read()
    
    print(res)      # prints the file content
