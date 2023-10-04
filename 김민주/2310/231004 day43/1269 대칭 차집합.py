# [1269 대칭 차집합](https://www.acmicpc.net/problem/1269)  

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    nA, nB = map(int, input().split())

    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    intersection = A.intersection(B)
    
    countA = len(A) - len(intersection)
    countB = len(B) - len(intersection)
    
    print(countA + countB)