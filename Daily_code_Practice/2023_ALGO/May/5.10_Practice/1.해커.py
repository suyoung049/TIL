import sys
from collections import deque
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

computer = [[] for _ in range(n+1)]

for _ in range(m):
    y, x = map(int, input().split())
    computer[x].append(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque([start])
    check[start] = True
    hacking = 0

    while q:
        next = q.popleft()

        for next_com in computer[next]:
            if not check[next_com]:
                check[next_com] = True
                hacking += 1
                q.append(next_com)

    return hacking
 
result = 1
answer = []
for i in range(1, n+1):
    h_com = bfs(i)
    if result < h_com:
        result = h_com
        answer.clear()
        answer.append(i)
    elif result == h_com:   
        answer.append(i)

print(*answer)

