from collections import deque
import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    def bfs():
        global q, f
        while q:
            temp = deque()
            while q:
                y, x = q.popleft()
                # 테두리면서 불이 아니라면 
                if (y == n - 1 or x == m - 1 or y == 0 or x == 0) and matrix[y][x] != '*':
                    return matrix[y][x] + 1

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if 0<= ny < n and 0<= nx < m and matrix[ny][nx] == '.' and matrix[y][x] != '*':
                        temp.append([ny,nx])
                        matrix[ny][nx] = matrix[y][x] + 1
            q = temp # 움직이는 거리 따로 저장
            if not q:
                break
                
            temp = deque()
            while f:
                y, x = f.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx [i]
                    if 0 <= ny < n and 0<= nx < m and check[ny][nx] == 0 and matrix[ny][nx] != '#':
                        temp.append([ny,nx])
                        check[ny][nx] = 1
                        matrix[ny][nx] = '*'
            f = temp # 불은 따로 저장



    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    m, n = map(int, input().split())

    matrix = [list(input().strip()) for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    q = deque()
    f = deque()

    for j in range(n):
        for i in range(m):
            if matrix[j][i] == '@':
                q.append([j,i])
                matrix[j][i] = 0

            elif matrix[j][i] == '*':
                f.append([j,i])
                check[j][i] = 1

    result = bfs()
    if result:
        print(result)
    else:
        print('IMPOSSIBLE')