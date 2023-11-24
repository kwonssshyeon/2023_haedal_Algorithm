from collections import Counter
def solution(s):
    sH = Counter(s)
    odd = 0
    for key in sH:
        if sH[key] % 2 == 1:
            odd += 1
    return odd <= 1     
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
