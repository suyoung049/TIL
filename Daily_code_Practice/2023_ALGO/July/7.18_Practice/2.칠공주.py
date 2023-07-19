# 백트래킹 문제에서는 2차원 배열을 1차원 배열로 1차원 배열을 2차원 배열로 바꾸는 것을 생각
# 만약 5 * 5 2차원 배열이라면 (2, 3) 위치의 수는 index가 13이 된다. 
# 반대로 index를 다시 2차원 좌표로 바꾸기 위해서는 (13//5, 13%5) 가 될 수 있다. 
# 근데 언제 써야 할까??? 무작위로 7개 뽑을때??? 규칙이 일정하지 않을때 완전 탐색에 쓸만 할것 같음 일단 백트래킹을 언제 사용하는지 공부가 필요함

import sys
sys.stdin = open("2_input.txt", "r")
from collections import deque
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

answer = 0

def bfs(y,x):
    visit_check = [[0] * 5 for _ in range(5)]
    q = deque([(y,x)])
    connect_cnt = 1

    while q:
        y, x = q.popleft()
        visit_check[y][x] = 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny <5 and 0<= nx < 5 and not visit_check[ny][nx]:
                if seven_check[ny][nx] == 1:
                    visit_check[ny][nx] = 1
                    connect_cnt += 1
                    q.append((ny,nx))
    
    return connect_cnt

def check():
    for j in range(5):
        for i in range(5):
            if seven_check[j][i] == 1:
                if bfs(j,i) == 7:
                    return True

#  백트래킹으로 조합을 만들것 
def dfs(idx, student_cnt, som_cnt):
    global answer

    if student_cnt > 7:
        return
    # 종료조건
    if idx == 25:
        if student_cnt == 7 and som_cnt >= 4:
            if check():
                answer += 1
        return
    
    seven_check[idx//5][idx%5] = 1
    dfs(idx+1, student_cnt + 1, som_cnt + int(matrix[idx//5][idx%5] == "S"))
    seven_check[idx//5][idx%5] = 0
    dfs(idx + 1, student_cnt, som_cnt)


matrix = [list(input().strip()) for _ in range(5)]
seven_check = [[0] * 5 for _ in range(5)]

dfs(0, 0, 0)

print(answer)