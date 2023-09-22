# [1037 약수](https://www.acmicpc.net/problem/1037)

import math

num_real_divisors = int(input())
real_divisors = list(map(int, input().split()))

n = max(real_divisors) * min(real_divisors)

print(n)