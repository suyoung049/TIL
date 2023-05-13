import sys
from heapq import heappop, heappush
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n, m, k = map(int, input().split())

beer = []

for _ in range(k):
    pre, lev = map(int, input().split())
    beer.append((pre,lev))

beer = sorted(beer, key = lambda x:(x[1], x[0]))

good_beer = []
pre_sum = 0
check = True

for y, x, in beer:
    heappush(good_beer, (y,x))
    pre_sum += y
    if len(good_beer) == n:
        if pre_sum >= m:
            check = False
            print(x)
        
        else:
            pre_sum -= heappop(good_beer)[0]

if check == True:
    print(-1)








            
