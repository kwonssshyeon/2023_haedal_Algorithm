import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n = int(input())
s = int(n**(1/2))



def func():
    global n

    if (n**(1/2))%1==0:
        return 1
    
    squares = {i**2 for i in range(1,s+1)}

    for a in squares:
        if n-a in squares:
            return 2
        
    for a,b in combinations_with_replacement(squares,2):
        if n-a-b in squares:
            return 3
        
    return 4

print(func())