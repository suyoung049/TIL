import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    y, x = map(int, input().split())
    matrix[y][x] = 1 # 자신보다 큰사람

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if matrix[j][k]==1 and matrix[k][i]==1:
                matrix[j][i] = 1 # 자신보다 작은사람

answer = 0

for i in range(1, n+1):
    tall = 0
    for j in range(1, n+1):
        tall += (matrix[i][j] + matrix[j][i])

    if tall == n-1:
        answer += 1
pprint(matrix)
print(answer)

            
