import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

matrix = [[0] * 101 for _ in range(101)]

for _ in range(n):

    y, x = map(int, input().split())

    for j in range(y, y + 10):
        for i in range(x, x + 10):
            if matrix[j][i] != 0:
                continue

            else:
                matrix[j][i] = 1


answer = 0
for k in range(101):
    for p in range(101):
        if matrix[k][p] == 1:

            for i in range(4):
                ny = k + dy[i]
                nx = p + dx[i]

                if 0<= ny < 101 and 0<= nx < 101:
                    if matrix[ny][nx] == 0:
                        answer += 1
print(answer)


