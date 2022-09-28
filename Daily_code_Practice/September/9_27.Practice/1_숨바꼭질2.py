import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

stay = [-1] * 100001
count = 0

def bfs(start):
    global count
    stay[start] = 0
    
    q = deque([start])

    while q:
        y = q.popleft()

        if y == m:
            count += 1
            
           
        for ny in (y+1, y-1, 2*y):
            if 0<= ny < 100001:
                if stay[ny] == -1 or stay[ny] >= stay[y] + 1:
                    stay[ny] = stay[y] + 1
                    q.append(ny)


bfs(n)
print(stay[m])
print(count)

