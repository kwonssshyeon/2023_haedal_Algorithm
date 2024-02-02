# 19:40 ~

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

# 가로,세로,대각선의 인덱스
change = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


def isSame(arr):
    cur=arr[0]
    for i in arr:
        if i!=cur:
            return False
    return True


def answer():
    for cnt in range(8):
        for values in combinations(change,cnt):
            copy = coins.copy()
            for value in values:
                for idx in value:
                    if copy[idx]=='H':
                        copy[idx]='T'
                    else:
                        copy[idx]='H'

            if isSame(copy):
                return cnt
    return -1



for _ in range(n):
    coins = []
    for _ in range(3):
        coins+=list(map(str,input().split()))

    print(answer())



    

# 같은줄을 두번 뒤집는 일은 없음    