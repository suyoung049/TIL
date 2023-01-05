import sys
from collections import deque
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

count = 0
stay = [-1] * 51
visit = [0] * 51 

n, m = map(int, input().split())

def move(y):
    data = []
    for _ in range(stay[y]+1):
        data.append(y)
        y = visit[y]
    
    print(' ' .join(map(str, data[::-1])))



def bfs(s):
    global count
    stay[s] = 0

    q = deque([s])

    while q:
        y = q.popleft()

        if y == m:
            move(y)
            return

        
        for ny in (y+1, y-1, y*2):
            if 0<= ny < 51:
                if stay[ny] >= stay[y] +1 or stay[ny] == -1:
                    stay[ny] = stay[y] + 1
                    visit[ny] = y
                    q.append(ny)

bfs(n)


