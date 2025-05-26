# # def word_frequency(userStr):
# #     for ch in ",.!?;:":
# #         userStr = userStr.replace(ch, "") 
# #     words = userStr.lower().split()
# #     freq = {}
# #     for word in words:
# #         if word in freq:
# #             freq[word] += 1
# #         else:
# #             freq[word] = 1
# #     return freq

# # input_userStr = "Today is a a good ? maybe yes yes"
# # print(word_frequency(input_userStr))

# # def grp_anagram(words):
# #     res = {}
# #     for word in words:
# #         key = ''.join(sorted(word)) 
# #         if key in res:
# #             res[key].append(word)
# #         else:
# #             res[key] = [word]
# #     return list(res.values())
# # words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# # print(grp_anagram(words))

# class Student:
#     # Class-level dictionary to store all students
#     registry = {}

#     def __init__(self, student_id, name, grade):
#         self.id = student_id
#         self.name = name
#         self.grade = grade

#         # Store instance in class-level dictionary
#         Student.registry[self.id] = self

#     @classmethod
#     def get_top_students(cls, n):
#         # Sort students by grade in descending order
#         sorted_students = sorted(cls.registry.values(), key=lambda s: s.grade, reverse=True)
#         return sorted_students[:n]

# # Example usage
# s1 = Student(1, 'Alice', 88)
# s2 = Student(2, 'Bob', 92)
# s3 = Student(3, 'Charlie', 85)
# s4 = Student(4, 'David', 95)

# top_students = Student.get_top_students(2)

# # Print top students
# for student in top_students:
#     print(f"{student.name} - Grade: {student.grade}")

def grp_anagram(words):
    res = {}
    for word in words:
        key = ''.join(sorted(word)) 
        if key in res:
            res[key].append(word)
        else:
            res[key] = [word]
    return list(res.values())
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(grp_anagram(words))