import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m, k = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]

my, mx, result, cheeze = 0, 0, 0, 1  # 처음 시작 위치, 움직인 거리, 치즈는 1부터 시작하므로 1을 주고 시작

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'S':  # 처음의 시작 위치를 찾아서
            my, mx = j, i        # 스타트 위치로 변경
            break


def bfs():
    global my, mx, result, cheeze
    q = deque([(my, mx, 0)])   # 움직인 거리를 함수에 주기
    check[my][mx] = True

    while q:
        y, x, d = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0 <= nx < m and not check[ny][nx]:
                if matrix[ny][nx] != 'X':                # 먹을 순서가 아닌 치즈도 이동이 가능하므로 제약 조건은 벽만 아니면 된다.
                    if '1' <= matrix[ny][nx] <= '9':    # 지정한 범위안에 있다면 치즈가 있는 위치
                        if cheeze == int(matrix[ny][nx]):
                            cheeze += 1      # 치즈는 1부터 9까지 있을 수 있으므로 1씩 더해주기
                            my, mx = ny, nx  # 1의 치즈를 먹고 그 위치에서 2까지 시작
                            result += (d+1)  # 주어진 치즈를 다은 최소 거리의 합        
                            return

                    check[ny][nx] = True
                    q.append((ny,nx,d+1))
            

for _ in range(k):
    check = [[False] * m for _ in range(n)]
    bfs()
    

print(result)    

list = ['1', '2', '3', '4', '5']
x = []

for i in list:
    if '2'< i < '5':
        x.append(i)

print(list)
print(x)