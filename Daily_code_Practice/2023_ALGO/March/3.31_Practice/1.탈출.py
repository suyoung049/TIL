import sys
sys.setrecursionlimit(10**4)
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0]
dx = [0, 1]

n = int(input())

def pprint(list_):
    for row in list_:
        print(row)

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[None] * n for _ in range(n)]


def dfs(y,x):
    # 도착지점에서 출발 지점으로 Top_down 방식
    if (y,x) == (n-1, n-1):
        return 1
    
    # 만약 방문 한적이 있다면 그 지점을 방문한 경우의 수를 그대로 return
    if dp[y][x] is not None:
        return dp[y][x]
    
    dp[y][x] = 0
    # 방문 한적이 없다면
    for i in range(2):
        ny = y + dy[i] * matrix[y][x]
        nx = x + dx[i] * matrix[y][x]

        # 이동 할 수 있는 지점에서 다시 재귀 함수 호출 그 다음지점까지 갈 수 있는 경우의 수 return
        if 0<= ny < n and 0<= nx <n:
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]

print(dfs(0, 0))

