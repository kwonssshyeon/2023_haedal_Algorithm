import sys
input = sys.stdin.readline

N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
card_num = list(map(int, input().split()))

cnt = {}

for i in card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in card_num:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')