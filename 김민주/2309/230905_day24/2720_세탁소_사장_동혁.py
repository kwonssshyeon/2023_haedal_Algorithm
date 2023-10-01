# [2720 세탁소 사장 동혁](https://www.acmicpc.net/problem/2720)  

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    C = int(input()) # 124cent
    quarter = C // 25 # 124 // 25 = 4
    dime = C % 25 // 10 # 24 // 10 = 2
    nickel = C % 25 % 10 // 5 # 4 // 5 = 0
    penny = C % 25 % 10 % 5 # 4

    print(f"{quarter} {dime} {nickel} {penny}")
