import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

board = [[0] * 100 for _ in range(100)]

n = int(input())
answer = 0

for _ in range(n):
    sy, sx = map(int, input().split())
   
    for j in range(sy, sy+10):
        for i in range(sx, sx+10):
            if board[j][i] != 0:
                continue
            else:
                board[j][i] = 1
                answer += 1

print(answer)