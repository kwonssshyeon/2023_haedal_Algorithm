# [10815 숫자 카드](https://www.acmicpc.net/problem/10815)

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    numbercard_set = set()

    # n개의 숫자 카드 저장
    n = int(input())
    numbers = list(map(int, input().split()))
    for number in numbers:
        numbercard_set.add(number)

    # print(numbers)
    # print(numbercard_set)

    # m개의 수 검사
    m = int(input())
    check_numbers = list(map(int, input().split()))
    # print(check_numbers)
    for cn in check_numbers:
        if cn in numbercard_set:
            print(1, end=" ")
        else: 
            print(0, end=" ")
    print() # 이걸 해야 맨끝에 %가 안나온다...
