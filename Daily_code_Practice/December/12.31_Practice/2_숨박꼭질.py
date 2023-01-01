import sys 
sys.stdin = open('2_input.txt', 'r')
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())

inf = sys.maxsize

matrix = [inf] * 100001

stack = []

def dijk(n, m):
    if m <= n:
        return (n-m)

    heappush(stack, [0,n])

    while stack:
        w, n = heappop(stack)
        for nx in (n+1, n-1, 2*n):
            if 0 <= nx < 100001 :
                if nx == 2*n and matrix[nx] == inf:
                    matrix[nx] = w
                    heappush(stack, [w, nx])
                
                else:
                    if matrix[nx] == inf:
                        matrix[nx] = w+1
                        heappush(stack, [w+1, nx])
        
    return(matrix[m])

print(dijk(n,m))

