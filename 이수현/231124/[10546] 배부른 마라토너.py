import sys
from collections import defaultdict

input = sys.stdin.readline


# 역순에 주의
# 동명이인에 주의


def solution(n, name):
    nH = defaultdict(int)
    for index, key in enumerate(reversed(name)):
        if index < n - 1:
            nH[key] += 1
        else:
            nH[key] -= 1
            if nH[key] < 0:
                return key
            # if key not in nH:
            #     return key
    # if nH[key] < 0:
    #     return key


name = []
n = int(input())
for _ in range(2 * n - 1):
    name.append(input().rstrip())

result = solution(n, name)
print(result)
