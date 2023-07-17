# 경우의 수 가 여러개 나온다 -> 순열, 조합
# 여러개가 겹치게 나오고 수를 알아야 한다 -> Counter
# 방문 체크를 안해줘서 시간초과

import sys
from itertools import permutations
from collections import deque
sys.stdin = open("3_input.txt", "r")
input = sys.stdin.readline

n = int(input())

damage_li = []

for damage in permutations((9, 3, 1), 3):
    damage_li.append(damage)


dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]

hp = list(map(int, input().split()))

if n < 3:
    hp = hp + [0] *(3-n)


q = deque([(hp, 0)])


while q:
    hp, count_ = q.popleft()
    dp[hp[0]][hp[1]][hp[2]] = 1
    if hp == [0, 0, 0]:
        print(count_)
        break

    for hit in damage_li:
        next_hp = [0, 0, 0]

        for i in range(3):
            next_hp[i] = hp[i] - hit[i]

            if next_hp[i] < 0:
                next_hp[i] = 0
        
        if not dp[next_hp[0]][next_hp[1]][next_hp[2]]:
            dp[next_hp[0]][next_hp[1]][next_hp[2]] = 1
            q.append((next_hp, count_ + 1))
        
        

