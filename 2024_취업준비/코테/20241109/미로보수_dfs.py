import sys
sys.stdin = open('1_input.txt', 'r')
sys.setrecursionlimit(10 ** 7)

# 변수 선언
N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().strip() for _ in range(N)]
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 경로에 사이클이 있는지 확인
visited = [[0] * M for _ in range(N)]
# 현재 경로가 탐색완료된 경로인지 확인
done = [[0] * M for _ in range(N)]

# 방향 벡터 및 매핑
dy = [1, -1, 0, 0]  # D, U, R, L에 대한 y 좌표 변화
dx = [0, 0, 1, -1]  # D, U, R, L에 대한 x 좌표 변화
m = {'U': 1, 'D': 0, 'L': 3, 'R': 2}

answer = 0  # 총 비용 합계

def dfs(py, px):
    global answer
    visited[py][px] = 1  # 현재 노드 방문 표시
    dir = m[arr[py][px]]  # 현재 위치의 방향 얻기
    y = py + dy[dir]
    x = px + dx[dir]

    # 미로 밖으로 나가는 경우
    if x < 0 or y < 0 or x >= M or y >= N:
        done[py][px] = 1
        return

    if done[y][x]:
        done[py][px] = 1
        return
    elif visited[y][x]:
        # 사이클 감지됨
        sy, sx = y, x
        cc = float('inf')
        while True:
            cc = min(cc, cost[sy][sx])  # 사이클 내 최소 비용 찾기
            d = m[arr[sy][sx]]
            sy += dy[d]
            sx += dx[d]
            if sy == y and sx == x:
                break
        answer += cc
    else:
        dfs(y, x)  # 다음 노드로 이동

    done[py][px] = 1  # 현재 노드 처리 완료 표시

# 모든 노드에 대해 DFS 수행
for i in range(N):
    for j in range(M):
        if not done[i][j]:
            dfs(i, j)

print(answer)