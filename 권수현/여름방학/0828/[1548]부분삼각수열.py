import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

if n<=2:
    print(n)
    sys.exit()


data.sort()

start = 0
end = 2
maximum = 2
while end<n:
    # 맨앞 2개를 더한게 다음수보다 크면 그 다음수 검사
    if data[start]+data[start+1] > data[end]:
        maximum=max(maximum,end-start+1)
        end+=1
        continue
    # 작으면 맨앞을 옮김(끝에 닿을때까지)
    else:
        start+=1
        # 끝에 닿으면 끝을 옮김
        if start==end-1:
            end+=1

    

print(maximum)
        
    