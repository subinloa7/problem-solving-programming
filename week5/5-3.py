# 문제 3) 3의 배수이며 짝수인 수 찾기 (Lv.1)
# 문제 : 정수 N을 입력받아 1부터 N까지의 정수 중 3의 배수이면서 짝수인 수의 개수와 합을 출력하는 프로그램을 작성하시오.
# 입력 : 정수 N
# 출력 (N 입력 -> 조건에 만족하는 수의 개수 출력 -> 해당 수들의 합 출력) : 만약 조건을 만족하는 숫자가 없으면 두 줄에 각각 0을 출력

print("정수 입력: ", end="")
N = int(input())

count = 0 # 개수
total = 0 # 합

for i in range(1, N+1):
  if i % 3 == 0 and i % 2 == 0:
    count += 1
    total += i 

print(count)
print(total)

# 교수님식 코드 
N = int(input("정수 입력: "))

count = 0 
sum = 0

for i in range(1, N+1):
  if i % 3 == 0 and i % 2 == 0:
    count += 1
    sum += i

print(count)
print(sum)
