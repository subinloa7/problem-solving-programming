# 문제 6) 나비 모양 별 찍기 (Lv.3)
# 문제 : 정수 N을 입력받아 나비 모양의 별을 출력하시오. 위쪽 N개의 줄에서는 양쪽 날개의 별을 늘리고, 아래쪽 N개의 줄에서는 별을 줄여 출력하시오.
# 입력 : 정수 N이 주어짐 (1 <= N <= 20)
# 출력 : (1) 총 2N개의 줄을 출력함 (2) 위쪽의 i번쨰 줄에는 별 i개, 공백 2(N-i)개, 별 i개를 순서대로 출력함 
# (3) 아래쪽은 위쪽을 위아래로 뒤집은 모양으로 출력함 (4) 가운데의 공백 없는 줄은 두 번 출력됨

N = int(input())

for i in range(1, N + 1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)

for i in range(N, 0, -1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)

# 교수님식 코드 
N = int(input()) # N = 4
# 위쪽 날개 : 양쪽 별이 늘어나고 가운데 공백이 줄어듦
for i in range(1, N+1):
    stars = "*" * i
    spaces = " " * (2 * (N-i))
    print(stars + spaces + stars)
# 아래쪽 날개 : 양쪽 별이 줄어들고 가운데 공백이 늘어남
for i in range(N, 0, -1):
    stars = "*" * i 
    spaces = " " * (2 * (N-i))
    print(stars + spaces + stars)
