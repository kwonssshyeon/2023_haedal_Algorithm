# [1764 듣보잡](https://www.acmicpc.net/problem/1764)  

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    neverheard = set()
    intersection = set()

    for _ in range(n):
        neverheard.add(input().strip())
    for _ in range(m):
        name = input().strip()

        if name in neverheard:
            intersection.add(name)

    # 사전 순 정렬
    sorted_intersection = sorted(intersection)
    
    print(len(sorted_intersection))
    for name in sorted_intersection:
        print(name)
