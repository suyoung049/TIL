num = input()

try:
    print(100/int(num))
except ZeroDivisionError:
    print('0으로 나눌수 없습니다.')
except ValueError:
    print('숫자 형식을 입력해주세요')