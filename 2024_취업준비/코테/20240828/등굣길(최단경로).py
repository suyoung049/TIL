m, n = 4, 3
puddles = [[2, 2]]

from collections import deque

def solution(m, n, puddles):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1

    dp[0][0] = 1

    queue = deque([(0,0)])
    while queue:
        y, x = queue.popleft()

        for k in range(2):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0<= ny <n and 0<= nx < m and dp[ny][nx] != -1:
                if dp[ny][nx] == 0:
                    queue.append((ny, nx))
                dp[ny][nx] += dp[y][x] % 1000000007
    print(dp)

    return dp[n-1][m-1] % 1000000007
    

print(solution(m, n , puddles))