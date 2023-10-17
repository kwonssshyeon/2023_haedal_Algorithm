def gcd(n, m):
    if m == 0:
        return n
    
    else:
        return gcd(m, n % m)

def lcm(n, m):
    return (n * m) / gcd(n, m)

def solution(n, m):
    return [gcd(n,m), lcm(n, m)]