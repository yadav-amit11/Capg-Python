#Sets in Python

# Demonstrating set behavior with booleans
s = {1, 100, "apple", False, 0}
s1 = {1, 100, "apple", True, 0}

print(s)   # Output: {False, 1, 100, 'apple'} → Note: False == 0, True == 1
print(s1)  # Output: {True, 100, 'apple', 0}

# Set operations
s = {1, 2, 34, 5, 3, 4, 2}
s1 = {12, 44, 1, 3, 2, 3}

# Union (returns a new set)
# res = s.union(s1)
# print(res)

# Update (modifies original set)
# s.update(s1)
# print(s)

# Intersection (common elements)
res = s.intersection(s1)
print(res)   # Output: {1, 2, 3} 

# In-place intersection
# s.intersection_update(s1)
# print(s)