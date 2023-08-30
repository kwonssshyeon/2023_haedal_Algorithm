import sys
import math

def get_dist(a, b):
    aa = (a[0]-b[0])**2
    bb = (a[1]-b[1])**2
    return math.sqrt(aa + bb)

def edit_dists(new_taken_star):
    for i, star in enumerate(stars):
        if star[2] == True:
            continue
        dist[i] = min(dist[i], get_dist(new_taken_star, star))


n = int(sys.stdin.readline())
stars = [0 for _ in range(n)]
dist = [sys.maxsize for _ in range(n)]
for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars[i] = [x, y, False]
edit_dists(stars[0])
stars[0][2] = True

answer = 0
for i in range(1, n):
    closest_dist = min(dist[i] for i in range(n) if stars[i][2] is False)
    closest_star = stars[dist.index(closest_dist)]
    answer += closest_dist
    edit_dists(closest_star)
    closest_star[2] = True

print(format(answer, ".2f"))




'''
크루스칼: 전체 간선 중 최단거리 선택 => 간선들이 정해져 있을 때 사용
프림: 현재 트리에서 최단거리 노드 선택

다익스트라: 1번노드 to 모든노드 최단거리 알고리즘 => MST는 아님
플로이드-워셜: 모든 노드간 최단거리 알고리즘 => MST 아님
'''
