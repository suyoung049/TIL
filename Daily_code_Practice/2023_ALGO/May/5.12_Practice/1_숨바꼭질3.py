import sys
sys.stdin = open("1_input.txt", "r")
from heapq import heappop, heappush
input = sys.stdin.readline

inf = sys.maxsize

n, k = map(int, input().split())

check = [inf] * 100001
q = []

def dijkstra(start, end):
    if start >= end:
        return(start-end)
    
    heappush(q, (0,start))

    while q:
        count_, y = heappop(q)

        for ny in [y-1, y+1, y*2]:
            if 0<= ny < 100001:
                if ny == y*2 and check[ny] == inf:
                    check[ny] = count_
                    heappush(q, (count_, ny))
                
                elif check[ny] == inf:
                    check[ny] = count_ + 1
                    heappush(q, (count_+1, ny))

    return check[k]


print(dijkstra(n, k))