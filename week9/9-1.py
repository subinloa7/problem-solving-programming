# 문제 1) 직사각형의 넓이 구하기 (Lv.1)
# 문제 : (1) 가로와 세로를 전달받아 직사각형의 넓이를 반환하는 함수 rectangle_area(width, height)를 작성하시오.
# (2) 입력받은 두 정수로 함수를 호출하고 반환값을 출력하시오.
# 입력 : 한 줄에 가로 W와 세로 H가 주어짐. (1 <= W, H <= 100)
# 출력 : 직사각형의 넓이를 출력함.

def rectangle_area(width, height):
    return width * height

W, H = map(int, input().split())

print(rectangle_area(W, H))
