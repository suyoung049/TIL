import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

# not 연산자 잘 쓰기.
# not(a and b) = a 또는 b 둘중 하나 이상이 거짓인 경우 참
# not(a or b) = a와b가 모두 거짓인 경우 참


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
visited = [[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)] 




def bfs(double_coin):
    q = deque([(double_coin[0][0], double_coin[0][1], double_coin[1][0], double_coin[1][1])])
    visited[double_coin[0][0]][double_coin[0][1]][double_coin[1][0]][double_coin[1][1]] = 0

    while q:
        one_y, one_x, two_y, two_x = q.popleft()

        if visited[one_y][one_x][two_y][two_x] >= 10:
            return -1

        for i in range(4):
            n_one_y = one_y + dy[i]
            n_one_x = one_x + dx[i]
            n_two_y = two_y + dy[i]
            n_two_x = two_x + dx[i]

            if not(0<= n_one_y <n and 0<= n_one_x<m) and not(0<= n_two_y<n and 0<=n_two_x<m):
                continue
            
            if not(0<= n_one_y< n and 0<= n_one_x< m):
                return visited[one_y][one_x][two_y][two_x] + 1
            
            if not(0<= n_two_y< n and 0<=n_two_x< m):
                return visited[one_y][one_x][two_y][two_x] + 1

            if matrix[n_one_y][n_one_x] == "#":
               n_one_y, n_one_x = one_y, one_x
            if matrix[n_two_y][n_two_x] == "#":
                n_two_y, n_two_x = two_y, two_x

            if visited[n_one_y][n_one_x][n_two_y][n_two_x] == -1:
                visited[n_one_y][n_one_x][n_two_y][n_two_x] = visited[one_y][one_x][two_y][two_x] + 1
                q.append((n_one_y, n_one_x, n_two_y, n_two_x))
    return -1

double_coin = []
for j in range(n):
    for i in range(m):
        if matrix[j][i] == "o":
            double_coin.append((j,i))

print(bfs(double_coin))

