import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())

for test_case in range(T):
    m, n ,k = map(int, input().split())

    matrix = [[0] * n for _ in range(m)]
    check = [[False]*n for _ in range(m)]
   

    for _ in range(k):
        y, x = map(int, input().split())
        matrix[y][x] = 1
    
    def bfs(y,x):
       
        q = deque([(y,x)])
        check[y][x] = True

        while q:
            ey, ex = q.popleft()

            for i in range(4):
                ny = ey + dy[i]
                nx = ex + dx[i]

                if 0<= ny < m and 0<= nx < n and check[ny][nx] == False:
                    if matrix[ny][nx] == 1:
                        check[ny][nx] = True
                       
                        q.append((ny,nx)) 
        
                          
 
    
    count = 0
    for j in range(m):
        for i in range(n):
            if matrix[j][i] == 1 and check[j][i] == False:
                check[j][i] = True
                count += 1
                bfs(j,i)
                

                
    
    print(count)
