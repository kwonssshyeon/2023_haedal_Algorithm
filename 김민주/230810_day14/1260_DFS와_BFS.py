import sys
from collections import deque
input = sys.stdin.readline


def dfs(graph, start_v):
  visited = []; stack = [start_v]
  
  while stack:
    v = stack.pop()
    if v not in visited:
      visited.append(v)
      stack.extend(sorted(graph[v], reverse=True))
      print(v, end=" ")
  

def bfs(graph, start_v):
  visited = []; queue = deque([start_v])
  
  while queue:
    v = queue.popleft()
    if v not in visited:
      visited.append(v)
      queue.extend(sorted(graph[v]))
      print(v, end=" ")
  
  
if __name__ == "__main__":
  # 입력 받기
  n, m, v = map(int, input().split()) 
  # 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 시작 정점의 번호 V
  graph = [[] for _ in range(n+1)] # 2d array
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # graph = [[a, b]
    graph[b].append(a)  #          [b, a]]

  # DFS, BFS 결과 출력
  dfs(graph, v)
  print()
  bfs(graph, v)
  
