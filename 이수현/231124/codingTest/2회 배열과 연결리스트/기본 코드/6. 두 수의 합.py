def solution(nums, target):
    answer = [0] * 2
    nums.sort()
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if target == nums[i] + nums[j]:
                return [nums[i],nums[j]]
            elif target < nums[i] + nums[j]:
                continue
    return answer
        
                                       
print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))
