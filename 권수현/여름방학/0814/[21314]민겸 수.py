import sys
input = sys.stdin.readline

input_str = list(map(str,input().strip()))



def toNumber(data):
    length = len(data)
    if data[-1]=='K':
        return 10**(length-1)*5
    elif data[-1]=="M":
        return 10**(length-1)
    


def find_max(input_str):
    check = 0
    max=''
    M = '1'
    for i in range(len(input_str)):
        if input_str[i] == 'K':
            max += str(toNumber(input_str[check:i+1]))
            check=i+1
    if input_str[-1]=="M":
        length = len(input_str[check:])
        max += M*length
    return max




def find_min(input_str):
    check = 0
    min=''
    flag = input_str[0]
    for i in range(1,len(input_str)):

        if (flag != input_str[i]) | (input_str[i]=="K"):
            min += str(toNumber(input_str[check:i]))
            check = i
            flag = input_str[i]


    min += str(toNumber(input_str[check:]))



    return min



print(find_max(input_str))
print(find_min(input_str))