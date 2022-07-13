# 통에 있는것을 꺼내서 변수명으로 나열
for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')

chars = input()
for i in chars:
    print(i)

# range 활용
chars = input() #range(len(chars))
for idx in range(len(chars)):
    print(chars[idx])