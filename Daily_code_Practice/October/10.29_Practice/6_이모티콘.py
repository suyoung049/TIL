import sys
from collections import deque
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

def pprint(list_):
     for row in list_:
        print(row)

visit = [[-1] * (n+1) for _ in range(n+1)]

q = deque([(1,0)])

visit[1][0] = 0

while q:
    y, x = q.popleft()

    if visit[y][y] == -1:
        visit[y][y] = visit[y][x] + 1 # 화면의 이모티콘을 클립보드로 모두 복사한 경우
        q.append((y,y))

    if y + x <= n and visit[y+x][x] == -1:
        visit[y+x][x] = visit[y][x] + 1 # 클리보드의 이모티콘을 화면에 모두 붙여넣기
        q.append((y+x, x))
    
    if y-1 >= 0 and visit[y-1][x] == -1:
        visit[y-1][x] = visit[y][x] + 1 # 화면의 이모티콘을 하나 지우는 경우
        q.append((y-1, x))


answer = sys.maxsize
for i in range(n+1):
    if visit[n][i] != -1:
        if answer > visit[n][i]:
            answer = visit[n][i]

print(answer)
        