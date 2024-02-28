def solution(my_string, n):
    return ''.join(i * n for i in my_string)

# join() 함수를 사용하여 my_string을 n번 반복하여 반환합니다.
# 예를 들어, my_string이 "abc"이고 n이 3이면, "abcabcabc"를 반환합니다.
# 이 함수는 문자열을 반환하므로, 반환 값의 타입은 str입니다.