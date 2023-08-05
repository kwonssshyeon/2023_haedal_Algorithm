import sys
from collections import deque

n = int(input())
arr = [deque() for _ in range(n+1)]
# 이중 리스트..? 구현
for i in range(1, n+1):
    tmpList = deque(map(int, sys.stdin.readline().split()))
    me = tmpList.popleft()

    partner = tmpList.popleft()
    while partner > -1:
        dist = tmpList.popleft()
        arr[me].append([partner, dist])
        partner = tmpList.popleft()

def dfs(nodeIndex: int, preIndex: int):
    # 연결된 간선 없는 노드
    if len(arr[nodeIndex]) == 0:
        return 0

    maxDist = 0
    maxDistIndex = nodeIndex
    # dfs
    # vertex[0]:partner, vertex[1]:dist
    for vertex in arr[nodeIndex]:
        # 방금 타고 온 간선 재이용하려는 경우
        if preIndex == vertex[0]:
            continue
        # dfs 진행
        dist, distIndex = dfs(vertex[0], nodeIndex)
        dist += vertex[1]
        if dist > maxDist:
            maxDist = dist
            maxDistIndex = distIndex

    return maxDist, maxDistIndex


maxDist = 0
maxDistIndex = 0
maxDist, maxDistIndex = dfs(1, 0)

realMaxDist = 0
realMaxDistIndex = 0
realMaxDist, realMaxDistIndex = dfs(maxDistIndex, 0)

print(realMaxDist)

# 트리의 노드를 구슬로, 간선들을 구슬끼리 잇는 실로, 간선의 가중치를 그 실의 길이라고 생각하고 이 실로 연결된 구슬들 사이의 최장거리(트리의 지름)를 구해봅시다.
# 구슬 중에서 아무 구슬(노드1)이나 골라 위로 들어올리면 실이 축 늘어지며 가장 길게 떨어진 구슬(노드2)이 나올 것입니다(처음 선택한 노드1에서 가장 먼 노드2).
# 이 구슬(노드2)을 잡은 후, 이 구슬(노드2)에서 실로 가장 길게 연결된 구슬(노드3)을 잡고 양쪽으로 잡아당기면 실로 연결된 구슬들의 최장거리가 나올 것입니다.