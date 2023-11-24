from collections import Counter
from collections import Counter

def solution(nums):
    answer = -1
    sH = {}
    for key in nums:
        sH[key] = sH.get(key,0)+1

    # input이 N = 50만이어도 NlogN으로 구현하면 < (최대시간 *3) 이므로 통과가 된다.
    # 가장 작은 자기 분열 수 반환
    #Counter은 가장 많은 걸 우선적으로 만들어주네
    # nH = Counter(nums)

    print(sH)
    for key, value in sH.items():
        if key == value:
           return value
    return answer 
                          
print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))
