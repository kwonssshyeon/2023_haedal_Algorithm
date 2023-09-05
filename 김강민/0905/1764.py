import sys
input = sys.stdin.readline

N, M = map(int, input().split())

noSee = []
noListen = []

for _ in range(N):
    noSee_name = input().strip()
    noSee.append(noSee_name)

for _ in range(M):
    noListen_name = input().strip()
    noListen.append(noListen_name)

for i in noSee:
    print(i)