import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
move = 1

def bfs():
    global move
    q = set([(0, 0, matrix[0][0])])

    while q:
        y, x, z = q.pop()
        move = max(move, len(z))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] not in z:
                    q.add((ny, nx, z+matrix[ny][nx]))
                    print(q)

bfs()
print(move)



