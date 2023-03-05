import sys
sys.stdin = open('6_input.txt')
from collections import deque

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 0, 0, 1, -1, 1, 1, -1, -1]
dx = [0, 1, -1, 0, 0, 1, -1, 1, -1]

matrix = deque(list(input().strip()) for _ in range(8))
pprint(matrix)

def bfs():
    q = deque([(7, 0)])
    turn = 0

    while q:
        check = [[False]* 8 for _ in range(8)]
        
        length_ = len(q)

        for _ in range(length_):
            y, x = q.popleft()
            
            # 만약 본인의 위치가 바닥 이동후 벽이라면 제거 벽이 이동했다는 소리는 본인의 위치도 위로 올라갔다
            if matrix[y][x] == '#':
                continue
            if (y, x) == (0,7):
                return 1

            # 본인이 이동하고 벽이 이동한다 
            for i in range(9):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < 8 and 0<= nx < 8 and not check[ny][nx]:
                    if matrix[ny][nx] == '.':
                        check[ny][nx] = True
                        q.append((ny, nx))

        # 벽 이동 로직
        matrix.pop()
        matrix.appendleft(['.','.','.','.','.','.','.','.'])
        
        turn += 1

        if turn == 9:
            return 1
    return 0


print(bfs())