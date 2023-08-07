import sys

# arr에 저장해 sort하는 방법도 고려
first = 0
second = 0
third = 0
isContinue = True
while isContinue:
    totalCal = 0
    while True:
        tmp = sys.stdin.readline()
        if tmp == '\n':
            break
        if tmp == '-1\n':
            isContinue = False
            break
        totalCal += int(tmp)
    if totalCal > first:
        third = second
        second = first
        first = totalCal
    elif totalCal > second:
        third = second
        second = totalCal
    elif totalCal > third:
        third = totalCal

print(first + second + third)

# https://adventofcode.com/2022/day/1
# 여기문제 풀어쓰요
