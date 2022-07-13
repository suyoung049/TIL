num = int(input())

if num >= 0:
    value = num
else:
    value = -num
print(num , value)

# 조건 표현식 코드
value = num if num >= 0 else -num 

# 조건문 변환
num = -5
value = num if num >= 0 else 0
print(value )

num = -5
if num >= 0:
    value = num
else:
    value = 0
print(value)