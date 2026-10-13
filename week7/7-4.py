# 문제 4) 누적 합 리스트 만들기 (Lv.2)
# 문제 : (1) N개의 정수를 리스트에 저장한 뒤, 첫 번째 값부터 각 위치까지의 합을 저장한 새로운 리스트를 만드시오.
# 예를 들어 [3, 5, 2]의 누적 합 리스트는 [3, 8, 10]임.
# 입력 : (1) 첫 번째 줄에 정수 N이 주어짐 (1 <= N <= 100)
# (2) 두 번째 줄에 N개의 정수가 주어짐 (-100 <= 각 값 <= 100)
# 출력 : 누적 합 리스트의 값을 공백으로 구분하여 출력함 
# ex) 5
# 3 5 2 7 1
# 3 8 10 17 18 
  
N = int(input())
data = list(map(int, input().split()))

total = 0
result = []
# prefix_sums = []

for i in range(N):
    total = total + data[i]
  # total += data[i]
    result.append(total)
  # prefix_sums.append(total)

print(*result)
# print(*prefix_sums)
