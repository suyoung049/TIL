import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

def bfs(shark_y, shark_x, shark_size):
    fish = []
    check = [[False] * n for _ in range(n)]
    depth = [[0] *n for _ in range(n)]

    check[shark_y][shark_x] = True

    q = deque([(shark_y, shark_x)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and not check[ny][nx]:
                
                if map[ny][nx] < shark_size and map[ny][nx] != 0:
                    check[ny][nx] = True
                    depth[ny][nx] = depth[y][x] + 1
                    fish.append((ny, nx, depth[ny][nx]))

                elif map[ny][nx] < shark_size and map[ny][nx] == 0:
                    check[ny][nx] = True
                    depth[ny][nx] = depth[y][x] + 1
                    q.append((ny, nx))
                
                elif map[ny][nx] == shark_size:
                    check[ny][nx] = True
                    depth[ny][nx] = depth[y][x] + 1
                    q.append((ny, nx))
    
    # 핵심아이디어 pop을 해주기 위해서 내림차순 정렬 , 거리가 가까운 거 부터, y값이 작은거(위에서 부터), x 값이 작은거(왼쪽에서 부터) 
    return sorted(fish, key=lambda x:(-x[2], -x[0], -x[1])) 



shark_y, shark_x, shark_size = (0, 0, 2)

for j in range(n):
    for i in range(n):
        if map[j][i] == 9:
            shark_y, shark_x = j, i
            map[j][i] = 0


result = 0
fish_count = 0
while True:
    
    fish = bfs(shark_y, shark_x, shark_size)

    if len(fish) == 0:
        break

    else:
        # 우선순위 별로 다시 pop
        n_y, n_x, depth = fish.pop()

        result += depth

        map[n_y][n_x] = 0
        
        # 상어 시작 위치 조정
        shark_y, shark_x = n_y, n_x

        fish_count += 1

        if fish_count == shark_size:
            shark_size += 1
            
            # 상어 크기 커진 후에 초기화 필수 
            fish_count = 0

print(result)
