import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
j = max(matrix)
danger = max(j)

def bfs(y, x, k):
    q = deque([(y,x,k)])

    while q:

        y, x, k = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n and not check[ny][nx]:
                if matrix[ny][nx] > k:
                    check[ny][nx] = True
                    q.append((ny, nx, k))



result = []
for k in range(danger+1):
    check = [[False]*n for _ in range(n)]
    count = 0
    for j in range(n):
        for i in range(n):
            if matrix[j][i] > k and not check[j][i]:
                check[j][i] = True
                count += 1
                bfs(j,i,k)
    result.append(count)          


print(max(result))
    

