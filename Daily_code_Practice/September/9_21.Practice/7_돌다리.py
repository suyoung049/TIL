import collections
import sys
from collections import deque
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

a, b, n, m = map(int, input().split())

dy = [1, -1, -a, a, b, -b, a, b]

stone = [0] * 1000001
visit = [False] * 10000001

def bfs(y):
    q = deque([y])
    visit[y] = True

    while q:
        y = q.popleft()

        for i in range(8):
            if i < 6 :
                ny = y + dy[i]

                if 0<= ny <1000001 and visit[ny] == False:
                    visit[ny] = True
                    stone[ny] = stone[y] + 1
                    q.append(ny)
            else:
                ny = y *dy[i]

                if 0<= ny < 1000001 and visit[ny] == False:
                    visit[ny] = True
                    stone[ny] = stone[y] + 1
                    q.append(ny)  

bfs(n) 
print(stone[m])     