import sys
from collections import deque

sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

stay = [0] * 50


dy = [1, -1, 2]

def bfs(start):
    q = deque([start])

   
    
    while q:

        ey = q.popleft()

        for i in range(3):
            if i < 2:

                ny = ey + dy[i]

                if 0<= ny <50 and stay[ny] == 0:
                    
                    stay[ny] = stay[ey] + 1
                    q.append(ny)

            else:
                ny = ey*dy[i]

                if 0<= ny < 50 and stay[ny] == 0:
                    
                    stay[ny] = stay[ey] + 1
                    q.append(ny)

bfs(n)
print(stay[m])              
