import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

sa = {}
bam = {}

bord = [0] *101
check = [False] * 101

for _ in range(n):
    a, b = map(int, input().split())
    sa[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    bam[a] = b

def bfs(x):
    q = deque([x])

    while q:
        y = q.popleft()

        if y == 100:
            return bord[y]

        for dice in range(1,7):
            next = y + dice

            if 0 <= next <= 100 and not check[next]:
                if next in sa.keys():
                    next = sa[next]
                
                if next in bam.keys():
                    next = bam[next]
                
                if not check[next]:
                    check[next] = True
                    bord[next] = bord[y] + 1
                    q.append(next)

print(bfs(1))
                
            


