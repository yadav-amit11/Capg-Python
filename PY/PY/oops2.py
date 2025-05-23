class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # ✅ Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):  # ✅ Getter method
        return self.__balance

# --- Using the class ---
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)

print("Balance:", acc.get_balance())  # ✅ OK

# print(acc.__balance)  # ❌ This will raise an error (encapsulated)

# Bypassing encapsulation (not recommended, just for demo)
print("Accessing private variable using name mangling:", acc._BankAccount__balance)
