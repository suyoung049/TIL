import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0

def find_parent(parent, y):
    if parent[y] != y:
        parent[y] = find_parent(parent, parent[y])
    return parent[y]

def union_parent(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    y, x ,cost = map(int, input().split())
    edges.append((cost, y, x))

edges.sort()

for edge in edges:
    cost, y, x = edge
    parent_y = find_parent(parent, y)
    parent_x = find_parent(parent, x)

    if parent_y != parent_x:
        union_parent(parent, parent_y, parent_x)
        result += cost

print(result)
