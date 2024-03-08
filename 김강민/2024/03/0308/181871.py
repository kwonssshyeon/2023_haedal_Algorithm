def solution(myString, pat):
    answer = 0
    for i in range(0, len(myString)):
        if myString[i:len(pat) + i] == pat:
            answer += 1
    return answer

# for은 range(a,b)일때, a 부터 b-1 까지의 숫자를 반복한다.
# myString을 slicing 하되, myString에서 1을 뺀 만큼 반복하므로 0부터 myString의 길이-1까지 반복한다.