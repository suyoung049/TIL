import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print (row)


n, m = map(int, input().split())
inf = sys.maxsize

matrix = [[inf] * (n+1) for _ in range(n+1)]

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y][x] = 1
    matrix[x][y] = 1

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if j == i:
                matrix[j][i] = 0

            else:
                matrix[j][i] = min(matrix[j][i],matrix[j][k]+matrix[k][i])

result = sys.maxsize
for j in range(1, n+1):
    kevin = 0
    for i in range(1, n+1):
        if matrix[j][i] == inf:
            kevin += 0
        else:
            kevin += matrix[j][i]

    if result > kevin:
        result = kevin
        p = j
        
    
print(p)
  