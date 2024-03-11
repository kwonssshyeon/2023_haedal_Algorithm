def gcd(a, b):
    i = min(a,b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcd(4, 28)) # 4

## 유클리드 알고리즘
def gcd_euclid(a, b):
    if b == 0:
        return a
    return gcd_euclid(b, a % b)

print(gcd_euclid(4, 28)) # 4