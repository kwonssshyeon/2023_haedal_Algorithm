import sys
import math

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    numeratorA, denominatorA = map(int, input().split())
    numeratorB, denominatorB = map(int, input().split())

    new_numerator = numeratorA * denominatorB + numeratorB * denominatorA 
    new_denominator = denominatorA * denominatorB # 분모를 같게 바꿈

    gcd_new = gcd(new_numerator, new_denominator)

    simplified_numerator = new_numerator // gcd_new
    simplified_denominator = new_denominator // gcd_new

    print(f"{simplified_numerator} {simplified_denominator}")
