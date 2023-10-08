import sys

input = sys.stdin.readline
ary = []
a, b, c = 0, 0, 0
N, M = map(int, input().split(" "))
for _ in range(M):
    ary.append(list(map(int, input().split(" "))))


def unionFind(ary, N):
    def find(x):
        if parent[x] == x:
            return x
        path = [x]  # 경로 압축을 위한 경로 저장
        while x != parent[x]:
            x = parent[x]
            path.append(x)
        for node in path:
            parent[node] = x
        return x

    parent = list(range(N + 1))  # 각 원소의 부모를 자기 자신으로 초기화

    def union(p, q):
        root_p = find(p)
        root_q = find(q)
        if root_p != root_q:
            parent[root_p] = root_q  # 균형 잡힌 트리 유지

    for i in range(len(ary)):
        if ary[i][0] == 0:
            union(ary[i][1], ary[i][2])
        else:
            print("YES") if find(ary[i][1]) == find(ary[i][2]) else print("NO")


unionFind(ary, N)
