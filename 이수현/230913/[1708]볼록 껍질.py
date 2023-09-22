import sys
import math

input = sys.stdin.readline

N = int(input())
ary = []
for _ in range(N):
    x, y = map(int, input().split())
    ary.append((x, y))

mindot = min(ary, key=lambda p: (p[1], -p[0]))
sortedAry = sorted(
    ary,
    key=lambda p: (math.atan2(p[1] - mindot[1], p[0] - mindot[0]), p[1], -p[0]),
)


def ccw(i, j, k):
    return (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0]) > 0


def convex_hull(sortedAry):
    # convex_hull
    convex_hull = [sortedAry[0], sortedAry[1]]
    for i in range(2, len(sortedAry)):
        while len(convex_hull) > 1 and not ccw(
            convex_hull[-2], convex_hull[-1], sortedAry[i]
        ):
            # print(convex_hull.pop())
            convex_hull.pop()
        convex_hull.append(sortedAry[i])
    return convex_hull


result = convex_hull(sortedAry)
print(len(result))
