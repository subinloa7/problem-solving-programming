# 문제 4) BMI 계산기 (Lv.2)
# 문제 : 키와 몸무게를 입력받아 BMI를 계산하고 현재 체중의 상태를 출력해주는 프로그램을 함수로 작성하시오.
# *BMI를 계산하는 함수와 BMI를 판정하는 함수를 작성하시오.
# 입력 : (1) 첫 번째 줄에 정수 H(키, cm 단위), W(몸무게)가 주어짐. (0 <= H, W <= 200)
# (2) BMI 계산은 = W(몸무게) / (H(m) * H(m)) 로 계산됨.
# < 18.5 : 저체중, 18.5 ~ 22.9 : 정상, 23 ~ 24.9 : 과체중, 25 ~ 29.9 : 경도비만, 30 이상 : 고도 비만
# 출력 : 각 BMI 구간에 맞춰 저체중, 정상, 과체중, 경도비만, 고도비만을 출력

def calculate_bmi(H, W):
    height = H / 100
    bmi = W / (height * height)
    return bmi

def check_bmi(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    elif bmi < 30:
        return "경도비만"
    else:
        return "고도비만"

H, W = map(int, input().split())

bmi = calculate_bmi(H, W)
result = check_bmi(bmi)

print(result)
