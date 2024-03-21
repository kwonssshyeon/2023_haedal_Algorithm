import sys
input = sys.stdin.readline

n = int(input())
sum_num = 0
for _ in range(n):
    a, b = map(str, input().split())
    reversed_a = int(a[::-1])
    reversed_b = int(b[::-1])
    
    sum_num = str(reversed_a + reversed_b)[::-1]
    
    if len(sum_num) < len(a):
        sum_num = '0' * len(a) - len(sum_num) + sum_num

    print(sum_num)