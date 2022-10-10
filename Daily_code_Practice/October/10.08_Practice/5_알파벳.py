import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
count_ = 1



def bfs():
    global count_
    
    q = set([(0, 0, matrix[0][0])])
    
    

    while q:
        y, x, z = q.pop()
        count_ = max(count_, len(z))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if matrix[ny][nx] not in z:
                    q.add((ny, nx, z+matrix[ny][nx]))
                    
bfs()
print(count_)





