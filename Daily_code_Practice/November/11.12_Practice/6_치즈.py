import sys
sys.stdin = open('6_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)] # 얇은 치즈가 놓여져 있는 판
sum_list = [] # 시간에 따른 공기와 만나서 녹은 치즈들의 수의 리스트

def bfs():
    check = [[False] * m for _ in range(n)]
    q = deque([(0,0)])
    check[0][0] = True # 시작지점이 정해져 있지 않으므로 (0,0) 에서 시작
    cheese = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and not check[ny][nx]: # 방문 여부만 확인 이동하면 안될 위치는 따로 지정되어 있지 않음

                if matrix[ny][nx] == 0: # 만약 공기(0) 라면 방문 처리만 표시 판 위는 변경 X
                    check[ny][nx] = True
                    q.append((ny, nx)) # 공기(0) 만 Q에 집어 넣어서 bfs 처리한다.(공기에 인접한 치즈만 녹는 알고리즘)

                elif matrix[ny][nx] == 1: # 만약 치즈(1) 라면 방문 처리후 공기와 밀접해 있기 때문에 공기(0)로 녹아버림
                    matrix[ny][nx] = 0
                    cheese += 1           # 녹은 치즈의 넓이 표시
                    check[ny][nx] = True  # 마찬가지로 방문표시만 해주고 Q에는 넣지 않는다(공기에 인접한 치즈만 녹게 하기 위해)
    sum_list.append(cheese)
    return cheese 


time = 0
while True:
    time += 1
    result = bfs()
    if result == 0: # 함수를 처리한 후 결과가 0이라면 녹은 치즈가 없다 모두 녹았다
        break

print(time-1)        # 치즈가 다 녹은 시간
print(sum_list[-2]) # 모두 녹기 한시간 전 치즈의 양(=마지막에 녹은 치즈의 양) 표시


