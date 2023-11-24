from collections import defaultdict

import sys

input = sys.stdin.readline


def solution2(n, m, name):
    answer = []
    sH = defaultdict(int)
    for x in name:
        sH[x] += 1
    for key in sH:
        if sH[key] == 2:
            answer.append(key)
    print(len(answer))
    for x in sorted(answer):
        print(x)


def solution(n, m, name):
    answer = []
    nH = defaultdict(int)
    for index, key in enumerate(name):
        if index < n:
            nH[key] = 1
        else:
            if key in nH:
                answer.append(key)
    print(len(answer))
    answer.sort()
    for name in answer:
        print(name)


arr = []
n, m = map(int, input().split(" "))
for i in range(n + m):
    arr.append(input().rstrip())
solution(n, m, arr)
# solution2(n, m, arr)
