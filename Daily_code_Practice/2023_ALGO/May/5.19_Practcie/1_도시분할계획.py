import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)
edge = []


def find_parent(parent, y):
    if parent[y] != y:
        parent[y] = find_parent(parent, parent[y])
    # 같을 때까지 연결이 부모노드를 찾는것
    return parent[y]

def union_parent(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n+1):
    parent[i] = i


for _ in range(m):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()
answer = 0
result = []

for cost, a, b in edge:
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)


    if parent_a != parent_b:
        union_parent(parent, parent_a, parent_b)
        result.append((cost, a, b))
        answer += cost

print(result)
