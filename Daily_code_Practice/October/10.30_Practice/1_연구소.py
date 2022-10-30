import sys
from collections import deque
from itertools import combinations
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

virous = [] # 바이러스 심을 수 있는 위치 저장
count_ = 0

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 2:
            virous.append((j,i)) # 바이러스를 심을 수 있는 위치 
            count_ += 1      # 심지 않는 다면 0과 동일
        elif matrix[j][i] == 0:
            count_ += 1
pprint(matrix)

result = sys.maxsize
count_ -= m  # 바이러스 3개를 첨에 심으면 퍼트리는것과 는 무관 


for com_ in combinations(virous, m):
    check = [[-1] * n for _ in range(n)]
    q = deque()
    full = 0
    max_time = 0 # 조건문을 다 돌린 후에는 마지막까지 퍼트린 가장 최대 시간 출력

    for e in com_:
        q.append(e)
        check[e[0]][e[1]] = 0

    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n and matrix[ny][nx] != 1: # matrix[ny][nx] == 0 조건을 넣지 않는 이유는 2, 0 둘다 전파 가능
                if check[ny][nx] == -1:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
                    full += 1

    max_time = check[y][x]

    if full == count_:
        result = min(max_time, result)


if result == sys.maxsize:
    print(-1)
else:
    print(result)

