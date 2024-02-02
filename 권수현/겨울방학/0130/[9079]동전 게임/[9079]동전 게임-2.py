# 비트마스킹을 이용한 풀이

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

change = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def solution(coins):
    for cnt in range(5):
        for values in combinations(change,cnt):
            copy = coins
            for value in values:
                for idx in value:
                    copy^=1<<idx

            if copy==0 or copy==511:
                return cnt
    return -1
                    


for _ in range(n):
    coins = ''
    for _ in range(3):
        values = list(map(str,input().split()))
        for value in values:
            if value=='H': coins+='1'
            else: coins+='0'

    print(solution(int(coins,2)))




