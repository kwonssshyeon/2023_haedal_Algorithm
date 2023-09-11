# [24313 알고리즘 수업 - 점근적 표기 1](https://www.acmicpc.net/problem/24313)

a1, a0 = map(int, input().split()) # f(n)의 계수
c = int(input()) 
n0 = int(input()) # n 값

if a1*n0 + a0 <= c * n0 and a1 <= c:
    print(1)
else:
    print(0)