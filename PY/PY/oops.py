class Employee:
    def __init__(self, name, salary):
        self.name = name            # Public Variable
        self._salary = salary       # Protected Variable
        self.__bonus = 5000         # Private Variable

    def show_public(self):          # Public Method
        print("Public method called.")
        print("Name:", self.name)

    def _show_protected(self):      # Protected Method
        print("Protected method called.")
        print("Salary:", self._salary)

    def __show_private(self):       # Private Method
        print("Private method called.")
        print("Bonus:", self.__bonus)

    def access_private_method(self):
        # Access private method inside the class
        self.__show_private()

# Create object
emp = Employee("John", 60000)

# --- Accessing Variables ---
print("Public Variable:", emp.name)          # ✅ Allowed
print("Protected Variable:", emp._salary)    # ⚠️ Allowed (but discouraged)
print(emp.__bonus)                         # ❌ Not allowed (raises AttributeError)
print("Private Variable (using name mangling):", emp._Employee__bonus)  

# --- Accessing Methods ---
emp.show_public()          # ✅ Allowed
emp._show_protected()      # ⚠️ Allowed (but discouraged)
# emp.__show_private()     # ❌ Not allowed
emp.access_private_method()  # ✅ Private method accessed inside class
