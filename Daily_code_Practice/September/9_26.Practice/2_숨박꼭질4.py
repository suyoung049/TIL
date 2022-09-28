import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

stay = [-1] * 50
visite = [0] * 50

def move(y):
    data = []
    temt = y
    for _ in range(stay[y]+1):
        data.append(temt)
        temt = visite[temt]
    print(' '.join(map(str,data[::-1])))



def bfs(start):
    q = deque([start])
    stay[start] = 0

    while q:
        y = q.popleft()

        if y == m:
            print(stay[y])
            move(y)
            return
        
        for ny in (y+1, y-1, 2*y):
            if 0<= ny < 50:
                if stay[ny] == -1 or stay[ny] >= stay[y]+1:
                    stay[ny] = stay[y] +1 
                    visite[ny] = y
                    q.append(ny) 
bfs(n)
