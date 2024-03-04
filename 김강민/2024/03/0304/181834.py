def solution(myString):
    answer = ''
    for string in myString:
        if ord(string) < ord("l"):
            answer += 'l'
        else: 
            answer += string
    return answer
    
    