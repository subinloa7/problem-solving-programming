# 문제 1) N의 배수 출력하기 (Lv.1)
# 문제 : 두 정수 N과 M을 입력받아 N의 배수를 M개 출력하시오.
# 입력 (1) 두 정수 N, M이 주어짐. (2) 1 <= N, M <= 100
# 출력 : N의 배수를 작은 수부터 M개 출력함. 

N, M = map(int, input().split())
for i in range(1, M+1):
  print(N*i)
