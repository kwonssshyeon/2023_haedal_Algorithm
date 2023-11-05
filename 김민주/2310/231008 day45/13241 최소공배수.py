import sys
import math

input = sys.stdin.readline

def find_gcd(a, b) -> int:
    remainder = 1
    while remainder:
        remainder = a % b
        a, b = b, remainder
    return a

if __name__ == "__main__":
    a, b = map(int, input().split())

    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    print(lcm)
    