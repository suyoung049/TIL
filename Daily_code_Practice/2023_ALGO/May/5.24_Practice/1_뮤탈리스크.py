import sys
from collections import deque
from itertools import combinations, permutations
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

damege_li = []

for i in permutations((9, 3, 1), 3):
    damege_li.append(i)


dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]


n = int(input())

if n < 3:
    scv = list(map(int, input().split())) + [0] * (3-n)

else:
    scv = list(map(int, input().split()))


q = deque([(scv, 0)])

while q:
    hit, cnt = q.popleft()
    dp[hit[0]][hit[1]][hit[2]] = 1

    if hit == [0, 0, 0]:
        print(cnt)
        break

    for damage in damege_li:
       
        next_damage = [0, 0, 0]

        for i in range(3):
            temp = hit[i] - damage[i]

            if temp <= 0:
                temp = 0
            
            next_damage[i] = temp

        if not dp[next_damage[0]][next_damage[1]][next_damage[2]]:
            dp[next_damage[0]][next_damage[1]][next_damage[2]] = 1
            q.append((next_damage, cnt + 1))






            
