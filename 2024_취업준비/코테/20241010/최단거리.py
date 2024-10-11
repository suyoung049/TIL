from collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    check = [[False for _ in range(m)] for _ in range(n)]
    check[0][0] = True
    que = deque([(0, 0, 1)])
    
    while que:
        (y,x, step) = que.popleft()

        if (y,x) == (n-1, m-1):
            return step
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and maps[ny][nx] == 1:
                if not check[ny][nx]:
                    check[ny][nx] = True
                    que.append((ny,nx, step + 1))
    return -1

print(solution(maps))