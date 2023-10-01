# [14425 문자열 집합](https://www.acmicpc.net/problem/14425)  

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    S = set()
    count = 0

    n, m = map(int, input().split())

    for i in range(n):
        str = input().strip() # 집합 S에 포함되어 있는 문자열
        S.add(str)

    for i in range(m):
        str = input().strip() # 검사해야 하는 문자열
        if str in S:
            count += 1

    print(count)