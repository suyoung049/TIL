import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]

max_len = 1

def bfs(y,x):
    global max_len
    word = matrix[y][x]

    q = set()
    q.add((y,x,matrix[y][x]))

    while q:
        y, x, word = q.pop()

        max_len = max(max_len, len(word))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if matrix[ny][nx] not in word:
                    q.add((ny, nx, word+matrix[ny][nx]))
    
bfs(0, 0)

print(max_len)