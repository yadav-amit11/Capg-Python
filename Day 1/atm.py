print("1. Withdraw")
print("2. Deposit")
print("3. Balance")

balance = 15000

while True:
    option = int(input("Enter option: "))
    match option:
        case 1:
            amt = int(input("Enter amount to withdraw: "))
            if balance >= amt:
                if amt > 0 and amt <= 5000:
                    balance -= amt
                    print(f"Withdrawing {amt}")
                    print(f"Remaining balance: {balance}")
                else:
                    print("Invalid amount")
            else:
                print("Insufficient balance")
        case 2:
            amt = int(input("Enter amount to deposit: "))
            if amt > 0 and amt <= 10000:
                balance += amt
                print(f"Deposited {amt}")
                print(f"New balance: {balance}")
            else:
                print("Invalid amount")
        case 3:
            print(f"Current balance: {balance}")
        case _:
            print("Invalid option")
    cont = input("Continue? (y/n): ")
    if cont.lower() != 'y':
        break   