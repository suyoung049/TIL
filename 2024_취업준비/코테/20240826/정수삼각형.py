triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    dp = [[0 for _ in range((n + 1)) ] for n in range(len(triangle))]
    dy = [-1, -1]
    dx = [-1, 0]

    for j in range(len(triangle)):
        for i in range(j+1):
            if (j, i) == (0, 0):
                dp[j][i] = triangle[j][i]
            
            else:
                max_num = 0
                for k in range(2):
                    ny = j + dy[k]
                    nx = i + dx[k]

                    if 0 <= nx <= ny:
                        max_num = max(max_num, dp[ny][nx])
                dp[j][i] = triangle[j][i] + max_num
    
    return max(dp[-1])

print(solution(triangle))