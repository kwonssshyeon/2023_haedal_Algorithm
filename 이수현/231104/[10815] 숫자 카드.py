import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

_dict = {}  
for i in range(len(cards)):
    _dict[cards[i]] = 0  

for j in range(M):
    if checks[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')