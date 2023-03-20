import sys
from heapq import heappush, heappop
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

coin = []

for _ in range(n):
    y = int(input())
    if y not in coin:
        coin.append(y)

coin.sort()

INF = sys.maxsize
check = [INF] * 100001

heapque = []
def dijkstra(start, count_):
    check[start] = 0
    heappush(heapque, (count_, start))

    while heapque:
        y, x = heappop(heapque)

        if check[x] < y:
            continue
   
        for i in range(len(coin)):
            nx = x + coin[i]


            if 0 <= nx < 100001:
                if check[nx] > y + 1:
                    check[nx] = y + 1
                    heappush(heapque, (y+1, nx))

dijkstra(0, 0)

if check[m] == INF:
    print(-1)

else:
    print(check[m])