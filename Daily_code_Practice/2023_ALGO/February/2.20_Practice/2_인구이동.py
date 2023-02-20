import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m, r = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def bfs(y,x):
    q = deque([(y,x)])
    stack = [(y,x)]

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n and not check[ny][nx]:
                if m<= abs(matrix[ny][nx]- matrix[y][x]) <= r:
                    check[ny][nx] = True
                    q.append((ny,nx))
                    stack.append((ny,nx))
    
    return stack

count = 0

while True:
    check = [[False]*n for _ in range(n)]
    people = False
    for j in range(n):
        for i in range(n):
            if not check[j][i]:
                check[j][i] = True
                temp = bfs(j,i)
                if len(temp) > 1:
                    people = True
                    people_num = 0
                    for i in temp:
                        people_num += matrix[i[0]][i[1]]
                    people_num = (people_num//len(temp))
                    for i in temp:
                        matrix[i[0]][i[1]] = people_num
    
    if people == False:
        break

    else:
        count += 1
                    
print(count)


