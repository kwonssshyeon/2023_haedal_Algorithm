import sys
import math

input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int, input().split())

    bigger = max(a, b)
    smaller = min(a, b)

    remainder = 1
    while remainder:
        remainder = bigger % smaller
        bigger, smaller = smaller, bigger % smaller
    gcd = bigger

    lcm = (a * b) // gcd

    print(lcm)