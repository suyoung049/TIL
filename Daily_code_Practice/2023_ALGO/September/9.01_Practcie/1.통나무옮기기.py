import sys
from collections import deque
sys.stdin = open("1_input.txt")
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]

visited = set()

def bfs(start):
    q = deque([(start[0][0], start[0][1], start[1][0], start[1][1],start[2][0], start[2][1], 0)])
    visited.add((start[0][0], start[0][1], start[1][0], start[1][1],start[2][0], start[2][1]))

    while q:
        ay, ax, by, bx, cy, cx, cnt = q.popleft()
        if (ay,ax) == end[0] and (by,bx) == end[1] and (cy,cx) == end[2]:
            return cnt
        
        for i in range(4):
            nay = ay + dy[i]
            nax = ax + dx[i]
            nby = by + dy[i]
            nbx = bx + dx[i]
            ncy = cy + dy[i]
            ncx = cx + dx[i]

            if 0<= nay < n and 0<= nax < n and 0<= nby< n and 0 <= nbx < n and 0 <= ncy < n and 0<= ncx < n:
                if (nay, nax, nby, nbx, ncy, ncx) not in visited:
                    if matrix[nay][nax] != "1" and matrix[nby][nbx] != "1" and matrix[ncy][ncx] != "1":
                        visited.add((nay, nax, nby, nbx, ncy, ncx))
                        q.append(((nay, nax, nby, nbx, ncy, ncx, cnt + 1)))
        
        if by-1 == ay:
            if 0<= ax-1 < n and 0<= ax+1 < n:
                if matrix[ay][ax-1] != "1" and matrix[ay][ax+1] != "1" and matrix[by][bx-1] != "1" and matrix[by][bx +1] != "1" and matrix[cy][cx-1] != "1" and matrix[cy][cx+1] != "1":
                    nay = ay +1
                    nax = ax - 1
                    nby = by
                    nbx = bx
                    ncy = cy-1
                    ncx = cx +1

                    if 0<= nay < n and 0<= nax < n and 0<= nby< n and 0 <= nbx < n and 0 <= ncy < n and 0<= ncx < n:
                        if (nay, nax, nby, nbx, ncy, ncx) not in visited:
                            if matrix[nay][nax] != "1" and matrix[nby][nbx] != "1" and matrix[ncy][ncx] != "1":
                                visited.add((nay, nax, nby, nbx, ncy, ncx))
                                q.append(((nay, nax, nby, nbx, ncy, ncx, cnt + 1)))
        else:
            if 0<= ay-1 < n and 0<= ay +1 < n:
                if matrix[ay-1][ax] != "1" and matrix[ay+1][ax] != "1" and matrix[by-1][bx] != "1" and matrix[by+1][bx] != "1" and matrix[cy-1][cx] != "1" and matrix[cy+1][cx] != "1":
                    nay = ay-1
                    nax = ax +1
                    nby = by
                    nbx = bx
                    ncy = cy+1
                    ncx = cx-1
                    if 0<= nay < n and 0<= nax < n and 0<= nby< n and 0 <= nbx < n and 0 <= ncy < n and 0<= ncx < n:
                        if (nay, nax, nby, nbx, ncy, ncx) not in visited:
                            if matrix[nay][nax] != "1" and matrix[nby][nbx] != "1" and matrix[ncy][ncx] != "1":
                                visited.add((nay, nax, nby, nbx, ncy, ncx))
                                q.append(((nay, nax, nby, nbx, ncy, ncx, cnt + 1)))

start = []
end = []
for j in range(n):
    for i in range(n):
        if matrix[j][i] == "B":
            start.append((j,i))
        elif matrix[j][i] == "E":
            end.append((j,i))

result = bfs(start)
if not result:
    print(0)
else:
    print(result)


