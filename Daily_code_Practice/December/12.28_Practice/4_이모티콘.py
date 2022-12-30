import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

s = int(input())

# 2차원 리스트 방문표시를 딕셔너리로 표현(한번 생각해보기)
check = {}
check[(1,0)] = 0

# 너비우선 탐색
def bfs(x,y):
    q = deque()
    # (현재 이모티콘 개수, 클립보드에 개수)
    q.append((1,0))

    while q:
        now, clip = q.popleft()
        # 현재 이모티콘 개수가 s개라면
        if now == s:
            return check[now, clip] # 걸린 최소 시간 출력
        # 화면에 있는 모든 이모티콘 클립보드로 복사
        if (now, now) not in check.keys():
            check[(now, now)] = check[(now,clip)] + 1
            q.append((now,now))
        # 클립보드에 있는 모든 이모티콘 화면으로 붙여 넣기
        if (now+clip, clip) not in check.keys():
            check[(now+clip, clip)] = check[(now, clip)] + 1
            q.append((now+clip, clip))
        # 화면에 있는 이모티콘 중 하나를 삭제하기
        if (now-1, clip) not in check.keys():
            check[(now-1, clip)] = check[(now, clip)] + 1
            q.append((now-1, clip))

print(bfs(1,0))
