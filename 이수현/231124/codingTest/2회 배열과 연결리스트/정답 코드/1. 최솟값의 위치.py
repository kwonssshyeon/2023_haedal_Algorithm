def solution(nums):
    answer = 0
    minN = 1000000
    n = len(nums)
    for i in range(n):
        if nums[i] < minN:
            minN = nums[i]
            answer = i
    return answer

print(solution([7, 10, 5, 3, 2, 15, 19]))
print(solution([-12, 12, 30, -15, -5, 3, 9, -11, 14]))
print(solution([17, 11, 5, 8, 23, 29, 19, 12, 25, 16, 2]))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21]))
