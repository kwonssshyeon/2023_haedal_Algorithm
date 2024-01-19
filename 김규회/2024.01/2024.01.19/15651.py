# 15651.py
# https://www.acmicpc.net/problem/15651

import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())

for i in product(range(1, n + 1), repeat = m):
    print(*i)