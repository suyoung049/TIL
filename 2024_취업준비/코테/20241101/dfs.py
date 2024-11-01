import sys
sys.stdin = open('3_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

cnt = 1
def dfs(start, graph, visit):
    global cnt
    visit[start] = cnt
    for n_node in graph[start]:
        if visit[n_node] == 0:
            cnt += 1  # 방문하지 않은 노드만 방문
            dfs(n_node, graph, visit) 


# 입력 처리
node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
visit = [0] * (node + 1)

# 그래프 생성
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 연결 리스트 정렬
for g in graph:
    g.sort()

# DFS 실행
dfs(start, graph, visit)

# 결과 출력
for i in range(1, node + 1):
    print(visit[i])




