import sys

input = sys.stdin.readline
ary = []
a, b, c = 0, 0, 0
N, M = map(int, input().split(" "))
for _ in range(M):
    ary.append(list(map(int, input().split(" "))))


def unionFind(ary, N):
    ids = []
    for idx in range(N + 1):
        ids.append(idx)

    def connected(p, q):
        return ids[p] == ids[q]

    def minMax(a, b):
        if a < b:
            return a, b
        else:
            return b, a

    def union(p, q):
        id1, id2 = minMax(ids[p], ids[q])
        for idx, _ in enumerate(ids):
            if ids[idx] == id2:
                ids[idx] = id1

    for i in range(len(ary)):
        if ary[i][0] == 0:
            union(ary[i][1], ary[i][2])
        else:
            print("YES") if connected(ary[i][1], ary[i][2]) else print("NO")


unionFind(ary, N)
