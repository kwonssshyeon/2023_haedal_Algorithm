import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n == 2: 
        return True
    elif n < 2 or n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    m, n = map(int, input().split())
    primes_list = []

    # 소수들만 저장
    primes_list = [i for i in range(m, n + 1) if is_prime(i)]
    
    for elem in primes_list:
        print(elem)