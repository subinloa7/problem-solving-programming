# 문제 6) 연속 K일의 최고 매출 구간 찾기 (Lv.3)
# 문제 : (1) N일 동안의 매출을 리스트에 저장하시오. (2) 이 중 연속된 K일의 매출 합이 가장 큰 구간을 찾으시오.
# (3) 매출 합이 같은 구간이 여러 개이면 시작 날짜가 가장 빠른 구간을 선택하시오.
# 입력 : (1) 첫 번째 줄에 정수 N과 K가 공백으로 구분되어 주어짐 
# (2) 두 번째 줄에 N개의 매출이 공백으로 구분되어 주어짐 
# (3) 1 <= K <= N <= 100 (4) 각 매출은 0 이상 10,000 이하의 정수임 
# 출력 : (1) 첫 번째 줄에 선택한 구간의 시작 날짜와 마지막 날짜를 출력함 
# (2) 두 번째 줄에 해당 구간의 매출 합을 출력함 (3) 날짜는 1일부터 시작함 
# ex) 7 3 
# 10 20 15 30 25 10 20 
# 3 5
# 70

n, k = map(int, input().split())
sales = list(map(int, input().split()))

# n = 7, k = 3
# sales = [10 20 15 30 25 10 20]

# 시작일 / 합계 --> best
best_start = 0
best_sum = -1

for i in range(n - k + 1):
    # 현재 구간에서 가장 높은 값이 나오나?

    current = sales[i:i+k]  # i ~ i+k 구간이 잘린다
    total = 0
    for item in current: 
        total += item

    if total > best_sum:
        best_sum = total
        best_start = i

# 시작 날짜와 마지막 날짜 출력(시작 날짜는 1부터 시작)
print(best_start + 1, best_start + k)

# 매출 합
print(best_sum)
