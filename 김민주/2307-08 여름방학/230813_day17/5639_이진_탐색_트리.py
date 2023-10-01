# https://www.acmicpc.net/problem/5639 이진 검색 트리
# 전위순회 결과를 입력으로 받아서 후위순회 결과 출력하기

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


class Node:
  def __init__(self, key):
    self.key = key
    self.left = None; self.right = None


class BST:
  def __init__(self):
    self.root = None

  def insert(self, key):
    self.root = self._insert_value(self.root, key)
    
  def _insert_value(self, node, key): 
    if node is None: # 아직 노드가 없을 때
      node = Node(key) # 루트 노드 생성
    else: # 왼쪽 자식 키 < 노드의 키 < 오른쪽 자식 키인 특징
      if node.key > key:
        node.left = self._insert_value(node.left, key)
      else:
        node.right = self._insert_value(node.right, key)

    return node # 루트 노드를 리턴

  def postorder(self):
    def _postorder(root):
      if root is None:
        return
      _postorder(root.left)
      _postorder(root.right)
      print(root.key)

    _postorder(self.root)


if __name__ == "__main__":
  bst = BST()
  while True:
    try:
      data = int(input())
      bst.insert(data)
    except:
      break

  bst.postorder()
