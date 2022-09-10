import sys
import heapq
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    a = int(input())
    if a == 0:
        if heap:
             print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-a,a))