print("Functions")

# print(calculate_grade)

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:  
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
print(calculate_grade)
print(type(calculate_grade))

student_1_marks = calculate_grade(57)
student_2_marks = calculate_grade(85)

print(f"Student 1 grade: {student_1_marks}")
print(f"Student 2 grade: {student_2_marks}")