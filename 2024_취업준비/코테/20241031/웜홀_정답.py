import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def has_negative_cycle(n, graph):
    INF = float('inf')
    distance = [INF] * (n + 1)

    for start_node in range(1, n + 1):
        # distance[start_nod] != INF 아닐경우
        # 이미 다른 start_node의 사이클에 포함되어 있으므로 확인 X
        if distance[start_node] == INF:  
            distance[start_node] = 0
            # 벨만-포드 알고리즘을 통해 음의 사이클 탐색
            # 벨만-포드 알고리즘
            # 1. 만약 n-1번 반복 이후 최단거리가 갱신되면 음의 사이클 존재
            # 2. 정상적인 그래프는 n-1번 반복후 최단거리 갱신 X
            for i in range(n):
                # 갱신 여부 기록
                updated = False
                for u in range(1, n + 1):
                    for v, time in graph[u]:
                        if distance[v] > distance[u] + time:
                            distance[v] = distance[u] + time
                            updated = True
                            # (1번 사항) n번째 반복에서 갱신 발생 시 음의 사이클 존재
                            if i == n - 1:
                                return True
                # 더 이상 갱신이 없다면 n-1번 후에도 갱신 X 2번 사항 만족(음의 사이클 X)
                if not updated:  
                    break
    return False

t = int(input())  # 테스트 케이스 수

for _ in range(t):
    result = 'NO'
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    # 도로 정보 입력 (양방향)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 웜홀 정보 입력 (단방향)
    for _ in range(w):
        start, end, time = map(int, input().split())
        graph[start].append((end, -time))  # 웜홀의 가중치는 음수로 처리
    
    # 음의 사이클이 있는지 확인
    if has_negative_cycle(n, graph):
        result = "YES"
    print(result)