# 카페 주문 금액 계산기 프로그램 작성 
# 입력 : 음료 한 잔의 가격, 주문 수량, 할인율 (%)
# 계산 규칙 : (1) 총 주문 금액 = 가격 * 주문 수량 (2) 할인 금액 = 총 주문 금액 * 할인율 / 100 (3) 최종 금액을 안내 
# 실행 예시 : 
# 음료 가격을 입력하세요 : 4500, 주문 수량을 입력하세요 : 3, 할인율을 입력하세요(%) : 10
# 최종금액은 (13500-1350) = (12150)원 입니다.
# 최종 결제 금액을 입력해주세요 : 20000, 잔금은 7850원 입니다.

# 입력
price = int(input("음료 가격을 입력하세요: "))
quantity = int(input("주문 수량을 입력하세요: "))
discount_rate = float(input("할인율을 입력하세요: "))

# 계산 
total_price = price * quantity
discount_amount = total_price * discount_rate / 100
final_price = total_price - discount_amount

# 최종 금액 출력 
print(f"\n최종 금액은 ({total_price}-{discount_amount:.0f}) = ({final_price:.0f})원 입니다.")

# 결제 금액 입력 
payment = int(input("\n최종 결제 금액을 입력해주세요: "))

# 잔금 계산 
change = payment - final_price
print(f"잔금은 {change:.0f}원 입니다.")
