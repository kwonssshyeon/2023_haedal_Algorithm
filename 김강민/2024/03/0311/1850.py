import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print('1' * gcd(a, b))

# 공부했던 최대공약수를 적용해봤는데 안돼서 원인을 찾던 중
# 출력값에 '1'을 곱해야 한다는걸 알게되었다...
# 하 하 하...