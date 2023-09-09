import sys
input = sys.stdin.readline

N = int(input())

position = list(map(int, input().split()))

s_position = sorted(set(position))

dic = {}

for i in range(len(s_position)):
    dic[s_position[i]] = i

for i in position:
    print(dic[i], end=' ')