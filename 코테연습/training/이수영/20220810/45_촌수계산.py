import sys

sys.stdin = open("45_input.txt", "r")

N = int(input())
x, y = map(int, input().split())
M = int(input())

graph_list = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for i in range(M):
    v1, v2 = map(int, input().split())
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)

stack = []
stack.append((x, 0))
visited[x] = True
answer = -1

while stack:
    number, count = stack.pop()

    if number == y:
        answer = count
        break
    
    for j in graph_list[number]:
        if not visited[j]:
            stack.append((j, count + 1))
            visited[j] = True
print(answer)





