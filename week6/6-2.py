# 문제 2) 계산기 (Lv.1)
# 문제 : 두 정수 A, B와 연산 기호를 입력받아 계산 결과를 출력하시오. 연산 기호의 구분에는 match-case를 사용하시오.
# 입력 : (1) 정수 A, B (2) 연산 기호 (+, -, *, //, %)
# 출력 조건 : (1) //, % 연산에서 B가 0이면 ERROR를 출력하시오. (2) 표에 없는 연산 기호이면 INVALID를 출력하시오.

A, B, P = input().split() # 연산 기호 = P
A = int(A)
B = int(B)

# 출력 예시로 
# 15 7 
# //
# 이렇게 되어있기 때문에 

A, B = map(int, input().split())
P = input()

match P:
  case "+":
    print(A+B)
  case "-":
    print(A-B)
  case "*":
    print(A*B)
  case "//":
    if B == 0:
      print("ERROR")
    else:
      print(A//B)
  case "%":
    if B == 0:
      print("ERROR")
    else:
      print(A%B)
  case _:
    print("INVALID")
