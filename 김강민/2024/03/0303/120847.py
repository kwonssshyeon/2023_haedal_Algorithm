def solution(numbers):
    numbers.sort(reverse = True)
    return numbers[0] * numbers[1]

# sort() vs sorted()
# sort()는 리스트 자체를 정렬
# sorted()는 정렬된 리스트를 반환 -> 새로운 리스트 생성