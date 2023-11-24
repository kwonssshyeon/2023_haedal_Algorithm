def solution(nums):
    answer = 0
    cnt = 0
    for x in nums:
        if x == 1:
            cnt += 1
        else:
            answer = max(answer, cnt)
            cnt = 0
    answer = max(answer, cnt)
    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
