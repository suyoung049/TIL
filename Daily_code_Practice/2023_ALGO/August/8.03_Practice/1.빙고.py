import sys
sys.stdin = open("1_input.txt",'r')
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]

lst = []

for i in range(5):
    lst += list(map(int, input().split()))


pos_lst = [0] * 26
for j in range(5):
    for i in range(5):
        pos_lst[board[j][i]] = (j,i)

v = [[0] * 10 for _ in range(4)]

for n in lst:
    j, i = pos_lst[n]
    v[0][j] += 1
    v[1][i] += 1
    v[2][j-i] += 1
    v[3][j+i] += 1

    cnt = 0
    
    for bingo in v:
        cnt += bingo.count(5)

    if cnt >= 3:
        break

print(sum(v[0]))