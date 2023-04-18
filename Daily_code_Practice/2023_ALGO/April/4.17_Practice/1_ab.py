import sys
from collections import deque
sys.stdin = open("1_input.txt", 'r')
input = sys.stdin.readline

n, m = map(int, input().split())


def bfs(start,count_):
    
    q = deque([(start,count_)])

    while q:
        y,x = q.popleft()

        if y == n:
            return x

        if y%2 == 0:
            ny = y//2
            x = x+1
            q.append((ny,x))
        
        else:
            if y %10 == 1 and y >10:
                ny = y//10
                x = x + 1
                q.append((ny,x))
            else:
                return -1

result = bfs(m, 1)

print(result)

