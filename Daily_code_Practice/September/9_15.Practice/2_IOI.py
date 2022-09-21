import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

m = int(input())

IOI = input()

result = 0
count = 0
i = 1  # index를 while 문으로 돌리기 위한 index 값 설정

while i < m-1:
    if IOI[i-1] == 'I' and IOI[i] == 'O' and IOI[i+1] == 'I':
        count += 1   # 'OI' 의 반복으로 n = count를 맞춘다
        if count == n: # 카운트와 개수가 맞았다면
            count -=1  #   n = 1 이상일경우 뒤에 'Oi'만 빼주면 다시 반복
            result += 1

        i += 1  # 'OI'를 반복 시키기 위해서

    else:
        count = 0
    i += 1           # 연속으로 안에 포함되는 문자열도 있기때문에 따로 지정

print(result)