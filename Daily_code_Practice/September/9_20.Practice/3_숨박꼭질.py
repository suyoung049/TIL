import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

dy = [1, -1, 2]

n, k = map(int, input().split())

stay = [0] * 50
visit = [False] * 50

def bfs(y):
    q = deque([y])
    visit[y] = True

    while q:
        y = q.popleft()

        for i in range(3):
            if i < 2:
                ny = y + dy[i]
            
                if 0<= ny < 50 and visit[ny] == False:
                    visit[ny] = True
                    stay[ny] = stay[y] + 1
                    q.append((ny))

            else:
                ny = y*dy[i]

                if 0<= ny < 50 and visit[ny] == False:
                    visit[ny] = True
                    stay[ny] = stay[y] + 1
                    q.append((ny))

bfs(n)
print(stay[k])

