import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n,m,k = map(int, input().split())  # 세로길이 n 가로길이 m  n * m  k 음식물 개수

matrix = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]




for _ in range(k):
    y,x = map(int, input().split())
    y,x = y-1 , x-1

    matrix[y][x] = 1

pprint(matrix)



def bfs(y,x):
    size = 1
    q = deque([(y,x)])
   
    while q:
        y , x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == 1 and check[ny][nx] == False:
                    check[ny][nx] = True
                    size += 1
                    q.append((ny,nx))
    return size

food = []

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 1 and check[j][i] == False:
            check[j][i] = True  
            food.append(bfs(j,i))

print(max(food))
            


    

