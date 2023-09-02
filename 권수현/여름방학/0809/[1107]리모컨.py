import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
if n!=0:
    errors=list(map(int,input().split()))
else:
    errors=[]

current = 100
init_min = abs(current-target)

target_to_list=[]
#정수 자리수 분리
for i in str(target):
    target_to_list.append(int(i))

#target과 고장난 버튼이 겹치는지 체크
cnt = 0
flag = 0
for num in target_to_list:
    if num not in errors:
        cnt+=1
    else:
        flag =1
        break


# 10개버튼 모두 고장난 경우
if len(errors)==10:
    print(init_min)

# '''
# 1. start_num을 target자릿수만큼의 1111...로 고치면 아래 코드에서 시간단축 가능
# 2. target이 6자리인경우는 start_num 1000000으로 고치면 시간단축 가능

# 귀찮으니 나중에...

# def define_start():
#     for i in range(len(target_to_list)):
# '''

# target에 고장난 버튼이 포함된 경우
elif flag==1:
    start_num = 10**len(target_to_list)+2*10**(len(target_to_list)-1)
    error_cnt = start_num
    
    for i in range(start_num):
        sec_flag=0
        #정수 자리수 변환
        start_num_to_list=[]
        for j in str(i):
            start_num_to_list.append(int(j))

        for num in start_num_to_list:
            if num in errors:
                sec_flag=1
        if(sec_flag==0):
            val = len(start_num_to_list)+abs(i-target)
            error_cnt = min(error_cnt,val)

    print(min(error_cnt,init_min))


# target에 고장난 버튼이 포함되지 않는 경우
elif flag==0:
    print(min(init_min,cnt))