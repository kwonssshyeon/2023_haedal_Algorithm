# 20:04 ~ 20:20
# 빈 배열에 대한 예외처리

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    orders = input().strip()
    n = int(input())
    data = input().strip()[1:-1].split(",")
    if n==0: number = deque()
    else: number = deque(data)
    

    finish = reverse = False
    for order in orders:
        if order=="R":
            reverse = not reverse
        else:
            if len(number)==0:
                print("error")
                finish = True
                break
            if reverse:
                number.pop()
            else:
                number.popleft()
    
    if not finish:
        if reverse: number.reverse()
        print("["+",".join(number)+"]")