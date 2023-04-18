import sys
from collections import deque
sys.stdin = open("1_input.txt", 'r')
input = sys.stdin.readline

n, s, m = map(int, input().split())

v_list = list(map(int, input().split()))
max_V = [set() for _ in range(n)]

q = deque([(s, 0)])

while q:
    v, idx = q.popleft()
    if idx == n:
        break

    for i in (v_list[idx], -v_list[idx]):
        n_v = v+i

        if 0<= n_v <=m and n_v not in max_V[idx]:
            q.append((n_v, idx+1))
            max_V[idx].add(n_v)
    


if not (max_V[n-1]):
    print(-1)
else:
    print((max(max_V[n-1])))