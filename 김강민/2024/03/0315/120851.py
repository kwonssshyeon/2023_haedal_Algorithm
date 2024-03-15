def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

# isdigit()
# 문자열이 숫자인지 아닌지 판별하는 함수
# 문자열이 숫자이면 True, 아니면 False를 반환한다.