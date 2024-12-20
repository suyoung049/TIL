import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

A,B,N,M = input().split()


A= int(A)
B= int(B)
N=int(N)
M=int(M)

dy = [1, -1, A, -A, B, -B, A, B]

stone = [0] * 100001


def bfs(start):
    q = deque([start])
    

    while q:
        ey = q.popleft()

        for i in range(8):
            if i < 6 :
                ny = ey + dy[i]

                if 0<= ny < 100001 and stone[ny] == 0:
                    q.append(ny)
                    
                    stone[ny] = stone[ey] + 1

                
            else:
                ny = ey*dy[i]

                if 0<=ny<100001 and stone[ny] == 0:
                    q.append(ny)
                    
                    stone[ny] = stone[ey] + 1

bfs(N)
print(stone[M])