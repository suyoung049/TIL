## 그래프 이론(DFS, BFS)



### 그래프 탐색 알고리즘: DFS/BFS

- 탐색(search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말합니다
- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있습니다.
- DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야 합니다.



### DFS(Depth-First Search)

- DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

- DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
  - 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
  - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리를 합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
  - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

```pytho
import sys
input = sys.stdin.readline

graph = [[], [2,3,8], [1,7], [1,4,5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
```



### BFS(Breadth-First Search)

- BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘 입니다.
- BFS는 큐 자료 구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 합니다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

```python
import sys
from collections import deque
input = sys.stdin.readline

graph = [[], [2,3,8], [1,7], [1,4,5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9



def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


bfs(graph, 1, visited)

```



## 기타 그래프 이론(최단 경로 & 기타 그래프 이론)

### 최단 경로 문제

- 최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미합니다
- 다양한 문제 상황
  - 한 지점에서 다른 한 지점까지의 최단 경로
  - 한 지점에서 다른 모든 지점까지의 최단 경로
  - 모든 지점에서 다른 모든 지점 까지의 최단 경로
- 각 지점은 그래프에서 노드로 표현
- 지점간 연결된 도로는 그래프에서 간선으로 표현



#### 다익스트라 최단 경로 알고리즘

- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작
  - 현실 세계의 도로(간선)은 음의 간선으로 표현 되지 않습니다.
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
  - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복



- 알고리즘의 동작 과정은 다음과 같습니다.
  1. 출발 노드를 설정
  2. 최단 거리 테이블을 초기화
  3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
  5. 위 과정에서 3번과 4번을 반복



- 다익스트라 알고리즘은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있습니다.
- 처리 과정에서 더 짧은 경로를 찾으면 '이제부터는 이 경로가 제일 짧은 경로야' 라고 갱신



##### 다익스트라 알고리즘의 특징

- 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않습니다.
  - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해 
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장
  - 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 함
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색) 합니다.



##### 다익스트라 기본 예제

```python
import sys
input = sys.stdin.readline

INF = sys.maxsize

# 노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단  거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)


# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)

    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
    
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print('INFINITY')

    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```

- 총 O(v)번에 걸쳐서 최단 거리가 짧은 노드를 매번 선형 탐색해야 합니다.
- 따라서 전체 시간 복잡도는 O(v^2)입니다.
- 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 이 코드로 문제를 해결 할 수 있습니다.
  - 하지만 노드의 개수가 10,000개는 넘어가는 문제라면 어떻게 해야 할까?

##### 우선순위 큐

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조입니다.
- 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있습니다.

##### 힙

- 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나입니다.
- 최소 힙(Min Heep) 과 최대 힙(Max Heap)이 있습니다.
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됩니다.



##### 다익스트라 알고리즘: 개선된 구현 방법

- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙(Heap) 자료구조를 이용합니다.
- 다익스트라 알고리즘이 동작하는 기본 원리는 동일합니다.
  - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료 구조를 추가적으로 이용한다는 점이 다릅니다
  - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용



##### 다익스트라 기본구현(힙큐 사용)

```python
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

# 노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 최단  거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)


# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있은 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):

    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
```

- 힙 자료 구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV) 입니다.
- 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V이상의 횟수로는 처리되지 않습니다.
  - 결과적으로 현재 우선 순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는 최대 간선의 개수(E)만큼 연산이 수행 될 수 있습니다.
- 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사합니다
  - 시간 복잡도는 O(ElogE)로 판단 할 수 있습니다
  - 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리 할 수 있습니다.
    - O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV) 



### 플로이드 워셜 알고리즘 개요

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산 합니다
- 플로이드 워셜(Floyd-Warshall) 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행 합니다.
  - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않습니다.
- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장
- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형에 속합니다.

- 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인합니다.

  - a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은 지 검사합니다.

- 점화식은 다음과 같습니다.

  ![점화식](그래프 이론(DFS, BFS).assets/점화식.png)

##### 플오이드 워셜 기본 구현

```python
import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0


# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a][b] = c

# 점화식에 따른 플로이드 워셔 알고리즘을 실행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k], graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        
        else:
            print(graph[a][b], end=' ')

print()
```



- 노드의 개수가 N개일 때, 알고리즘상으로 N번의 단계를 수행합니다
  - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경오를 고려
