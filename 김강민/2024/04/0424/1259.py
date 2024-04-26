import sys
input = sys.stdin.readline

while True:
    input_num = input().rstrip()
    
    if input_num == "0":
        break
    
    answer = "no"

    if input_num == input_num[::-1]:
        answer = "yes"
    
    print(answer)