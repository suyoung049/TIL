import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline


n = int(input())

egg_board = [list(map(int, input().split())) for _ in range(n)]

answer = 0


for j in range(n):
    for i in range(n):
        if j == i:
            continue

        if egg_board[j][0] <= 0:
            continue

        egg_board[j][0] -= egg_board[i][1]
        egg_board[i][0] -= egg_board[j][1]

        if egg_board[j][0] <= 0:
            answer += 1
        if egg_board[i][0] <= 0:
            answer += 1

print(answer)

