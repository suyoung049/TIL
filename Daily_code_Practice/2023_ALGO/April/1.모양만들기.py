import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 배열에 주어진 0을 하나하나 1로 바꾸면 시간초과 발생
# 첫 matrix에서 방문 표시를 해서 연결된 1의 개수를 count한 후에 
# 0을 하나만 바꿀 수 있기 때문에 배열에 0이 있다면 주변에 1을 세서 연결 만약 4방향이 전부 다른 연결 그림이라면 전부 합치는 연결 

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

def bfs(y, x, area):
    count_ = 1
    check[y][x] = area
    q = deque([(y,x)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and not check[ny][nx]:
                if matrix[ny][nx] == 1:
                    check[ny][nx] = area
                    count_ += 1
                    q.append((ny, nx))
    return count_

area = 1
sheap = {}
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 1 and not check[j][i]:
            sheap[area] = bfs(j,i,area)
            area += 1

answer = 0
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 0:
            zero_array = set()

            for k in range(4):
                ny = j + dy[k]
                nx = i + dx[k]

                if 0<= ny < n and 0<= nx < m and matrix[ny][nx] == 1:
                    if check[ny][nx] not in zero_array:
                        zero_array.add(check[ny][nx])
            
            
            result = 1

            for zero in zero_array:
                result += sheap[zero]

            answer = max(answer, result)

print(answer)            

