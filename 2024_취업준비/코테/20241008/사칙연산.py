arr = ["1", "-", "3", "+", "5", "-", "8"]
def solution(arr):
    answer = -1
    n = len(arr)
    for i in range(n):
        if arr[i].isdigit():
            arr[i] = int(arr[i])
    
    # 사칙연산을 위해 dp는 2개 필요
    max_dp = [[0 for _ in range(n)] for _ in range(n)]
    min_dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(0, n, 2):
        max_dp[i][i] = arr[i]
        min_dp[i][i] = arr[i]
    
    for length in range(3, n+1, 2):
        for left in range(0, n, 2):
            # length = right - left + 1
            right = length + left -1

            if right >= n:
                break

            min_candidate, max_candidate = [], []

            for operator in range(left+1, right, 2):
                if arr[operator] == '+':
                    max_candidate.append(max_dp[left][operator - 1] + max_dp[operator + 1][right])
                    min_candidate.append(min_dp[left][operator -1] + min_dp[operator + 1][right])
                else:
                    max_candidate.append(max_dp[left][operator - 1] - min_dp[operator + 1][right])
                    min_candidate.append(min_dp[left][operator -1] - max_dp[operator + 1][right])
                
            max_dp[left][right] = max(max_candidate)
            min_dp[left][right] = min(min_candidate)
        
    return max_dp[0][-1]


print(solution(arr))