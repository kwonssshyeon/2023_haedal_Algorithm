from collections import Counter
def solution(s):
    answer = False
    sH = Counter(s)
    cnt = 0
    # for i in sH.values():
    #     if i % 2 == 1:
    #         if cnt != 0: return  False
    #         cnt +=1
    # return True

    odd = 0
    for key in sH:
        if sH[key]%2 == 1:
            odd +=1
    return odd <= 1

    # for i in range(len(s)//2):
    #     if s[i] == s[-1-i]:
    #         continue
    #     else:
    #         return False
    # return True
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
