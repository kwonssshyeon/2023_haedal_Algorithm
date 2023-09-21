import sys
import math

input = sys.stdin.readline
import math
import sys


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


N = int(input())
ary = []

for i in range(N):
    x, y, z = map(str, input().split())
    x, y = int(x), int(y)
    if z == "Y":
        ary.append((x, y))

convex_hull_points = convex_hull(ary)

print(len(convex_hull_points))
for x, y in convex_hull_points:
    print(x, y)
