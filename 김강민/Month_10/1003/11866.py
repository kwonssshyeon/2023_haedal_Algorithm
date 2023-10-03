import sys
input = sys.stdin.readline

N, K = map(int, input().split())

que = [i for i in range(1, N+1)]
remove_que = []
num = 0

for _ in range(N):
    num += (K - 1)
    if num >= len(que):
        num %= len(que)
    remove_que.append(str(que[num]))
    que.pop(num)

print("<",", ".join(remove_que),">", sep='')