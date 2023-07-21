import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

egg_board = [list(map(int, input().split())) for _ in range(n)]
egg_cnt = 0
break_cnt = 0
answer = 0


def dfs(egg_cnt, break_cnt):
    global answer
    if egg_cnt == n:
        answer = max(answer, break_cnt)
        return
    
    if egg_board[egg_cnt][0] <= 0:
        dfs(egg_cnt + 1, break_cnt)
    

    else:
        check = False
        for j in range(n):
            if egg_cnt == j or egg_board[j][0] <= 0:
                continue

            check = True
            egg_board[egg_cnt][0] -= egg_board[j][1]
            egg_board[j][0] -= egg_board[egg_cnt][1]

            dfs(egg_cnt + 1, break_cnt + int(egg_board[egg_cnt][0] <= 0) + int(egg_board[j][0] <= 0))

            egg_board[egg_cnt][0] += egg_board[j][1]
            egg_board[j][0] += egg_board[egg_cnt][1]
        
        if check == False:
            dfs(egg_cnt + 1, break_cnt)
dfs(egg_cnt, break_cnt)
print(answer)