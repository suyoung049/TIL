import sys
from heapq import heappop, heappush
from collections import deque
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())

class_li = []
time_li = []
for _ in range(n):
    start, end = map(int, input().split())
    class_li.append((start, end))

class_li = sorted(class_li, key=lambda x:(x[0],x[1]))
class_li = deque(class_li)

for i in range(n):
    len_ = len(time_li)
    end = class_li.popleft()
    
    if len_ == 0:
        heappush(time_li, end[1])
    
    elif end[0] >= time_li[0]:
        heappop(time_li)
        heappush(time_li, end[1])

    else:
        heappush(time_li, end[1]) 

print(len(time_li))
