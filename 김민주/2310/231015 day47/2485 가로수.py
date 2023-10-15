import sys
import math

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    trees = []
    
    # 입력
    for _ in range(n):
        trees.append(int(input()))

    # 나무들 간 간격 구함
    intervals = []
    for i in range(1, n):
        intervals.append(trees[i] - trees[i-1])

    # 최대 공약수 계산
    gcd_interval = intervals[0]
    for interval in intervals[1:]:
        gcd_interval = math.gcd(gcd_interval, interval)

    # 결과 계산
    count = 0
    for interval in intervals:
        count += (interval // gcd_interval) - 1

    print(count)
