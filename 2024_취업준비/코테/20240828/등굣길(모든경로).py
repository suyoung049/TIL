m, n = 4, 3
puddles = [[2, 2]]

def solution(m, n, puddles):
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = 0
    found_load = dfs(m, n, puddles, dp, (0,0))
    print(dp)
    return dp[0][0] % 1000000007

def dfs(m, n, puddles, dp, start):
    # 움직임이 왼쪽, 오른쪽 밖에 없어서 갈 수 있으면 무조건 최단 경로
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    if start == (n-1, m-1):
        return 1 % 1000000007

    elif dp[start[0]][start[1]] != -1:
        return dp[start[0]][start[1]] % 1000000007

    dp[start[0]][start[1]] = 0

    for k in range(2):
        ny = start[0] + dy[k]
        nx = start[1] + dx[k]

        if 0<= ny < n and 0<= nx < m and dp[ny][nx] != 0:
            dp[start[0]][start[1]] += dfs(m, n, puddles, dp, (ny, nx))

    return dp[start[0]][start[1]] % 1000000007

print(solution(m, n , puddles))