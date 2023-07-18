import sys
from collections import deque
sys.stdin = open("1_input.txt",'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m, p = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
damage_li = {}
player_li = []
idx_li = []

for i in range(p):
    player, damage = input().split()
    damage_li[player] = int(damage)

boss_hp = int(input())

check = [[[False] * p for _ in range(m)] for _ in range(n)]


def bfs(boss_location, player_li, boss_hp):
    q = deque(player_li)
    hit_boss = []

    while True:

        for _ in range(len(q)):
            player, y, x = q.popleft()

            idx = idx_li.index(player)

            if (y, x) == boss_location:
                hit_boss.append(player)

            if player in hit_boss:
                continue

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < n and 0 <= nx < m and not check[ny][nx][idx]:
                    if matrix[ny][nx] != 'X':
                        check[ny][nx][idx] = True
                        q.append((player, ny, nx))
        
        if hit_boss:
            for i in range(len(hit_boss)):
                player = hit_boss[i]
                if player in damage_li:
                    boss_hp = boss_hp - damage_li[player]
                if boss_hp <= 0:
                    return hit_boss

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'B':
            boss_location = (j, i)
        elif matrix[j][i] != "X" and matrix[j][i] != ".":
            idx_li.append(matrix[j][i])
            player_li.append((matrix[j][i], j, i))

answer = bfs(boss_location, player_li, boss_hp)
print(len(answer))



