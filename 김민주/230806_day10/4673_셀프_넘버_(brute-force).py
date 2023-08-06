# https://www.acmicpc.net/problem/4673 셀프 넘버
## 1. 셀프넘버가 아닌 수를 제거한다(생성자가 있으므로)는 아이디어
## 2. 바로 제거하는 것보다 제거할 리스트를 따로 만들어 두는 것이 나음

def findSelfNums(nums):
  remove_list = []

  for i in nums: # 1 ~ 10000
    if i < 10: # 1 ~ 9
      remove_num = i + i # 1+1 = 2 ... 9+9 = 18
    elif i < 100: # 10 ~ 99
      remove_num = i + i//10 + i%10
    elif i < 1000: # 100 ~ 999
      remove_num = i + i//100 + i%100//10 + i%100%10
    else: # 1000 ~ 9999
      remove_num = i + i//1000 + i%1000//100 + i%1000%100//10 + i%1000%100%10
      
    if (remove_num in nums) and (remove_num not in remove_list): 
    # 10000 범위 밖인 수 방지, 중복 삭제 방지
      remove_list.append(remove_num)

  # self number이 아닌 수들 삭제하기
  for i in remove_list:
    nums.remove(i)

  return nums
  

if __name__ == "__main__":
  nums = list(range(1, 10001))

  answer = findSelfNums(nums)
  
  for num in answer:
    print(num)