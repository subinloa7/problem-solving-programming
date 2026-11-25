# 문제 4) 선택 정렬로 오름차순 정렬하기 (Lv.1)
# 문제 : (1) N개의 정수를 입력받아 선택 정렬로 오름차순 정렬하시오.
# (2) 각 단계에서 정렬되지 않은 구간의 최솟값을 찾아 해당 구간의 첫 번째 원소와 교환하시오.
# 구현 조건 : (1) sort(), sorted(), min()을 사용하지 않음.
# (2) 최솟값의 위치를 저장하는 변수를 사용함.
# (3) 안쪽 반복문이 끝난 뒤 교환하며, 이미 올바른 위치에 있으면 교환하지 않음.
# 입력 : (1) 첫 번째 줄에 정수 N이 주어짐. (1 <= N <= 100)
# (2) 두 번째 줄에 N개의 정수가 공백으로 구분되어 주어짐. (-1,000 <= 각 정수 <= 1,000)
# 출력 : 정렬된 리스트를 공백으로 구분하여 한 줄에 출력함.
# 입출력 예제 :
# 예제 입력 :
# 5
# 5 3 4 1 2
# 예제 출력 :
# 1 2 3 4 5

N = int(input())
numbers = list(map(int, input().split()))

for i in range(len(numbers)-1):
  min_index = i
  
  for j in range(i+1, len(numbers)):
    if numbers[j] < numbers[min_index]:
      min_index = j

  if min_index != i:
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(*numbers)
