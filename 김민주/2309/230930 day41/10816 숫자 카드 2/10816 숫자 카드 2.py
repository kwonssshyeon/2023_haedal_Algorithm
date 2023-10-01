# [10816 숫자 카드 2](https://www.acmicpc.net/problem/10816)

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numbercards = list(map(int, input().split()))
    numbercards_dic = {}
    for number in numbercards:
        if number in numbercards_dic:
            numbercards_dic[number] += 1
        else:
            numbercards_dic[number] = 1

    # numbercards_dic = {숫자카드: 개수}
    
    m = int(input())
    numbers = list(map(int, input().split()))
    for i in range(m):
        if numbers[i] in numbercards_dic:
            print(numbercards_dic[numbers[i]], end=" ")
        else:
            print(0, end=" ")
    print()