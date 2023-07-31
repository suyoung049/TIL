import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())

matrix = [[0] * 1001 for _ in range(1001)]
answer = [0]

for i in range(1,n + 1):
    y, x, ny, nx = map(int, input().split())

    for j in range(y, y+ny):
        for k in range(x, x+nx):
            matrix[j][k] = i


for i in range(1, n+1):
    cnt = 0

    for j in range(1001):
        for k in range(1001):
            if matrix[j][k] == i:
                cnt += 1
            
    answer.append(cnt)
    cnt = 0

for i in range(n+1):
    if i == 0:
        continue
    print(answer[i])


