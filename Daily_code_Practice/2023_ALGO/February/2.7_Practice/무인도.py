from collections import deque
maps = ["XXX","XXX","XXX"]

for i in maps:
    m = len(i)

n = len(maps)
check = [[False]*m for _ in range(n)]
answer = []


def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(a, b, c):
    q = deque([(a,b)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and not check[ny][nx]:
                if maps[ny][nx] != 'X':
                    check[ny][nx] = True
                    c += int(maps[ny][nx])
                    q.append((ny,nx))
    return c
   



for j in range(n):
    for i in range(m):
        sum_ = 0
        if maps[j][i] != 'X' and not check[j][i]:
            check[j][i] = True
            sum_ += int(maps[j][i])
            answer.append((bfs(j, i, sum_)))

if not answer:
    print([-1])
else:
    answer.sort()
    print(answer)

        
