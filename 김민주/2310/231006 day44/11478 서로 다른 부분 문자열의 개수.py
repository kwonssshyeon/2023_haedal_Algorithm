# [11478 서로 다른 부분 문자열의 개수](https://www.acmicpc.net/problem/11478)  

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    org_str = input().strip()

    substrs = set()
    n = len(org_str)

    for i in range(n):
        for j in range(i+1, n+1):
            substrs.add(org_str[i:j])

    print(len(substrs))