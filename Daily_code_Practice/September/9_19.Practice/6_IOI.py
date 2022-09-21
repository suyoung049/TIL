import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())
IOI = list(input())

count = 0
result = 0
i = 1

while i < m-1:
    if IOI[i-1] == 'I' and IOI[i] == "O" and IOI[i+1] == 'I':
        count += 1

        if count == n:
            count -= 1
            result += 1

        i += 1 # 문자열이 포함되어 있으면 인덱스를 두번 더해서 OI를 찾아준다

    else:
        count = 0
    
    i += 1 # 맞지 않다면 1번 더해서 다른 배열을 시작한다.

print(result)