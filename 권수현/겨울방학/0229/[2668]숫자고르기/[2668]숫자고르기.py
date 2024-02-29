import sys
input = sys.stdin.readline

n = int(input())
nums={}
for i in range(1,n+1):
    nums[i] = (int(input()))

# cycle이 생기면 같은 집합임
# set 에 cycle의 원소를 add
    
result = set()

def dfs(node):
    global start

    if node==start and len(temp)!=0:
        result.update(temp)
    
    if not visited[nums[node]]:
        temp.append(nums[node])
        visited[nums[node]]=True
        dfs(nums[node])


for start in range(1,n+1):
    if start not in result:
        visited = [False]*(n+1)
        temp=[]
        dfs(start)

print(len(result))
result = sorted(list(result))
for i in range(len(result)):
    print(result[i])