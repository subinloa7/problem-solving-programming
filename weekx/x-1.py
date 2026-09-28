# 문자열 반복해서 출력하기 
str, n = input().strip().split(' ')
n = int(n)

new_str = ' ' // 빈 문자열

for i in range(n):
  new_str += str

print(new_str) // print(str*n)
