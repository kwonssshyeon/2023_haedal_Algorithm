def solution(number):
    num_sum = sum(list(map(int, number))) # 문자열 number의 각 자리 숫자의 합을 계산
    remainder = num_sum % 9 # 각 자리 숫자의 합을 9로 나눈 나머지를 계산
    return remainder

number = "78720646226947352489"
print(solution(number))