def solution(array, commands):
    answer = []
    arr = []
    for num in range(len(commands)):
        i = commands[num][0] -1
        j = commands[num][1]
        k = commands[num][2] -1
        
        arr = array[i:j]
        arr.sort()
        answer.append(arr[k])
        
    return answer