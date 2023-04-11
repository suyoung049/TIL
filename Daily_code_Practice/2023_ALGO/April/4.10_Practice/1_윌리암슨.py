import sys
sys.stdin = open("1_input.txt", "r")
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = [list(map(int, input().strip())) for _ in range(n)]
check = [[0]*m for _ in range(n)]


def bfs(y, x, food_li):
    min_length = sys.maxsize
    q = deque([(y,x)])

    while q:
        y, x = q.popleft()
        if (y, x) in food_li:
            min_length = min(min_length, check[y][x])
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0 <= nx < m and check[ny][nx] == 0:
                if matrix[ny][nx] != 1:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
    
    return min_length

food_li = []

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 3:
            food_li.append((j,i))
        elif matrix[j][i] == 4:
            food_li.append((j,i))
        elif matrix[j][i] == 5:
            food_li.append((j,i))
        elif matrix[j][i] == 2:
            start_y, start_x = j, i

result = (bfs(start_y,start_x,food_li))

if result == sys.maxsize:
    print("NIE")

else:
    print("TAK")
    print(result)



            

        