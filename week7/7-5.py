# 문제 5) 가장 긴 연속 상승 구간 찾기 (Lv.3)
# 문제 : (1) N일 동안의 매출을 리스트에 저장하시오. 
# (2) 이 중 매일의 매출이 바로 전날보다 큰 상태로 이어지는 가장 긴 구간을 찾아 출력하시오.
# - 매출이 전날과 같거나 작으면 상승 구간이 끊어짐 
# - 하루만으로 이루어진 구간도 길이 1로 인정함
# - 가장 긴 구간이 여러 개이면 시작 날짜가 가장 빠른 구간을 선택함 
# 입력 : (1) 첫 번째 줄에 정수 N이 주어짐 (1 <= N <= 100)
# (2) 두 번째 줄에 N개의 매출이 주어짐 (0 <= 각 매출 <= 10,000)
# 출력 : (1) 첫 번째 줄에 가장 긴 상승 구간의 길이를 출력함 
# (2) 두 번째 줄에 해당 구간의 시작 날짜와 마지막 날짜를 출력함 
# (3) 날짜는 1일부터 시작함 
# ex) 8 
# 100 120 150 90 110 130 160 140 
# 4
# 4 7

N = int(input())
data = list(map(int, input().split())) # N일 동안의 매출 리스트

high_length = 1 # 상승 구간
max_high_length = 1 # 가장 긴 상승 구간
start_date = 1 # 시작 날짜
max_start_date = 1 # 가장 긴 구간의 시작 날짜

for i in range(1, N):
    if data[i] > data[i-1]:
        high_length += 1
    else:
        high_length = 1
        start_date = i + 1

    if high_length > max_high_length:
        max_high_length = high_length
        max_start_date = start_date

print(max_high_length)
print(max_start_date, max_start_date + max_high_length - 1)

# 교수님식 코드
N = int(input())
sales = list(map(int, input().split())) # N일 동안의 매출 리스트

# 현재 상승 구간
current_start = 0
current_length = 1

# 가장 긴 상승 구간 
best_start = 0 
best_length = 1

for i in range(1, N):
  if sales[i] > sales[i - 1]:
    current_length += 1
  else:
    # 상승이 끊어지면 현재 날짜부터 새 구간 시작 
    current_start = i
    current_length = 1

  # 더 긴 구간일 때만 갱신하여 동점이면 앞선 구간 유지
  if current_length > best_length:
    best_start = current_start
    best_length = current_length

# 인덱스를 1부터 시작하는 날짜로 변환
start_day = best_start + 1
end_day = best_start + best_length

print(best_length)
print(start_day, end_day)

# 나의 코드는 시작 위치가 1일부터 시작하는 날짜, 반복문 안에서 날짜 계산
# 교수님식 코드는 시작 위치가 0부터 시작하는 리스트 인덱스, 마지막에 날짜로 변환 (인덱스와 날짜의 차이를 알아야 함)
