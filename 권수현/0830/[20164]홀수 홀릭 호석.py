import sys
input = sys.stdin.readline

num_list = list(map(int,input().strip()))



def check_odd(num):
    cnt = 0
    for i in num:
        if i%2==1:
            cnt+=1
    return cnt

def to_dec(num):
    length = len(num)-1
    result = 0
    for i in range(length,-1,-1):
        result+=num[i]*(10**(length-i))
    return result




def odd_holic(num_list):
    global maximum, minimum
    global temp
    if len(num_list)==1:
        temp+=check_odd(num_list)

        maximum = max(maximum,temp)
        minimum = min(minimum,temp)

        temp = 0
        
    
    elif len(num_list)==2:
        num_sum = sum(num_list)
        num_sum_list = list(map(int,str(num_sum)))

        if len(num_sum_list)!=1:
            temp+=check_odd(num_sum_list)
        odd_holic(num_sum_list)

    else:
        for i in range(1,len(num_list)-1):
            for j in range(i+1,len(num_list)):
                n1=num_list[:i]
                n2=num_list[i:j]
                n3=num_list[j:]

                num_sum = to_dec(n1)+to_dec(n2)+to_dec(n3)

                num_sum_list = list(map(int,str(num_sum)))
                
                temp += check_odd(num_sum_list) 
                odd_holic(num_sum_list)

    return maximum,minimum



                    


            


maximum = 0
minimum = 10000000
temp = 0
ans = odd_holic(num_list)
first_sum=check_odd(num_list)
print(first_sum+ans[1],first_sum+ans[0])
