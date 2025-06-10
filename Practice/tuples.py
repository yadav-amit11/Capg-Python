# # tp=(1,2,3,'amit',True)
# # print(tp[5])
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')

# # Following action is not valid for tuples
# # tup1[0] = 100;

# # So let's create a new tuple as follows
# tup1 = tup1 + tup2
# print (tup1)

# # Create a tuple
# # t = (10, 20, 30)

# # # Try modifying an element
# # t[1] = 99  # ❌ This will raise an error
# print ('abc', -4.24e93, 18+6.6j, 'xyz')
# x, y = 1, 2
# print ("Value of x , y : ", x,y)

# t = (10, 20, 30)
# t2 = (10.5,)         # Single-element tuple (comma is necessary)
# t3 = 1, 2, 4         # Tuple without parentheses (valid syntax)
# t += (1, 2, 4) 
# print(t)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.discard("Delhi")
# print(cities)

# parent class
class Manager: 
   def managerMethod(self):
      print ("I am the Manager")

# child class
class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
# second child class
class Employee2(Manager): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp1 = Employee1()  
emp2 = Employee2()
# method calls
emp1.managerMethod() 
emp1.employee1Method()
emp2.managerMethod() 
emp2.employee2Method()  