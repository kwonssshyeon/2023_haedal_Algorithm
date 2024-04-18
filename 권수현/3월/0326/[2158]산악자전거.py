import sys; input = sys.stdin.readline
import heapq
from math import inf

def solve():
    V, R, C = map(int, input().split()) # 초기 속도, 행의 수, 열의 수
    matrix = [list(map(int, input().split())) for _ in range(R)] # 산의 모습

    # 2차원 다익스트라
    # 각 칸마다 제일 빠르게 도착하는 시간을 저장하면서 진행
    distance = [[inf] * C for _ in range(R)]
    queue = [[0, 0, 0, V]] # 거리, 위치 r, c, 속도
    distance[0][0] = 0

    # 다익스트라 시작
    while queue:
        d, r, c, v = heapq.heappop(queue)
        # 저장된 시간보다 지금 걸리는 시간이 더 크다면
        # 지금 걸리는 시간으로 갱신할 필요가 없음
        if distance[r][c] < d:
            continue
        for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]: # 상하좌우
            # 다음 위치가 범위 안이며, 그 위치에 저장된 시간보다 지금 시간 + 한칸 움직이는데 걸리는 시간이 더 작으면 갱신
            if 0 <= rr < R and 0 <= cc < C and distance[rr][cc] > distance[r][c] + 1 / v:
                distance[rr][cc] = distance[r][c] + 1 / v
                heapq.heappush(queue, [distance[rr][cc], rr, cc, v * 2 ** (matrix[r][c] - matrix[rr][cc])])
                
    print(distance[R - 1][C - 1])

solve()