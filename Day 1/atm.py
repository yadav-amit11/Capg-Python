print("1.Withdraw")
print("2.Deposit")
print("3.Balance")
balance=15
option=int(input("enter option:"))
match option:
    case 1:
        amt=int(input("enter amount to withdraw: "))
        # add nested loop for bal>withdraw
        if amt > 0 and amt <= 5000: 
            print(f"Withdrawing {amt}")
            print(f"Remaining balance: {balance - amt}")   
        else:
            print("Invalid amount")   
    case 2:
        amt=int(input("Enter amount to deposit: "))
        if amt > 0 and amt <= 10000: 
            print(f"Deposited {amt}")
            print(f"New balance: {balance + amt}")
        else:
            print("Invalid amount")      
    case 3:
        print(f"Current balance: {balance}")
    case _:
        print("Invalid")

        