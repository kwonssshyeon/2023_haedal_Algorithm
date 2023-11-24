def solution(nums):
    answer = -1
    #DAT를 사용해도 됨. N이 작으니까! Direct Address Table
    cnt = [0]*1001
    answer2=0
    for x in nums :
        cnt[x] += 1

    for i in range(1000,0,-1):
        if cnt[i] == 1:
            return i

    answer2 = max( (i for i, count in enumerate(cnt) if count ==1),default=-1)
    print(answer2)

    sH = {}
    for x in nums:
        sH[x] = sH.get(x,0) + 1
    filtered_keys = [key for key, value in sH.items() if value == 1]
    answer = max(filtered_keys) if filtered_keys else -1
    return answer
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
