import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))


for _ in range(n):
    question, s, b = map(int, input().split())
    question = list(str(question))
    count = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= count
        for j in range(3):
            if num[i][j] == question[j]:
                strike += 1
            elif question[j] in num[i]:
                ball += 1
            
        if (strike != s) or (ball != b):
            num.remove(num[i])
            count += 1

print(len(num))