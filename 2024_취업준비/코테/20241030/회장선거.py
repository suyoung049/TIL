import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
inf = 10000

matrix = [[inf for _ in range(n+1)] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    matrix[a][b] = 1
    matrix[b][a] = 1

for k in range(n + 1):
    for j in range(n + 1):
        for i in range(n + 1):
            if j == i:
                continue
            matrix[j][i] = min(matrix[j][i], matrix[j][k] + matrix[k][i])


candidate = [-1 for _ in range(n+1)]

for j in range(1, n+1):
    for i in range(1, n+1):
        if matrix[j][i] == inf:
            continue
        candidate[j] = max(candidate[j], matrix[j][i])


result = inf
answer_li = []

for i in range(1, n+1):
    result = min(result, candidate[i])

for i in range(1, n+1):
    if candidate[i] == result:
        answer_li.append(i)

print(result, len(answer_li))
print(*answer_li)

