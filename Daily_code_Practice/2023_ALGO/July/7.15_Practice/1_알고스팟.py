import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline
from heapq import heappop, heappush

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

inf = sys.maxsize

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(m)]
dp = [[inf] * n for _ in range(m)]


def dijkstra(y,x):
    heap = []
    heappush(heap, (0, y, x))
    dp[y][x] = 0
    
    while heap:
        n_count, y, x = heappop(heap)

        if (y, x) == (m-1, n-1):
            return n_count
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < m and 0<= nx < n:
                if dp[ny][nx] < n_count:
                    continue
                
                h_count = n_count + matrix[ny][nx]
                
                if dp[ny][nx] > n_count:
                    dp[ny][nx] = n_count
                    heappush(heap, (h_count, ny, nx))

    return -1

print(dijkstra(0, 0))
