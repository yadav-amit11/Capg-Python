# Creating tuples
t = (10, 20, 30)
t2 = (10.5,)         # Single-element tuple (comma is necessary)
t3 = 1, 2, 4         # Tuple without parentheses (valid syntax)
t += (1, 2, 4)       # Tuple concatenation

print(t3)            # Output: (1, 2, 4)
print(type(t2))      # Output: <class 'tuple'>
print(type(t))       # Output: <class 'tuple'>
print(t2)            # Output: (10.5,)
print(t)             # Output: (10, 20, 30, 1, 2, 4)

# Tuple methods
t = (1, 2, 3, 4, 4, 4)
print(t.count(4))    # Output: 3 (occurrences of 4)
print(len(t))        # Output: 6 (length of tuple)
print(t.index(4))    # Output: 3 (first index of 4)
