from collections import deque
def solution(nums):
    # answer = set()
    # for x in nums:
    #     answer.add(x)
    #
    # answer = sorted(list(answer),reverse=True)
    answer = deque()
    answer.appendleft(nums[0])

    # 내림차순으로 애초에 넣으면 sorted를 안해도 되는구나!
    # 앞에다 부터 넣기 !

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            answer.appendleft(nums[i])
    return list(answer)
   
print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))
