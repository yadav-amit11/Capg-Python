s = "   Hello Python World   "

print(s.lower())           # '   hello python world   '
print(s.upper())           # '   HELLO PYTHON WORLD   '
print(s.title())           # '   Hello Python World   '
print(s.strip())           # 'Hello Python World'

print("abc123".isdigit())  # False
print("123".isdigit())     # True
print("abc".isalpha())     # True

email = "abc@gmail.com"
print(email.find("@a"))     # 3
print(email.endswith(".com"))  # True

text = "banana"
print(text.count("a"))     # 3
print(text.replace("a", "*"))  # b*n*n*

words = "apple,banana,,grape".split(",")  # ['apple', 'banana', 'grape']
joined = "-".join(words)                # 'apple-banana-grape'

# Formatting
name = "Ravi"
score = 95
print("Student: {}, Score: {}".format(name, score))  # Student: Ravi, Score: 95
print("name{name}".format_map({'name':2}))
print("5".zfill(-2))  # 0005
print("asadkas".strip('sa'))
print("a".center(5,'o'))
