def solution(numbers):
    no_num = 0
    for i in range(0, 10):
        if i not in numbers:
            no_num += i
    
    return no_num


numbers = [1, 2, 3, 4, 6, 7, 8, 0]
print (solution(numbers))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges