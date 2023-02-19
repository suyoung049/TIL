import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m, r = map(int, input().split())

map = [list(input().strip()) for _ in range(n)]



def loc_bomb():
    for j in range(n):
        for i in range(m):
            if map[j][i] == 'O':
                bomb.append((j,i))

def full_bomb():
    for j in range(n):
        for i in range(m):
            map[j][i] ='O'

def bombs():

    while bomb:
        y, x = bomb.popleft()
        map[y][x] = '.'

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if map[ny][nx] == 'O':
                    map[ny][nx] = '.'

r -= 1
while True:
    if r == 0:
        break
    bomb = deque()
    
    loc_bomb()

    full_bomb()

    r -= 1

    if r == 0:
        break

    bombs()
    r -= 1

for i in map:
    print("".join(i))
        