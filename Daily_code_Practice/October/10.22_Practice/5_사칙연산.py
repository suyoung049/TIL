import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

sy, fy = map(int, input().split())


if sy == fy:
    print(0)
q = deque()
check = set()

def bfs():
    inf = sys.maxsize
    q.append((sy,''))
    check.add(sy)

    while q:
        y, s = q.popleft()

        if y == fy:
            return s

        ny = y * y
        if 0<= ny <= inf and ny not in check:
            q.append((ny,s +'*'))
            check.add(ny)

        ny = y + y
        if 0<= ny <= inf and ny not in check:
            q.append((ny,s+'+'))
            check.add(ny) 

        ny = 1
        if ny not in check:
            q.append((ny,s+'/'))
            check.add(ny)
    return -1

print(bfs())







