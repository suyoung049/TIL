rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX, characterY, itemX, itemY = 1, 3, 7, 8
from collections import deque
matrix = [[0 for _ in range(101)] for _ in range(101)]
def solution(rectangle, characterX, characterY, itemX, itemY):
    global matrix
    check = [[False for _ in range(101)] for _ in range(101)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    answer = 0
    for s_y, s_x, l_y, l_x in rectangle:
        make_line(s_y*2, s_x*2, l_y*2, l_x*2)

    queue = deque([(characterY * 2, characterX * 2, 0)])

    while queue:
        y, x, cnt = queue.popleft()

        if y == (itemY * 2) and x == (itemX * 2):
            return cnt//2
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < 101 and 0<= nx < 101 and matrix[ny][nx] == 1 and not check[ny][nx]:
                queue.append((ny, nx, cnt + 1))
                check[ny][nx] = True


def pprint(matrix):
    for x in matrix:
        print(x)

def make_line(s_y, s_x, l_y, l_x):
    global matrix
    for j in range(s_x, l_x + 1):
        for i in range(s_y,l_y + 1):
            if i == s_y or i== l_y or j == s_x or j == l_x:
                if matrix[j][i] == 0:
                    matrix[j][i] = 1
            else:
                matrix[j][i] = 2



print(solution(rectangle, characterX, characterY, itemX, itemY))