# 1924.py
# https://www.acmicpc.net/problem/1924

import sys
import calendar

input = sys.stdin.readline

x, y = map(int, input().split())

day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

Day = calendar.weekday(2007, x, y)
print(day[Day])