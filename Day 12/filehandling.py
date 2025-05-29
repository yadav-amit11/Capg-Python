#filehandling(r,r+,w,w+,a,a+)
"""
syntax :
with open('filename.txt','r,r+,w,w+,a,a+') as f
    #file operations like(read(),readline(),readlines() | write(),writelines())
r,r+

"""
# try:
#     with open('dummy.txt','r') as f:
#     #res = f.read() #returns string
#         if f.readable():
#             res=f.readlines() # from first to last line
# #             print(f.tell())
# #             print(f.seek(0))
# #             print(f.read())
    
# # except FileNotFoundError as e:
# #     print("error",e)
# # else:
# #     # print(res)
# #     pass
 

try:
    with open('dummy.txt','r') as fs:
        if fs.readable():
            res=fs.read()
            num_chars = len(res.replace('\n', '')) 
            print("no of chars w/o newline :", num_chars)
            print("no of char with newline",fs.tell())

            num_lines=len(res)
            print("no of lines ",num_lines)

            num_words=sum(len(i.split()) for i in res)  
            print("number of words",num_words)  
except FileNotFoundError as e:
    print("error",e)

# try:
#     with open('dummy.txt', 'r+') as f:
#         lines = f.readlines() 
#         for i in lines:
#             marks = i.split(',')
#             if int(marks[3]) < 50:
#                 print(i)
# except FileNotFoundError as e:
#     print("error",e)

n = int(input("enter n "))
with open('dummy.txt', 'a+') as f:
    for i in range(n):
        record = input(f"enter record {i+1} ")
        f.write(record + '\n')
        
f.seek(0)
print(f.read())

print("added ")



