import sys
input = sys.stdin.readline

input_list = list(input().strip())
index = []
stack = []
case = []
final = set()

for i in range(len(input_list)):
    if input_list[i]=="(":
        input_list[i]=''
        stack.append(i)


    elif input_list[i] == ")":
        input_list[i]=''
        index.append([stack.pop(),i])


#조합 함수(재귀로 구현)
def findAllCase(index,n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(index)): 
        one = index[i] 
        rest_index = index[i + 1:] 
        for idx in findAllCase(rest_index, n-1): 
            result.append([one]+idx) 
              
    return result



n = len(index)
for i in range(n):
    case = findAllCase(index,i)
    for i in case:
        copy_input = input_list[:]
        for a,b in i:
            copy_input[a] = "("
            copy_input[b] = ")"
        final.add("".join(copy_input))

print(*sorted(final),sep='\n')
