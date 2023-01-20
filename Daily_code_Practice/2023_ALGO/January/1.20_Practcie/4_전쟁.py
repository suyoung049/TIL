import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = list(list(input().strip()) for _ in range(m))
check = [[False]*n for _ in range(m)]


def w_bfs(y,x):
    answer = 1
    q = deque([(y,x)])

    while q:
        (y,x) = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0<= nx < n and not check[ny][nx]:
                if matrix[ny][nx] == 'W':
                    check[ny][nx] = True
                    answer += 1
                    q.append((ny,nx))
    
    return answer


def b_bfs(y,x):
    answer = 1
    q = deque([(y,x)])

    while q:

        (y,x) = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0<= nx < n and not check[ny][nx]:
                if matrix[ny][nx] == 'B':
                    check[ny][nx] = True
                    answer += 1
                    q.append((ny,nx))
    
    return answer

w_power = 0
b_power = 0

for j in range(m):
    for i in range(n):
        if matrix[j][i] =='W' and not check[j][i]:
            check[j][i] = True
            w_power += (w_bfs(j,i)) ** 2

        elif matrix[j][i] =='B' and not check[j][i]:
            check[j][i] = True
            b_power += (b_bfs(j,i)) ** 2 

print(w_power, b_power)