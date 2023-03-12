### 철로 

##### 풀이

각 경로를 순회하면서 집, 사무실 중 좌표값이 큰(더 오른쪽에 있는) 점에서 왼쪽으로 d 길이의 철로를 깔았을 때 철로에 몇개의 경로가 포함 되는지를 확인하는 방식으로 풀이

1) 먼저 각 사무실, 집 정보를 roads에 저장 할 때 사무실과 집의 거리가 d보다 d를 어떻게 움직여도 포함 될 수 없으므로 저장하지 않는다. d보다 작거나 같다면 좌표 정보를 오름차순으로 정렬해 저장
2) 철로의 시작점을 가장 작은 것부터 시작할 수 있도록 rados를 본인의 원소 중 큰 원소를 기준으로 오름차순 정렬해준다. (앞서 말한 것처럼 더 멀리 있는 좌표값에서 왼쪽으로 철로를 설치하기 때문에 더 멀리있는 좌표값(= 큰 원소)가 시작점이 된다.)
3) 철로의 시작점을 가장 작은 것부터 순회하면서 차례대로 힙에 넣어주게 된다. 이때 힙에 존재하는 가장 작은 값(최소힙)이 철로의 끝점안에 있는지 확인해 철로 내에 있지 않다면 힙에서 제거.



##### 철로 풀이를 위한 사전준비

- 시작, 끝, 숫자 비교 분리(입력값에서 작은 수를 start로 큰수를 end로 저장)
- start와 end 거리가 주어진 경로길이보다 크다면 포함 (X)
- 끝 위치를 기준으로 오름차순 정렬
  - 최대 포함 된 경로의 수 비교를 위해 끝위치가 작은 수부터 포함 시켜 최대수를 구하고 조건이 맞지 않는 다면 제거하는 방식
- 만약 현재 로드의 끝점에서 경로길이 만큼 뺀값을 비교 힙큐 안에 제일 작은 경로의 시작위치와 비교 벗어나면 

```python
heap_line[0][0] < road[1] - d
```

​		힙큐 안에서 제거





##### 이 문제가 우순 순위 큐 유형인 이유

힙큐 안에 포함 된 로드들의 제일작은값(최소 힙)이 비교 로드의 끝점에서 길이를 뺀 값안에 포함되어야 하므로



##### 철로 풀이 코드

```py
n = int(input())

line_list = []

for _ in range(n):
    a, b = map(int, input().split())
    if a > b : 
        start = b
        end = a
        line_list.append((start, end))
    else:
        start = a
        end = b
        line_list.append((start,end))

d = int(input())

roads = []
heap_line = []

for y, x in line_list:
    if x - y <= d:
        roads.append((y,x))

roads.sort(key=lambda x:x[1])
print(roads)


answer = 0
for road in roads:
    while True:
        if not heap_line:
            heappush(heap_line, road)
            break

        if heap_line[0][0] >= road[1] - d:
            heappush(heap_line, road)
            break

        heappop(heap_line)
    
    answer = max(answer, len(heap_line))

print(answer)
```

 