- 따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N^3)입니다.



### 기타 그래프 이론

#### 서로소 집합

- 서로소 집합(Disjoint Sets)란 공통 원소가 없는 두 집합을 의미합니다.



##### 서로소 집합 자료구조

-  서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조입니다.
- 서로소 집합 자료구조는 두 종류의 연산을 지원합니다.
  - 합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산입니다.
  - 찾기(Find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산입니다.
- 서로소 집합 자료구조는 합치기 찾기(Union Find) 자료구조라고 불리기도 합니다
- 여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같습니다
  1. 합집합(Union) 연산을 확인하여, 서로 연결되 두 노드 A, B를 확인합니다.
     1. A와 B의 루트 노드 A, B를 각각 찾습니다.
     2. A를 B의 부모 노드로 설정합니다.
  2.  모든 합집합(Union) 연산을 처리할 때까지 1번의 과정을 반복합니다.

- 기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없습니다.
  - 루트 노드를 찾기 위해 부모 테이블을 계속해서 확인하며 거슬러 올라가야 합니다
- 다음 예시에서 노드 3의 루트를 찾기 위해서는 노드2를 거쳐 노드 1에 접근해야 합니다.



##### 서로 집합 자료구조: 기본적인 구현 방법

```py
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parernt(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parernt(parent, a, b)

for i in range(1, v+1):
    print(find_parent(parent, i), end='')

```



##### 서로소 집합 자료구조: 기본적인 구현 방법의 문제점

- 합집합(Union) 연산이 편향되게 이루어지는 경우 찾기(Find)함수가 비효율적으로 동작합니다.
- 최악의 경우에는 찾기(Find) 함수가 다른 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V)입니다.
  - 다음과 같이 {1, 2, 3, 4, 5}의 총 5개의 원소가 존재하는 상황을 확인해 봅시다.

- 찾기(Find)함수를 최적화하기 위한 방법으로 경로 압축(Path Compression)을 이용할 수 있습니다.
  - 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신합니다. 

##### 서로소 집합 자료구조: 경로 압축

- 경로 압축 기법을 적용하면 각 노드에 대하여 찾기(Find)함수를 호출한 이후에 해당 노드의 루트 노드가 바로 부모 노드가 됩니다.
- 동일한 예시에 대해서 모든 합집합(Union)함수를 처리한 후 각 원소에 대하여 찾기(Find) 함수를 수행하면 다음과 같이 부모 테이블이 갱신 됩니다.

#### 서로소 집합을 활용한 사이클 판별

- 서로소 집합은 무방향 그래프 내에서 사이클을 판별할 때 사용할 수 있습니다.
  - 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용할여 판별 할 수 있습니다.
- 사이클 판별 알고리즘은 다음과 같습니다.
  1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인합니다.
     1. 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(Union)연산을 수행합니다.
     2. 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것입니다.
  2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복합니다.



##### 서로소 집합을 활용한 사이클 판별

```python
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parernt(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
if cycle:
    print('사이클이 발생했습니다.')

else:
    print('사이클이 발생하지 않았습니다.')
```



#### 신장트리

- 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미합니다.
  - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 합니다.

##### 최소 신장 트리

- 최소한의 비용으로 구성되는 신장 트리를 찾아야 할 때 어떻게 해야 할까요
- 예를 들어 N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결 될 수 있게 도로를 설치하는 경우를 생각해 본다.
  - 두 도시 A,B를 선택했을 때 A에서 B로 이동하는 경로가 반드시 존재하도록 도로를 설치 합니다

##### 크루스칼 알고리즘

- 대표적인 최소 신장 트리 알고리즘입니다.
- 그리디 알고리즘으로 분류 됩니다.
- 구체적인 동작 과정은 다음과 같습니다.
  1. 간선 데이터를 비용에 따라 오름차순으로 정렬
  2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
     1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
     2. 사이클이 발생하는 경우 최소 신장 트리에 포함 시키지 않는다
  3. 모든 간선에 대하여 2번의 과정을 반복



##### 크루스칼 알고리즘

````py
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parernt(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i]  = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번재 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edges
    if find_parent(parent, a) != find_parent(parent, b):
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        union_parernt(parent, a, b)
        result += cost
````

