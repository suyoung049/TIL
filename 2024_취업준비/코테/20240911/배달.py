N = 5
K = 4
road = 	[[1,2,2],[1,3,3],[1,4,1],[1,5,10],[2,4,2],[3,4,1], [3,5,1], [4,5,3],[3,5,10],[3,1,8],[1,4,2],[5,1,7],[3,4,2],[5,2,4]]
from heapq import heappush, heappop

# 최단 경로
def solution(N, road, K):
    
    answer = 0
    graph = [[] for _ in range(N+1)]
    test = []
    for a, b, c in road:
        graph[a].append((b,c))
    for i in range(1,6):

        answer = short_root(i, graph, K)

        test.append(answer)
    print(test)
    return answer

def short_root(start, graph, k):
    INF = 2000 * 10000 + 1
    dp = [INF for _ in range(N+1)]
    answer = 0
    heap = []
    dp[start] = 0
    heappush(heap, (0, start))

    while heap:
        y, x = heappop(heap)
        
        # 시간 복잡도 감소를 위한 코드 
        if dp[x] < y:
            continue

        # 여기서 nx는 다음 노드, length는 노드까지 비용
        for nx, length in graph[x]:
            # y는 시작점에서 x 현재 노드사이의 비용
            n_length = y + length
            # 지금 까지 시작점에서 다음 노드까지의 경로중 비용보다 현재 비용이 작다면 갱신
            if dp[nx] > n_length:
                dp[nx] = n_length
                heappush(heap, (n_length, nx))

    for cnt in dp:
        if cnt <=k:
            answer += 1
    return dp


solution(N, road, K)
