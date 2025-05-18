
students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
max_marks = max(students.values())
print("\nStudent(s) with the highest marks:")
for name, marks in students.items():
    if marks == max_marks:
        print(name)

new_name = input("\nEnter a new student name: ")
if new_name in students:
    print("Name already exists.")
else:
    new_marks = int(input("Enter marks: "))
    students[new_name] = new_marks
    print("New student added.")
