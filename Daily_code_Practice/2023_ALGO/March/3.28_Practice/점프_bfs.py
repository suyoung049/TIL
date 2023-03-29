import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

# bfs로 풀이하기 위해서는 이미 방문했던 돌이어도 그때와 다른 속도라면 재방문 가능

n, m = map(int, input().split())

block_stone = set()

for _ in range(m):
    small = int(input())
    block_stone.add(small)

check = [[] for _ in range(n+1)]

def bfs(start,speed, count_):
    q = deque([(start,speed,count_)])

    while q:
        y, x, count_ = q.popleft()
        
        for n_speed in (x-1, x, x+1):
            if n_speed > 0:
                next = y + n_speed
                
                if next == n:
                    return count_ + 1

                if next <= n and next not in block_stone:
                    if n_speed not in check[next]:
                        check[next].append(n_speed)
                        q.append((next, n_speed, count_ + 1))
    
    return -1
print(bfs(1, 0, 0))

