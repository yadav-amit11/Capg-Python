cart = {}
def add_item():
    item = input("Enter item: ")
    price = float(input("Enter price: "))
    cart[item] = price
    print(f"{item} added")

def remove_item():
    item = input("Enter item to remove: ")
    if item in cart:
        del cart[item]
        print(f"{item} removed")
    else:
        print(f"{item} not found ")

def calculate_total():
    total = sum(cart.values())
    if total > 100:
        discount = 0.10
    elif total > 50:
        discount = 0.05
    else:
        discount = 0
    final_total = total - (total * discount)
    print("Total:",total)
    print(f"Discount: {discount*100}%")
    print("Final Total:",final_total)

while True:
    print("1. Add Item 2. Remove Item 3.Total 4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        calculate_total()
    elif choice == '4':
        break
    else:
        print("Invalid")
