import sys
from collections import deque
from itertools import permutations
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

# 로봇 청소기가 방을 돌아다니는 함수
def bfs(y, x):
    check = [[-1] * m for _ in range(n)]
    check[y][x] = 0
    q = deque([(y,x)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and check[ny][nx] == -1:
                if matrix[ny][nx] != "x":
                    q.append((ny, nx))
                    check[ny][nx] = check[y][x] + 1
    
    return check

while True:
    m, n = map(int, input().split())
    if not m or not n:
        break
    else:
        matrix = [list(input().strip()) for _ in range(n)]
        dust = []

        for j in range(n):
            for i in range(m):
                if matrix[j][i] == "o":
                    start_j, start_i = j, i
                elif matrix[j][i] == "*":
                    dust.append((j,i))
        
        visited = bfs(start_j, start_i)
        first_dust = [0] * len(dust)
        clean_check = True
        
        # 처음에 로봇청소기가 각각의 먼지들로 가는거리
        for idx, location in enumerate(dust):
            if visited[location[0]][location[1]] == -1:
                clean_check = False
                print(-1)
                break
            else:
                first_dust[idx] += visited[location[0]][location[1]]
        
        # 먼지 i 부터 나머지 먼지들로 가는 거리 차례대로 dp에 저장
        if clean_check:
            dp = [[0] * len(dust) for _ in range(len(dust))]
            for i in range(len(dust) -1 ):
                visited = bfs(dust[i][0], dust[i][1])
                for j in range(i+1, len(dust)):
                    dp[i][j] = visited[dust[j][0]][dust[j][1]]
                    dp[j][i] = dp[i][j]
            answer = sys.maxsize

            # 조합을 만들어서 청소기가 가는 순서대로 합친후 최소값 구하기
            for li in permutations(range(len(dust))):
                temp = first_dust[li[0]]
                start = li[0]
                for k in range(1, len(dust)):
                    end = li[k]
                    temp += dp[start][end]
                    start = end
                
                answer = min(answer, temp)
            
            print(answer)


        