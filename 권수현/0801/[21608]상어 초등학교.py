import sys
input = sys.stdin.readline

n = int(input())
like_student={}
seat = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n**2):
    input_all = list(map(int, input().split()))
    student_num = (input_all[0])
    like_student[student_num] = input_all[1:]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for point, likes in like_student.items():
    max_like = 0
    max_blank = 0
    result = []
    for i in range(n):
        for j in range(n):
            if seat[i][j]==0:
                like = 0
                blank = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] in likes:
                            like += 1
                        
                        if seat[nx][ny] == 0:
                            blank += 1
                result.append((like,blank,i,j))


    result = sorted(result, key=lambda x : (-x[0],-x[1],x[2],x[3]))
    cur_x = result[0][2]
    cur_y = result[0][3]
    seat[cur_x][cur_y] = point

#print(seat)

sum = 0
for i in range(n):
    for j in range(n):
        point = seat[i][j]
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if (0 <= nx < n and 0 <= ny < n):
                if (seat[nx][ny] in like_student[point]):
                    count += 1


        if (count != 0):
            sum += 10**(count-1)

print(sum)