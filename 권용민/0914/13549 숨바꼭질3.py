from collections import deque

n, k = map(int, input().split())
time = 0

visited = [False for _ in range(200000)]
q = deque()
q.append([n, time])

while True:
    [n, time] = q.popleft()
    if n == k:
        print(time)
        break
    if n < 0 or n >= 200000:
        continue
    if visited[n] is True:
        continue
    
    visited[n] = True
    if n < k:
        q.appendleft([n*2, time])
    q.append([n+1, time+1])
    q.append([n-1, time+1])

"""
2시 13분 완료....아깝쓰

일반적인 BFS를 사용하려면 모든 간선의 길이가 다 같아야 한다!
이 문제같은 0-1BFS는 길이가 0인 간선을 큐의 앞에 넣는 방식으로 하거나,
길이가 0인 간선을 간선으로 취급 안하고 걍 n+1, n-1을 넣을때 그것의 2의 거듭제곱들도 싹다 큐에 넣는 식으로 해결 가능

"""