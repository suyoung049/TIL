import sys
from heapq import heappop, heappush
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

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

        else:
            heappop(heap_line)
    
    answer = max(answer, len(heap_line))

print(answer)








    


    
