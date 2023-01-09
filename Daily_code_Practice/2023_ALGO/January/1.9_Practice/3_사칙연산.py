import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

if n == m:
    print(0)

def bfs(y,s):
    inf = sys.maxsize
    q = deque([(y,s)])
    check = []

    while q:

        y, s = q.popleft()

        if y == m:
            return s
        
        for ny in (y*y, y+y, 1):
            if ny == y*y:
                if 0<= ny <= inf and ny not in check:
                    q.append((ny, s+'*'))
                    check.append(ny)
            
            if ny == y+y:
                if 0<= ny <= inf and ny not in check:
                    q.append((ny, s+'+'))
                    check.append(ny)
            
            if ny == 1:
                if 0<= ny <= inf and ny not in check:
                    q.append((ny, s+'/'))
                    check.append(ny)
    
    return -1


s = ''
print(bfs(n,s))













answer = ''
bfs(m, answer)