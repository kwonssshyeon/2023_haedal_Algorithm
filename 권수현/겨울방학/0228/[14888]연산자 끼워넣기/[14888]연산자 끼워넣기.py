# 순열 -> 시간초과

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
opps = list(map(int,input().split()))
opp_idx = []
for i in range(4):
    for _ in range(opps[i]):
        opp_idx.append(i)

mini,maxi = float('inf'),-float('inf')

# for orders in permutations(list(range(n-1))):
#     # opp 순서대로 담기
#     ops=[]
#     for order in orders:
#         ops.append(opp_idx[order])

for ops in permutations(opp_idx,n-1):
    # 연산
    result = nums[0]
    for num,op in zip(nums[1:],ops):
        if op==0:
            result+=num
        elif op==1:
            result-=num
        elif op==2:
            result*=num
        elif op==3:
            if result<0:
                result*=(-1)
                result//=num
                result*=(-1)
            else:
                result//=num

    maxi = max(maxi,result)
    mini = min(mini,result)


print(maxi)
print(mini)