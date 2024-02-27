import sys
input = sys.stdin.readline

N, M = map(int, input().split())

noSee = []
noListen = []
noSeeListen = []

for i in range(N):
    name = input().strip()
    noSee.append(name)

for i in range(M):
    name = input().strip()    
    noListen.append(name)

noSeeListen = list(set(noSee) & set(noListen))
noSeeListen.sort()
print(len(noSeeListen))

for i in noSeeListen:
    print(i)