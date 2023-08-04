import sys
input = sys.stdin.readline

n = int(input())
input_data=[]
people_num=0
for i in range(n):
    location, person = map(int,input().split())
    input_data.append([location,person])
    people_num+=person

input_data.sort(key= lambda x:x[0])

middle = people_num/2
cnt=0
for i in range(n):
    cnt+=input_data[i][1]
    if(cnt>=middle):
        print(input_data[i][0])
        break


#location이 순서대로 주어지는게 아님
#중간값에 가까운 마을이 정답
#이게 왜 그리디...?