grade_scale = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0, "P": -1}
sum_credit_by_grade = 0.0
sum_credit = 0.0

for _ in range(20):
    parts = input().split()
    credit = float(parts[1]); grade = grade_scale[parts[2]] # 입력 받아서 원하는 데이터/형식으로 변환

    if grade == -1: # P일 때
        continue
    else: 
        sum_credit += credit
        sum_credit_by_grade += credit * grade

gpa = sum_credit_by_grade / sum_credit
print(gpa)