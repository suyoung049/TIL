import sys
from heapq import heappop, heappush
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

m, n = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
inf = sys.maxsize
dp = [[inf] * m for _ in range(n)]

def dijkstra(y,x):
    ice = []
    dp[y][x] = 0
    heappush(ice, (dp[y][x], y, x))

    while ice:
        cost, cur_y, cur_x = heappop(ice)

        if dp[cur_y][cur_x] < cost:
            continue

        for next_y, next_x in zip(dy, dx):
            y, x = cur_y, cur_x
            next_cost = 0
            while True:
                if y+next_y < 0 or y+next_y >= n or x+next_x <0 or x+next_x >=m or matrix[y+next_y][x+next_x] == 11 or matrix[y+next_y][x+next_x]== 10 or matrix[y+next_y][x+next_x] == 12:
                    break
                else:
                    y += next_y
                    x += next_x
                    next_cost += matrix[y][x]
            
            if y+next_y < 0 or y+next_y >= n or x+next_x <0 or x+next_x >=m or matrix[y+next_y][x+next_x] == 10:
                continue
            elif matrix[y+next_y][x+next_x] == 12:
                y += next_y
                x += next_x
            if dp[y][x] > cost + next_cost:
                dp[y][x] = cost + next_cost
                heappush(ice, (dp[y][x], y, x))


for j in range(n):
    for i in range(m):
        if matrix[j][i] == "H":
            matrix[j][i] = 10
        elif matrix[j][i] == "R":
            matrix[j][i] = 11
        elif matrix[j][i] == "T":
            matrix[j][i] = 0
            start_y, start_x = j, i
        elif matrix[j][i] == "E":
            matrix[j][i] = 12
            end_y, end_x = j, i
        else:
            matrix[j][i] = int(matrix[j][i])

dijkstra(start_y, start_x)
if dp[end_y][end_x] == inf:
    print(-1)
else:
    print(dp[end_y][end_x])