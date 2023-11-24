def solution(score, k):
    answer = 0
    for x in score:
        if x >= k:
            answer += 1        
    return answer

print(solution([60, 50, 80, 90, 55, 70, 65, 45], 60))
print(solution([10, 20, 30, 40, 50], 60))
print(solution([50, 65, 75, 87, 90, 55, 78, 93, 100], 70))
print(solution([99, 30, 50, 55, 68, 70, 90, 100], 80))
