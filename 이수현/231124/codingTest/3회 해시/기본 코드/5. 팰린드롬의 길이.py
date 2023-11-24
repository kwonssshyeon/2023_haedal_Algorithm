from collections import Counter
def solution(s):
    answer = 0
    odd = 0
    #짝수 모두 가능
    #홀수면 가장 긴 글자만 포함하기
    #다른 홀수는 -1해서 더하기

    nH = Counter(s)
    for key in nH:
        if nH[key] % 2 == 1:
            odd += 1
    return len(s) - odd + 1 if odd > 0 else len(s)
    #     if nH[key] % 2 == 0:
    #         answer += nH[key]
    #     else:
    #         odd.append(int(nH[key]))
    #
    # if (odd):
    #     answer += sum(odd) - len(odd) + 1

    #return answer
    
                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
