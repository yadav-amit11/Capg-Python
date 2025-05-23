# # # '''
# # # *user def fun
# # # *built in fun
# # # *miscellaneous fun
# # # *anonymous fun
# # # '''
# # # '''
# # # def functionname():
# # #     #statements
    
# # # '''

# # def add2num(b,a):
# #     c= a+b
# #     return [a,b,c]
# #     print("check check!!") #won't execute

# # a= int(input()) #10
# # b= int(input()) #20

# # res=add2num(a,b)
# # print(res)
# # '''
# # *with arg with return
# # *with arg without return
# # *without arg with return
# # *without arg without return 
# # '''


# '''
# types of arguments:-
# 1)positional arg
# '''
# # def example(a,b):
# #     return a,b,
# # print(example(10,20,))

# #default arg:-

# # def fun1(b=10,a):
# #     print(a,b)
# # fun1(100,1)

# #keyword arg
# # def fun1(a,b,c):
# #     print(a,b,c)
# # fun1(30,b=10,c=20)

# #arbitrary variable(*args)
# # def fun(*values):
# #     print(values)
# # fun(10,20,30,40,50,60,70)

# #arbitrary keyword(**arg)
# # def fun(**arg):
# #     print(arg)
# # fun(a=10,b=20,c=40)
# #*

# cart = {}

# def add_item(item, price):
#     cart[item] = price
#     print(f"Added '{item}' for ${price:.2f}")

# def remove_item(item):
#     if item in cart:
#         del cart[item]
#         print(f"Removed '{item}' from the cart.")
#     else:
#         print(f"Item '{item}' not found in the cart.")

# def calculate_total():
#     total = sum(cart.values())
    
#     if total > 100:
#         discount = 0.10
#     elif total > 50:
#         discount = 0.05
#     else:
#         discount = 0.0

#     discounted_total = total - (total * discount)
#     print(f"Subtotal: ${total:.2f}")
#     print(f"Discount: {int(discount * 100)}%")
#     print(f"Total after discount: ${discounted_total:.2f}")
#     return discounted_total

# add_item("Laptop Bag", 40)
# add_item("Wireless Mouse", 30)
# add_item("Keyboard", 50)

# remove_item("Headphones") 
# remove_item("Wireless Mouse")

# calculate_total()

def validate_password(password):
    length_valid = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*"
    if 8 <= len(password) <= 16:
        length_valid = True
    else:
        return "Password must be 8-16 characters long."

    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_digit:
        return "Password must contain at least one digit."
    if not has_special:
        return "Password must contain at least one special character (!@#$%^&*)."

    return "Password is valid!"

print(validate_password("Password123!"))
print(validate_password("pass"))
print(validate_password("PASSWORD123!"))
print(validate_password("Password"))
