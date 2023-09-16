grade_scale = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0, "P": -1}
credits = []
credit_by_grades = []

for i in range(20):
    parts = input().split()
    credit = parts[1]; grade = parts[2]

    if grade == "P": 
        continue
    else: 
        credit = float(credit)
        grade = grade_scale[grade]

        credits.append(credit)
        credit_by_grades.append(credit * grade)

gpa = sum(credit_by_grades) / sum(credits)
print(gpa)