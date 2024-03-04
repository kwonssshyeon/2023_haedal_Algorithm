def solution(arr):
    answer = []
    for num in arr:
        for i in range(num):
            answer.append(num)
    return answer