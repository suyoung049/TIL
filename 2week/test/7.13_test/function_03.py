print('hi', 'hello')
# 기본값이 sep는 ''으로 정의가 되어있다.
print('hi', 'hello', sep = '-')

print(1, 2, 3, 4, 5, 6, 7, 8)

# 정해지지 않은 갯수의 인자
def my_add(*numbers):
    return numbers

result = my_add(1, 2, 3)
print(result, type(result))
# 내부적으로 numbers가 tuple

def my_func(**kwargs):
    return kwargs
result = my_func(name = '이수영', age = '30', gender = 'M')
print(result, type(result))