#global , local scope:-
# x=5
# def fun():
#     global x
#     x=10
#     print(x,"aa")
#     # print(locals())
# fun()
# print(x)
# # print(globals())
# print(locals())

#

#python function objects:-

print("hii")
result=print
print(result)
result("hiii")

def fun():
    print("hhhhh")
res=fun
print(res,fun)
res()

def fun():
    print("abcc")
    def inner(id):
        print("hii")
        id()
    return inner
def abc():
    print("neww")
res = fun() #inner
res(fun)

def fun():
    print("hii")
    return "hhh"
fun()
#recursion