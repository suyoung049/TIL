import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

check = [-1] * 1000001

def bfs(s):
    check[s] = 0
    q = deque([s])

    while q:
        y = q.popleft()

        if y == g:
            return check[g]
        
        for ny in (y+u, y-d):

            if 0 <= ny < 1000001 and check[ny] == -1:
                check[ny] = check[y] + 1
                q.append(ny)
    
    return 'use the stairs'
    
   
print(bfs(s))

