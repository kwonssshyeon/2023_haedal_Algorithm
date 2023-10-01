# [2869 달팽이는 올라가고 싶다](https://www.acmicpc.net/problem/2869)  

import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().split())

days = 1 + math.ceil((V - A) / (A - B))
print(days, end="")