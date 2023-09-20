# 2503.py
# https://www.acmicpc.net/problem/2503

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

count = [list(map(int, input().split())) for _ in range(n)]

num = [1,2,3,4,5,6,7,8,9]
answer = 0

for num in permutations(num,3):
    isAnswer = True
    
    for i in range(n):
        if not isAnswer: break
        
        strike, ball = 0, 0
        for j in range(3):
            target = str(count[i][0])
            
            if int(target[j]) == num[j]: strike += 1
            elif int(target[j]) in num: ball += 1
            
        if strike != count[i][1] or ball != count[i][2]:
            isAnswer = False
            break
    if isAnswer: answer += 1
    
print(answer)


