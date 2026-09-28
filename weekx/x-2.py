# 첫 번째로 나오는 음수 
def solution(num_list):
  answer = -1

for i in range(len(num_list)):
  if num_list[i] < 0:
    answer = i
    return answer
  return answr
