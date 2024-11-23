import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(matrix):
    for x in matrix:
        print(x)
n, m = map(int, input().split())

MIN_INF = float('-inf')

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[MIN_INF for _ in range(m)] for _ in range(n)]

for y in range(n):
    left = [MIN_INF for _ in range(m)]
    right = [MIN_INF for _ in range(m)]

    # 왼쪽에서 오른쪽 이동
    for x in range(m):
        if y == 0 and x == 0:
            left[x] = matrix[0][0]
        else:        
            # 위에서 내려오는 경우
            if y <= 0:
                from_up = MIN_INF
            else:
                from_up = dp[y-1][x]
            # 왼쪽에서 오른쪽 가기
            if x <= 0:
                from_left = MIN_INF
            else:
                from_left = left[x-1]
            
            left[x] = max(from_left, from_up) + matrix[y][x]
    
    # 오른쪽에서 왼쪽 이동
    for x in range(m-1, -1, -1):
        if y == 0 and x == m-1:
            right[x] = dp[y][x]
        else:
            # 위에서 내려오는 경우
            if y <= 0:
                from_up = MIN_INF
            else:
                from_up = dp[y-1][x]
            
            # 오른쪽에서 왼쪽 가기
            if x >= m-1:
                from_right = MIN_INF
            else:
                from_right = right[x+1]
            right[x] = max(from_right, from_up) + matrix[y][x]
        
    for x in range(m):
        dp[y][x] = max(left[x], right[x])

print(dp[n-1][m-1])
        


