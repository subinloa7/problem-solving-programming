# 문제 6) 등급 출력하기 (Lv.1))
# 문제 : 학생 N명의 점수를 차례대로 입력받아 각 학생의 점수에 따라 등급을 출력하시오.
# 입력 : (1) 자연수 N (1 <= N <= 5) (2) 첫 번째 줄에 학생 수 N이 주어짐. (3) 이후 N개의 점수가 한 줄씩 주어짐.
# 출력 : (1) 학생의 점수를 입력할 때마다 해당하는 등급을 줄마다 출력함.
# (2) 등급표 : 90점 이상 - A, 80점 이상 90점 미만 - B, 70점 이상 80점 미만 - C, 70점 미만 - F

N = int(input())
for i in range(N):
  score = int(input())
  if score >= 90:
    print("A")
  elif score >= 80:
    print("B")
  elif score >= 70:
    print("C")
  else:
    print("F")
