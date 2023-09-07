import sys
input  = sys.stdin.readline

N = int(input())

N_number = list(map(int, input().split()))

M = int(input())

M_number = list(map(int, input().split()))

card = {}

for i in range(len(N_number)):
    card[N_number[i]] = 0

for i in range(M):
    if M_number[i] not in card:
        print(0, end=' ')
    else:
        print(1, end=' ')