# [22108 통계학](https://www.acmicpc.net/problem/22108)  

import sys
import math
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

# 산술평균
average = round(sum(nums) / n)

# 중앙값
nums.sort()
median = nums[n // 2]
# median = (sorted(nums))[n // 2] # 틀림

# 최빈값
count = Counter(nums)
mode_list = count.most_common()
if len(nums) > 1 and mode_list[0][1] == mode_list[1][1]:
    mode = mode_list[1][0] # 최빈값이 두 개 이상이면 두 번째로 작은 값으로 지정
else:
    mode = mode_list[0][0]

# 범위
range = max(nums) - min(nums)

print(average)
print(median)
print(mode)
print(range)