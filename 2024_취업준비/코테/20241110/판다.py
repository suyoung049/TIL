import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())
 
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[False]*n for _ in range(n)]

def dfs(y,x):
    # 방문기록이 있으면 해당 위치 dp값 return
    if dp[y][x] != False:
        return dp[y][x]
    
    # 방문기록이 없으면 판다위치 1로 초기화
    dp[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= ny < n and 0<= nx < n:
            if matrix[y][x] < matrix[ny][nx]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
                
    return dp[y][x]

# 시작점이 정해진게 아니라 완전탐색
answer = 0
for j in range(n):
    for i in range(n):
        answer = max(answer, dfs(j,i))
print(answer)