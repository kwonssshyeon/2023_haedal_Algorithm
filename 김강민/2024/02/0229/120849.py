def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    for i in vowel:
        my_string = my_string.replace(i, '')
        
    return my_string

# 다양한 방법이 있었는데, replace() 를 이용해서 공백으로 바꾸는 방법으로 풀었음!