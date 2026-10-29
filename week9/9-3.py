# 문제 3) 리스트의 양 끝 값 더하기 (Lv.1)
# 문제 : (1) 리스트를 전달받아 첫 번째 값과 마지막 값의 합을 반환하는 함수 sum_ends(numbers)를 작성하시오.
# (2) 만약 리스트에 값이 하나뿐이면 해당 값을 두 번 더하시오.
# 입력 : (1) 첫 번째 줄에 정수 N이 주어짐 (1 <= N <= 100)
# (2) 두 번째 줄에 N개의 정수가 주어짐 
# (3) 각 정수는 -100 이상 100 이하임 
# 출력 : 첫 번째 값과 마지막 값의 합을 출력함 

def sum_ends(numbers):
  return numbers[0] + numbers[-1]

N = int(input())
numbers = list(map(int, input().split()))

print(sum_ends(numbers))
