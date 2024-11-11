import sys
sys.stdin = open('1_input.txt', 'r')
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]

index = 0
indices = [[-1]*m for _ in range(n)]
low_link = [[-1]*m for _ in range(n)]
on_stack = [[False]*m for _ in range(n)]
stack = []
component_min_cost = []

dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

def strong_connect(x, y):
    global index
    indices[x][y] = index
    low_link[x][y] = index
    index += 1
    stack.append((x, y))
    on_stack[x][y] = True

    dir = maze[x][y]
    nx, ny = x + dx[dir], y + dy[dir]

    # 미로 밖으로 나가는 경우
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        pass
    else:
        if indices[nx][ny] == -1:
            strong_connect(nx, ny)
            low_link[x][y] = min(low_link[x][y], low_link[nx][ny])
        elif on_stack[nx][ny]:
            low_link[x][y] = min(low_link[x][y], indices[nx][ny])

    if low_link[x][y] == indices[x][y]:
        scc = []
        while True:
            tx, ty = stack.pop()
            on_stack[tx][ty] = False
            scc.append((tx, ty))
            if tx == x and ty == y:
                break
        # 사이클인지 확인
        if len(scc) > 1 or (len(scc) == 1 and (nx, ny) == (x, y)):
            min_cost = min(cost[tx][ty] for tx, ty in scc)
            component_min_cost.append(min_cost)

for i in range(n):
    for j in range(m):
        if indices[i][j] == -1:
            strong_connect(i, j)

print(sum(component_min_cost))