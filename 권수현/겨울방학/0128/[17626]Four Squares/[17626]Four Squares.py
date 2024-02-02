# 6:36~
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n = int(input())
s = int(n**(1/2))

num_list = list(range(s,-1,-1))
answer=0

for cnt in range(1,5):
    for items in combinations_with_replacement(num_list,cnt):
        num=0
        for i in items:
            num+=i**2
            if num==n:
                answer=len(items)
                print(answer)
                sys.exit(0)


# 최대 4
# 2면 제곱수+제곱수 / 3이면 제곱수 + 제곱수 + 제곱수
