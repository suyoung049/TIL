num = ['1', '2', '3']

#  숫자로 바꿔서 쓰고 싶다?
# 리스트를 숫자로 형 변환은 불가능합니다.
# 다만, 숫자 형태의 문자를 변환할 수느 있습니다.

a = int(num[0])
b = int(num[1])
c = int(num[2])
new_num = [a, b, c]

new_num = []
for num in num:
    new_num.append(int(num))
print(new_num)