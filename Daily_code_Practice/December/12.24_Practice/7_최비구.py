import sys
from heapq import heappush, heappop
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = sys.maxsize

graph = [[] for _ in range(n+1)]
cost = [inf for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))

start, end = map(int, input().split())

def dijk(start):
    cost[start] = 0
    heap = []
    heappush(heap, (0,start))




dijk(start)
