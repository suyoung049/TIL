import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y-1][x-1] = 1
    matrix[x-1][y-1] = 1

for k in range(n):
    for j in range(n):
        for i in range(n):
            if j == i:
                continue

            elif matrix[j][k] and matrix[k][i]:
                if matrix[j][i] == 0:
                    matrix[j][i] = matrix[j][k] + matrix[k][i]

                else:
                    matrix[j][i] = min(matrix[j][i], matrix[j][k] + matrix[k][i])

result = []

for j in range(n):
    result.append(sum(matrix[j]))

inf = sys.maxsize

for i in range(len(result)):
    if result[i] < inf:
        inf = result[i]
        answer = i

print(answer+1)


            
            
