import sys
import math

input = sys.stdin.readline


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def planetcount(planet_list, start_x, start_y, end_x, end_y):
    cnt = 0
    for planet in planet_list:
        dis1 = calculate_distance(start_x, start_y, planet[0], planet[1])
        dis2 = calculate_distance(end_x, end_y, planet[0], planet[1])

        if dis1 < planet[2] and dis2 < planet[2]:
            pass
        elif dis1 < planet[2]:
            cnt += 1
        elif dis2 < planet[2]:
            cnt += 1
    return cnt


N = int(input().rstrip())
for _ in range(N):
    start_x, start_y, end_x, end_y = map(int, input().rstrip().split())
    planet = int(input().rstrip())
    planet_list = []
    for _ in range(planet):
        planet_list.append(list(map(int, input().rstrip().split())))
    result = planetcount(planet_list, start_x, start_y, end_x, end_y)
    print(result)
