# https://www.acmicpc.net/problem/11724 
# 주어진 그래프에서 연결 요소의 개수 구하기
# DFS 탐색

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v):
  visited[v] = True
  
  for i in vertices[v]:
    if visited[i] is False:
      dfs(i)


if __name__ == "__main__":
  # 인풋 받기
  n, m = map(int, input().split()) # the number of vertices & edges
  
  global vertices; vertices = [[] for _ in range(n+1)] # 2차원 배열
  global visited; visited = [False] * (n+1)

  for _ in range(m):
    u, v = map(int, input().split()) # two adjacent vertices
    vertices[u].append(v); vertices[v].append(u)

  # 연결 요소의 개수 세기
  ## 모든 인접 리스트를 순회하면서
  ## 방문하지 않은 노드가 있다면
  ## DFS로 한 연결 요소의 정점 모두 방문
  connected_components = 0
  for i in range(1, n+1):
    if visited[i] is False:
      dfs(i)
      connected_components += 1
  
  print(connected_components)