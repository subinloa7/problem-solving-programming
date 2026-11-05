# 문제 4) 별로 그리는 정사각형 (Lv.3)
# 문제 : 홀수 N을 입력받아 가로와 세로가 N칸인 정사각형을 출력하시오.
# 정사각형의 테두리와 두 대각선에는 *을 출력하고, 나머지 위치에는 공백을 출력하시오.
# 입력 : 홀수 N (5 <= N <= 21)
# 출력 : (1) 총 N개의 줄에 각각 N개의 문자를 출력함. 
# (2) 첫 번째 행, 마지막 행, 첫 번째 열, 마지막 열에는 별을 출력함.
# (3) 왼쪽 위에서 오른쪽 아래로 이어지는 대각선에 별을 출력함. 
# (4) 오른쪽 위에서 왼쪽 아래로 이어지는 대각선에 별을 출력함.
# (5) 별을 출력하는 조건이 여러 개 겹쳐도 해당 위치에는 별을 하나만 출력함.
# (6) 나머지 위치에는 공백을 출력함.

N = int(input())

for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1 or i == j or i + j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 교수님식 코드 
N = int(input())

if N % 2 == 0:
    print("홀수를 입력하세요.")
else:    
    for row in range(N):
        for col in range(N):
            char = " "

            # 정사각형의 테두리
            if row == 0 or row == N - 1 or col == 0 or col == N - 1:
                char = "*"

            # 왼쪽 위 → 오른쪽 아래 대각선
            if row == col:
                char = "*"

            # 오른쪽 위 → 왼쪽 아래 대각선
            if row + col == N - 1:
                char = "*"

            # 각 위치에서 한 번만 출력
            print(char, end="")

        # 한 행의 출력이 끝나면 줄바꿈
        print()
