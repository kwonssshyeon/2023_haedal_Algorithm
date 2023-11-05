# 1541.py
# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

exp = input().split('-') 

num = [] 

for i in exp:
    sum = 0
    tmp = i.split('+')
    for j in tmp: 
        sum += int(j)
    num.append(sum) 

n = num[0] 

for i in range(1,len(num)): 
    n -= num[i]
print(n)