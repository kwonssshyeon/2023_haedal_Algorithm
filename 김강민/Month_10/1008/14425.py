import sys
input = sys.stdin.readline

dic = {}
cnt = 0
N, M  = map(int, input().split())

for i in range(N):
    data = input().rstrip()
    dic[data] = True

for _ in range(M):
    data = input().rstrip()
    if data in dic:
        cnt += 1

print(cnt)