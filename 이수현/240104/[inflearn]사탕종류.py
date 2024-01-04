"""
현수에게 사탕이 n개 있습닏.
가지고 있는 사탕의 절반만 먹으라고 했습니다.
매개변수 nums에 현수가 가지고있는 사탕의 종류 정보가 주어지면, n/2개의 사탕을 먹는다면 최대 몇종류의 사탕을 먹을 수 있는지를 반환하는 프로그램을 작성하시오.
"""

import sys

input = sys.stdin.readline

# test = [2, 1, 1, 3, 2, 3, 1, 2]
# test = [1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]
# test = [5, 5, 5, 5, 5, 5]
# test = [12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23]
# test = [100, 200, 300, 400, 500, 600, 700, 800]


def solution():
    nums = list(map(int, input().split(",")))
    isSet = set(nums)

    # if len(nums) // 2 >= len(isSet):
    #     answer = len(isSet)
    # else:
    #     answer = len(nums) // 2
    # return answer

    return len(isSet) if len(nums) // 2 >= len(isSet) else len(nums) // 2


print(solution())
