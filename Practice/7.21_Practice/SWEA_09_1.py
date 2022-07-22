# while 반복 => 길이가 10이 될 때 까지
#기록지
N = int(input())
N1 = N
numbers = set()
# for 반복 : 숫자를 문자로
# numbers set에 추가

while True:
    for n in str(N):
        numbers.add(n)
    if len(numbers) == 10:
        break
    N += N1
    print(N)
    