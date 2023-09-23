import sys

input = sys.stdin.readline


def VPS(ary):
    cnt = 0
    for i in ary:
        if cnt < 0:
            return "NO"
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
    if cnt == 0:
        return "YES"
    return "NO"


N = int(input())
for _ in range(N):
    ary = list(input())
    print(VPS(ary))
