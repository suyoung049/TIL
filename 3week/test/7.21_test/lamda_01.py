# map(함수, 반복가능한 것)
# 반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과를
# map object로 변환한다.

# map(__, __)
# int 형 변환함수를
# input으로 받은 것을 쪼갠 결과인 리스트에 각각 적용한다.


numbers = [1, 2, 5, 19, 3, 9, 12]
result = []
for num in numbers:
    result.append(num * 3)
print(result)

def multiple_3(num):
    return num * 3

print(list(map(multiple_3, numbers)))

# 이 함수는 계속 사용되지 않고, map에서만 사용된다
# 임시적인 함수를 만들고 싶다 => lamda

print(list(map(lambda n: n*3, numbers)))