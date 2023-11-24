from collections import Counter
def solution(s):
    sH = Counter(s)
    odd = 0
    for key in sH:
        if sH[key] % 2 == 1:
            odd += 1

    return len(s) - odd + 1 if odd > 0 else len(s)
    
                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
