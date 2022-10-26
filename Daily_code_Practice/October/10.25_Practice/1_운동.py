import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

inf = sys.maxsize

n, m = map(int, input().split())

matrix = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    y, x, k = map(int, input().split())

    if matrix[y][x] > k:
        matrix[y][x] = k

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if j == i:
                matrix[j][i] = 0

            matrix[j][i] = min(matrix[j][i], matrix[j][k] + matrix[k][i])


for j in range(1, n+1):
    for i in range(1, n+1):
        if j != i:
            if matrix[j][i] != inf and matrix[i][j] != inf:
                if inf > matrix[j][i] + matrix[i][j]:
                    inf = matrix[j][i] + matrix[i][j]
                    
if inf == sys.maxsize:
    print(-1)

else:
    print(inf)





