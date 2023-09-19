# 2212py
# https://www.acmicpc.net/problem/2212

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

sensors_diff = [sensor[i]-sensor[i-1] for i in range(1, n)]
sensors_diff.sort()

print(sum(sensors_diff[:n-k]))