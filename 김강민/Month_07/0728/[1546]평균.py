N = int(input())
score = list(map(int, input().split()))
score.sort()

new_score = [i for i in range(N)]

for i in range(0, N):
    new_score[i] = score[i] / score[-1] * 100

sum = 0
for i in range(N):
    sum += new_score[i]

print(float(sum / N))