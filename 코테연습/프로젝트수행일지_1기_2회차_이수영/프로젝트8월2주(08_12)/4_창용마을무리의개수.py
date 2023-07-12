import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,(input().split()))
    graph_list = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for i in range(M):
        v1, v2 = map(int, input().split())
        graph_list[v1].append(v2)
        graph_list[v2].append(v1)
    
    
    def dfs(start):
        stack = [start]
        visited[start] = True
        
        while stack:

            current = stack.pop()

            for adj in graph_list[current]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)
    coun = 0
    for j in range(1, N+1):
        
        if not visited[j]:
            coun += 1 
        dfs(j) 
    print(f'#{test_case} {coun}')  

    # 문제에서 모두 아는 사이는 노드들이 모두 연결되어 있다는 뜻으로
    # 무리가 하나가 나오고 모두 연결되어 있지 않으면 Dfs 탐색을 진행하여 모두
    # 방문으로 바뀔때가지의 DFS 탐색횟수가 무리의 수가 되는 코드를 작성하였습니다.