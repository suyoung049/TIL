import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]

n, m, k = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

def bfs():
    sword = sys.maxsize
    q = deque([(0,0)])
    visit[0][0] = 1

    while q:
        y, x = q.popleft()
        if (y, x) == (n-1,m-1):
           
            return min(visit[y][x]-1, sword)

        if map[y][x] == 2:
            sword = (visit[y][x]-1) + (n-1-y) + (m-1-x)  # 검에서부터 공주까지 최단거리


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny <n and 0<= nx <m and visit[ny][nx] == 0:
                if map[ny][nx] == 0 or map[ny][nx] == 2:  # 0이라서 막혀있거나 2라서 검이라면 탐색 종료
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny,nx)) 
    return sword

result = bfs()
if result > k:
    print('Fail')
else:
    print(result)