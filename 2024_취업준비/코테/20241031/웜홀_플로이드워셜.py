import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
INF = float('inf')

for _ in range(n):
    answer = "NO"
    node, root, wormhole = map(int, input().split())
    matrix = [[INF for _ in range(node + 1)] for _ in range(node + 1)]

    # 초기화
    for i in range(1, node + 1):
        matrix[i][i] = 0  # 자기 자신으로 가는 비용은 0

    # 도로 정보 입력 (양방향)
    for _ in range(root):
        a, b, c = map(int, input().split())
        matrix[a][b] = min(matrix[a][b], c)
        matrix[b][a] = min(matrix[b][a], c)
    
    # 웜홀 정보 입력 (단방향, 음수 가중치 처리)
    for _ in range(wormhole):
        start, end, limit = map(int, input().split())
        matrix[start][end] = min(matrix[start][end], -limit)

    # 플로이드-워셜 알고리즘
    for k in range(1, node + 1):
        for i in range(1, node + 1):
            for j in range(1, node + 1):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    # 음의 가중치 사이클이 있는지 확인
    for i in range(1, node + 1):
        if matrix[i][i] < 0:  # 대각선 요소가 음수이면 사이클 존재
            answer = "YES"
            break
    
    print(answer)