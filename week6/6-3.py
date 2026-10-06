# 문제 3) 로봇 이동 명령 (Lv.3)
# 문제 : 로봇이 정사각형 격자 안에서 이동함. 격자의 좌표 범위는 가로와 세로 모두 0 이상 N 이하이며, 
# 로봇의 시작 위치는 (0,0)임. M개의 명령을 순서대로 입력받아 실행시키시오.
# 마찬가지로 match-case를 사용하여 구현하시오.
# 입력 : 정수 N, M
# 출력 : (1) 첫번째 : 최종 좌표(X,Y) (2) 두번째 : 성공한 이동 횟수 (3) 세번째 : 실패한 이동 횟수
# 명령 조건 : (1) R : X 좌표를 1 증가시킴, L : X 좌표를 1 감소시킴 
# (2) U : Y 좌표를 1 증가시킴, D : Y 좌표를 1 감소시킴 
# (3) H : 시작 위치 (0,0)으로 복귀함 
# 이동 후 격자 밖으로 나가게 된다면 해당 이동을 취소하고 실패 횟수를 1 증가시킴 
# H는 항상 실행되며, 성공한 이동 횟수에 포함하지 않음
# 정의되지 않은 명령은 위치를 변경하지 않고 실패 횟수를 1 증가시킴
# R, L, U, D로 실제 한 칸 이동했을 때만 성공 횟수를 1 증가시킴

N, M = map(int, input().split())

X = 0
Y = 0
fail = 0
success = 0 

for i in range(M):
    명령 = input()
  
    match 명령:
      case "R":
        if X == N:
          fail += 1
        else:
          X += 1
          success += 1
          
      case "L":
        if X == 0:
          fail += 1
        else:
          X -= 1
          success += 1
          
      case "U":
        if Y == N:
          fail += 1
        else:
          Y += 1
          success += 1
            
      case "D":
        if Y == 0:
          fail += 1
        else:
          Y -= 1
          success += 1
            
      case "H":
        X = 0
        Y = 0

      case _:
        fail += 1

print(X, Y)
print(success)
print(fail)
