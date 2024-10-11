board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

def solution(board, skill):
    answer = 0
    m, n = len(board), len(board[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 1:
            degree *= -1

        # 내가 이런 문제에서 누적합을 떠올릴 수 있을까?????
        dp[r1][c1] += degree
        
        if c2 + 1 < n:
            dp[r1][c2 + 1] -= degree
        if r2 + 1 < m:
            dp[r2 + 1][c1] -= degree
        if c2 +1 < n and r2 + 1 < m:
            dp[r2 + 1][c2 + 1] += degree
    
    for j in range(m):
        for i in range(n - 1):
            dp[j][i+1] += dp[j][i]

    for i in range(n):
        for j in range(m-1):
            dp[j+1][i] += dp[j][i]

    for k in range(m):
        for p in range(n):
            board[k][p] += dp[k][p]
            if board[k][p] > 0:
                answer += 1
    
    return answer
print(solution(board, skill))