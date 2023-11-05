import sys
import math

input = sys.stdin.readline

def is_prime(n):
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_smallest_prime_from(n):
    if n <= 2: # 2 이하이면 다음 소수가 2
        return 2
    elif n % 2 == 0: # 짝수면 넘김
        n += 1

    while not is_prime(n): 
        n += 2 # 홀수만 검사

    return n

if __name__ == "__main__":
    t = int(input().strip())

    # 각 케이스마다 가장 가까운 소수 찾기
    for _ in range(t):
        n = int(input().strip())
        print(find_smallest_prime_from(n))