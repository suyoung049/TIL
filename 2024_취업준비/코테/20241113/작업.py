import sys
sys.stdin = open('1_input.txt', 'r')
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
task_time = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    input_li = list(map(int, input().split()))
    task_time[i] = input_li[0]
    prior_tasks = input_li[2:]
    in_degree[i] += len(prior_tasks)
    for prior in prior_tasks:
        graph[prior].append(i)

queue = deque()

# 진입 차수가 0인 작업을 큐에 추가하고 DP 초기화
for i in range(1, n+1):
    if in_degree[i] == 0:
        dp[i] = task_time[i]
        queue.append(i)

while queue:
    current = queue.popleft()
    for next_task in graph[current]:
        # 선행작업 진행
        in_degree[next_task] -= 1
        # 선행 작업이 모두 끝나는 시간
        dp[next_task] = max(dp[next_task], dp[current] + task_time[next_task])
        # 선행작업이 전부 끝나야 다음 작업으로 진행
        if in_degree[next_task] == 0:
            queue.append(next_task)

print(max(dp))