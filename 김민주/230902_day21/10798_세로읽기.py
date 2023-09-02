# [10798 세로읽기](https://www.acmicpc.net/problem/10798)  

import sys

input = sys.stdin.readline

# 입력
letters = [["" for _ in range(15)] for _ in range(5)]

for row in range(5):
    word = input().strip() # 공백제거한 문자열

    for col in range(len(word)):
        letters[row][col] = word[col]

# 출력
for col in range(15):
    for row in range(5):
        letter = letters[row][col]

        if not letter:
            continue
        print(letter, end="")
