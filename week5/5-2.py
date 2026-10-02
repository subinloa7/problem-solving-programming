# 문제 2) 사분면 판단 (Lv.1)
# 문제 : 정수 X, 정수 Y 좌표를 입력받아, 해당 (X, Y)점이 어느 사분면에 속하는지 판단하는 프로그램을 작성하시오.
# 입력 : 정수 X, Y
# 사분면 : ex) (12, 5)인 점은 모두 양수이므로 1사분면 
# 출력 (X, Y 좌표 입력 -> 사분면 출력)

print("X 좌표 :", end="")
X = int(input())
print("Y 좌표 :", end="")
Y = int(input())

if X > 0 and Y > 0:
  print("제 1사분면에 있습니다.")
elif X < 0 and Y > 0:
  print("제 2사분면에 있습니다.")
elif X < 0 and Y < 0:
  print("제 3사분면에 있습니다.")
else:
  print("제 4사분면에 있습니다.")
