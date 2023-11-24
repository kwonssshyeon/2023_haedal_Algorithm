from collections import defaultdict, Counter
def solution(nums):
    answer = -1
    nH = Counter(nums)
    for key in nH:
        if nH[key] == 1:
            answer = max(answer, key)
 
    return answer
                            
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([2235253, 5525612, 142561567, 123456789, 2235253, 560, 123456789, 142561567]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
