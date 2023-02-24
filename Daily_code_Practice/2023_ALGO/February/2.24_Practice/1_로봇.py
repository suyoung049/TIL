import sys
sys.stdin = open('1_input.txt')
input = sys.stdin.readline
from collections import deque

def pprint(list_):
    for row in list_:
        print(row)

dy =[0, 0, 0, 1, -1] # 동 서 남 북
dx = [0, 1, -1, 0, 0] # 동 서 남 북

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[[False]*5 for _ in range(m)]for _ in range(n)]
start_y, start_x, start_dir = map(int, input().split())
end_y, end_x, end_dir = map(int, input().split())


def bfs(y,x,dir_):
    
    q = deque([(y,x,dir_,0)])
    check[y][x][dir_] = True

    while q:
        y,x,dir_,coun = q.popleft()

        if (y,x,dir_) == (end_y -1, end_x -1, end_dir):
            result = coun
            break

        for i in range(1,4):
            ny = y + (dy[dir_]*i)
            nx = x + (dx[dir_]*i)

            if 0<= ny < n and 0<= nx < m and not check[ny][nx][dir_]:
                
                if matrix[ny][nx] == 1: # 1을 가지 못하면 2,3도 갈수 없기 때문에
                    break
                
                else:
                    check[ny][nx][dir_] = True
                    q.append((ny,nx,dir_,coun+1))
            
        if dir_ == 1 or dir_ == 2:
            if not check[y][x][3]:
                check[y][x][3] = True
                q.append((y,x,3,coun+1))
            if not check[y][x][4]:
                check[y][x][4] = True
                q.append((y,x,4,coun+1))

        else:
            if not check[y][x][1]:
                check[y][x][1] = True
                q.append((y,x,1,coun+1))
            if not check[y][x][2]:
                check[y][x][2] = True      
                q.append((y,x,2,coun+1))  
    
    return result

print(bfs(start_y - 1, start_x - 1, start_dir))
