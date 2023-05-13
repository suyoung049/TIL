import sys
sys.stdin = open("3_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]


# dp top-down 방식
def dfs(y,x):
    # 도착지점 도착시 1을 return
    if y == n-1 and x == m-1:
        return 1
    
    # 방문한적있는 곳이면 그 값 그대로 retrun
    elif dp[y][x] != -1:
        return dp[y][x]

    # 한번 방문한곳이 조건이 맞지 않아 다시 돌아가는거 방지(시간초과)
    dp[y][x] = 0
    
    # 문제에 주어진 조건에 따라 다음 높이가 낮으면 현재 위치의 dp 값에 저장
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0<= nx < m:
            if matrix[ny][nx] < matrix[y][x]:
                dp[y][x] += dfs(ny,nx)  
    
    return dp[y][x] 



print(dfs(0,0))
pprint(dp)

