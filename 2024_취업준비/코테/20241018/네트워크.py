n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
from collections import deque

def solution(n, computers):
    visit = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visit[i]:
            answer += 1
            bfs(computers, i, n, visit)
    return answer

def bfs(computers, i, n, visit):
    queue = deque([i])
    visit[i] = True

    while queue:
        com = queue.popleft()
        for j in range(n):
            if j == com:
                continue
            else:
                if computers[com][j] == 1 and not visit[j]:
                    queue.append(j)
                    visit[j] = True

print(solution(n, computers))