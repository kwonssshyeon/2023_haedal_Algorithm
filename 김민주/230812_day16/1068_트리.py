# https://www.acmicpc.net/problem/1068 트리

import sys

input = sys.stdin.readline


def dfs(tree, start):
  if len(tree[start]) == 0:
    return 1
  count = 0
  for node in tree[start]:
    count += dfs(tree, node)
  return count


if __name__ == "__main__":
  # 입력 받기
  n = int(input())
  parents = list(map(int, input().split()))
  remove_node = int(input())

  # 트리 초기화
  tree = [[] for _ in range(n)] # 2d list
  root = -1 # 루트 노드일 때 부모의 값
  for i in range(n):
    if parents[i] == -1: # 부모 == -1이면
      root = i # 루트 노드로 지정
    else:
      tree[parents[i]].append(i)
    
  # 노드 삭제
  tree[remove_node] = [] # 노드에 딸린 자식들 삭제
  if remove_node == root:
    print(0)
  else:
    tree[parents[remove_node]].remove(remove_node)
    print(dfs(tree, root)) # dfs로 순회하며 리프 개수 세기
