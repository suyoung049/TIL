import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

def pprint(_list):
    for row in _list:
        print(row)

n = int(input())
value = sys.maxsize

matrix = [[value]*(n+1) for _ in range(n+1)]

m = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            matrix[i][j] = 0

for _ in range(m):
    j, i, k = map(int, input().split())
    if matrix[j][i] > k:
        matrix[j][i] = k

for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == value: #만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
            print(0, end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()