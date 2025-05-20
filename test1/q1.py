def cal_grades(marks_list):
    dict = {}
    SID = 1
    for score in marks_list:  
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        dict[SID] = grade
        SID += 1
    return dict

input_scores = input("Enter student marks: ")
scores = [int(score) for score in input_scores.split()]
print(cal_grades(scores))
