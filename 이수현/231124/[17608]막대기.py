import sys

input = sys.stdin.readline


def solution(nums):
    cnt = 1
    max = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > max:
            max = nums[i]
            cnt += 1
    return cnt


N = int(input())
nums = []
for _ in range(N):
    user_input = int(input())
    nums.append(user_input)
print(solution(nums))
