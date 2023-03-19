import sys
from heapq import heappop, heappush
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
INF = sys.maxsize

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = [list(map(int, input().strip())) for _ in range(n)]
door = [[INF] * n for _ in range(n)]


heapque = []
def dijkstra(y,x):
    door[y][x] = 0
    heappush(heapque, (0, y, x))

    while heapque:
        cost, y, x = heappop(heapque)

        if door[y][x] < cost:
            continue


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny <n and 0 <= nx <n:
                if matrix[ny][nx] == 0:
                    n_cost = cost + 1
                
                else:
                    n_cost = cost

                
                if door[ny][nx] > n_cost:
                    door[ny][nx] = n_cost
                    heappush(heapque, (n_cost, ny, nx))


dijkstra(0, 0)
print(door[n-1][n-1])