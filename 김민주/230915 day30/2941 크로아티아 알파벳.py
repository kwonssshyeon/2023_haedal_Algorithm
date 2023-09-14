# [2941 크로아티아 알파벳](https://www.acmicpc.net/problem/2941)

word = input()

# 크로아티안 문자가 있으면 알파벳 한 글자로 대체
def replaceLetter(word):
    croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for letter in croatian:
        word = word.replace(letter, 'a')

    return word

word = replaceLetter(word)  
print(len(word))
