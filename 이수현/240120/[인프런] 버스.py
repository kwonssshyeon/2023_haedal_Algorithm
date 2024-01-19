import sys

input = sys.stdin.readline


def solution(weight, limit):
    answer, total = 0, 0
    weight.sort()
    for i, w in enumerate(weight):
        total += w
        if total > limit:
            return i

    return len(weight)


print(solution([300, 100, 230, 120, 90, 150, 60], 700))
print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))
